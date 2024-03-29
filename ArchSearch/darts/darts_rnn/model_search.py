import torch
import torch.nn as nn
import torch.nn.functional as F
from darts.darts_rnn.genotypes import PRIMITIVES, STEPS, CONCAT, Genotype
from torch.autograd import Variable
from collections import namedtuple
from darts.darts_rnn.model import DARTSCell, RNNModel


class DARTSCellSearch(DARTSCell):

  def __init__(self,config_layer,fix_weight, ninp, nhid, dropouth, dropoutx):
    super(DARTSCellSearch, self).__init__(config_layer,fix_weight,ninp, nhid, dropouth, dropoutx, genotype=None)
    self.bn = nn.BatchNorm1d(nhid, affine=False)
    self.fix_weight = fix_weight
  def cell(self, x,srnn_arch_weights):
    #s0 = self._compute_init_state(x, h_prev, x_mask, h_mask)
    #s0 = self.bn(s0)
    #probs = F.softmax(self.weights, dim=-1)
    probs = F.softmax(srnn_arch_weights, dim=-1)
    offset = 0
    #states = [x]
    states = x.unsqueeze(0)
    for i in range(STEPS):

      ###### Test multiple connections ########
      raw_out = torch.zeros(states.shape).cuda()
      aux_out = torch.zeros(x.shape).cuda()
      for idx,state in enumerate(states):

        raw_out[idx],h = self.layer[i](state)

      for k, name in enumerate(PRIMITIVES):
        if name == 'none':
          continue
        #fn = self._get_activation(name)
        if name == "tanh":
          #acc_out = torch.tanh(raw_out).clone()
          acc_out = F.tanh(raw_out)
        elif name == "relu":
          #acc_out = torch.relu(raw_out,inplace=False).clone()
          acc_out = F.relu(raw_out)
        elif name == "sigmoid":
          #acc_out = torch.sigmoid(raw_out).clone()
          acc_out = F.sigmoid(raw_out)
        elif name == "identity":
          acc_out = raw_out#raw_out.clone()
        else:
          raise NotImplementedError

        unweighted = acc_out#acc_out.clone()
        aux_out += torch.sum(probs[offset:offset+i+1, k].unsqueeze(-1).unsqueeze(-1).unsqueeze(-1) * unweighted, dim=0)
        #raw_out = raw_out + probs[i, k].unsqueeze(-1).unsqueeze(-1) * unweighted
      #s = self.bn(s)
      states = torch.cat([states, aux_out.unsqueeze(0)], 0)
      #states.append(aux_out)
      offset += i+1
    out = torch.mean(states[-CONCAT:], dim=0)
    #out = states[-1]
    return out


class RNNModelSearch(RNNModel):

    def __init__(self, *args):
        super(RNNModelSearch, self).__init__(*args, cell_cls=DARTSCellSearch, genotype=None)
        self._args = args
        self._initialize_arch_parameters()

    def new(self):
        model_new = RNNModelSearch(*self._args)
        for x, y in zip(model_new.arch_parameters(), self.arch_parameters()):
            x.data.copy_(y.data)
        return model_new

    def _initialize_arch_parameters(self):
      k = sum(i for i in range(1, STEPS+1))
      #weights_data = torch.randn(k, len(PRIMITIVES)).mul_(1e-3) #random arch init?
      weights_data = Variable(1e-3 * torch.randn(k, len(PRIMITIVES)).cuda(), requires_grad=True)
      weights_data_aux = weights_data.requires_grad_()
      #self.weights = weights_data_aux.cuda()
      self.weights = weights_data
      #self.weights = Variable(weights_data.cuda(), requires_grad=True)
      self._arch_parameters = [self.weights]
      for rnn in self.rnns:
        rnn.weights = self.weights

    def arch_parameters(self):
      return self._arch_parameters

    def _loss(self, hidden, input, target):
      log_prob, hidden_next = self(input, hidden, return_h=False)
      loss = nn.functional.nll_loss(log_prob.view(-1, log_prob.size(2)), target)
      return loss, hidden_next

    def genotype(self):

      def _parse(probs):
        gene = []
        start = 0
        for i in range(STEPS):
          end = start + i + 1
          W = probs[start:end].copy()
          j = sorted(range(i + 1), key=lambda x: -max(W[x][k] for k in range(len(W[x])) if k != PRIMITIVES.index('none')))[0]
          k_best = None
          for k in range(len(W[j])):
            if k != PRIMITIVES.index('none'):
              if k_best is None or W[j][k] > W[j][k_best]:
                k_best = k
          gene.append((PRIMITIVES[k_best], j))
          start = end
        return gene

      gene = _parse(F.softmax(self.weights, dim=-1).data.cpu().numpy())
      genotype = Genotype(recurrent=gene, concat=range(STEPS+1)[-CONCAT:])
      return genotype

    def fix_arch_params(self,arch_params):
      self.weights = arch_params
      self.fix_weight = True
      return
