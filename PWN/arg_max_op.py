import numpy as np
raw_1 = np.array([[0.34462299942970276, 0.056651100516319275, 0.38755953311920166, 0.04651886224746704, 0.09346675872802734, 0.07118072360754013], [0.38106968998908997, 0.06242651119828224, 0.3345657289028168, 0.0572095587849617, 0.09800855815410614, 0.06671992689371109], [0.15722045302391052, 0.05178187042474747, 0.08385489881038666, 0.4635729193687439, 0.09867461025714874, 0.14489531517028809], [0.2691325545310974, 0.05122624337673187, 0.09742151945829391, 0.19348418712615967, 0.13846217095851898, 0.25027331709861755], [0.09118465334177017, 0.03948397561907768, 0.332532674074173, 0.2867238223552704, 0.131205752491951, 0.11886915564537048], [0.19538477063179016, 0.03438626229763031, 0.22960194945335388, 0.2089391052722931, 0.1689463108778, 0.16274157166481018], [0.07630518823862076, 0.044274795800447464, 0.22248542308807373, 0.29875949025154114, 0.21134346723556519, 0.14683163166046143], [0.2767963111400604, 0.040278151631355286, 0.0979144498705864, 0.06109358370304108, 0.2168804556131363, 0.30703702569007874], [0.17233313620090485, 0.03839981555938721, 0.1565941721200943, 0.1728903204202652, 0.2162821739912033, 0.24350039660930634], [0.3300086557865143, 0.06748084723949432, 0.20389094948768616, 0.16657763719558716, 0.16360755264759064, 0.06843435019254684], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204]])
raw_2 = np.array([[0.3416835367679596, 0.05627020075917244, 0.3877824544906616, 0.045200083404779434, 0.09419243037700653, 0.07487118244171143], [0.376462459564209, 0.062121134251356125, 0.3409403860569, 0.057360853999853134, 0.09980969876050949, 0.06330546736717224], [0.15543921291828156, 0.05208428204059601, 0.09389808028936386, 0.4701766073703766, 0.09526462852954865, 0.13313721120357513], [0.2575332820415497, 0.04956765100359917, 0.09632163494825363, 0.19258834421634674, 0.14777719974517822, 0.25621193647384644], [0.08270895481109619, 0.03955977410078049, 0.33195728063583374, 0.28269508481025696, 0.13812285661697388, 0.12495609372854233], [0.18275891244411469, 0.035069677978754044, 0.23354123532772064, 0.21768097579479218, 0.166365385055542, 0.16458380222320557], [0.07980014383792877, 0.044074032455682755, 0.2188653200864792, 0.28619083762168884, 0.2118086963891983, 0.15926101803779602], [0.28492751717567444, 0.040449365973472595, 0.10651145875453949, 0.06270832568407059, 0.20841944217681885, 0.29698389768600464], [0.20968613028526306, 0.03828619047999382, 0.1477610021829605, 0.14962129294872284, 0.21422922611236572, 0.24041619896888733], [0.35268574953079224, 0.08043815195560455, 0.23814989626407623, 0.15047834813594818, 0.10921996086835861, 0.06902783364057541], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204]])
raw_3 = np.array([[0.10068845003843307, 0.055605825036764145, 0.12463489174842834, 0.2816646099090576, 0.18998456001281738, 0.24742168188095093], [0.2618028521537781, 0.05922666937112808, 0.28579026460647583, 0.2406405806541443, 0.07201817631721497, 0.08052138984203339], [0.1776115894317627, 0.191554456949234, 0.2632271349430084, 0.2204710692167282, 0.06763464212417603, 0.07950109988451004], [0.34551259875297546, 0.06738775968551636, 0.0856807753443718, 0.05537261813879013, 0.2204137146472931, 0.2256324738264084], [0.2650578022003174, 0.3271699845790863, 0.14095041155815125, 0.062305234372615814, 0.08567490428686142, 0.11884164810180664], [0.24478000402450562, 0.060672249644994736, 0.2838425040245056, 0.14785395562648773, 0.1750153750181198, 0.08783584088087082], [0.4048154354095459, 0.0846320241689682, 0.1756366640329361, 0.16241422295570374, 0.05721447244286537, 0.11528710275888443], [0.30069398880004883, 0.430580198764801, 0.09105779975652695, 0.06311395019292831, 0.05456864461302757, 0.05998539179563522], [0.33964255452156067, 0.07351294904947281, 0.10946255922317505, 0.10033373534679413, 0.08699683845043182, 0.29005134105682373], [0.31310173869132996, 0.0563126765191555, 0.20347468554973602, 0.13729089498519897, 0.07789786905050278, 0.21192209422588348], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204]])
raw_4 = np.array([[0.3125494718551636, 0.06651417911052704, 0.35406821966171265, 0.0806451365351677, 0.05184901878237724, 0.13437393307685852], [0.33108529448509216, 0.06684280931949615, 0.05990103632211685, 0.11721157282590866, 0.1580294668674469, 0.26692983508110046], [0.3336845934391022, 0.07084020972251892, 0.10259146243333817, 0.10913090407848358, 0.1689848005771637, 0.21476799249649048], [0.2009722739458084, 0.06331279128789902, 0.06755834817886353, 0.28432542085647583, 0.3133610188961029, 0.07047008723020554], [0.14926907420158386, 0.0604906864464283, 0.1535804271697998, 0.24126845598220825, 0.32730963826179504, 0.06808175146579742], [0.24708102643489838, 0.058430664241313934, 0.0874100849032402, 0.2441239356994629, 0.2908115088939667, 0.07214276492595673], [0.3780967593193054, 0.07430849969387054, 0.08007761836051941, 0.06508555263280869, 0.34806984663009644, 0.054361723363399506], [0.2958943545818329, 0.06636925786733627, 0.1390400230884552, 0.09256640076637268, 0.35762178897857666, 0.04850814491510391], [0.30172210931777954, 0.06356916576623917, 0.137773334980011, 0.10351718962192535, 0.33706000447273254, 0.05635816603899002], [0.32356759905815125, 0.18121449649333954, 0.054956961423158646, 0.05458005145192146, 0.32889795303344727, 0.05678296089172363], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204]])
raw_5 = np.array([[0.12012460827827454, 0.0456487201154232, 0.2721903622150421, 0.3190873861312866, 0.04382813349366188, 0.19912083446979523], [0.34922659397125244, 0.05242316052317619, 0.3192919194698334, 0.11977493017911911, 0.11995662748813629, 0.03932669758796692], [0.059770893305540085, 0.04421452060341835, 0.057475727051496506, 0.08338110148906708, 0.34176546335220337, 0.41339239478111267], [0.36458614468574524, 0.050716791301965714, 0.22603437304496765, 0.16597865521907806, 0.03977289795875549, 0.15291112661361694], [0.0686432272195816, 0.044296760112047195, 0.053226929157972336, 0.05432179570198059, 0.33878591656684875, 0.4407254755496979], [0.20948709547519684, 0.04283890873193741, 0.17653235793113708, 0.28521955013275146, 0.16863615810871124, 0.11728598177433014], [0.2798829674720764, 0.044218000024557114, 0.08669473230838776, 0.03321447968482971, 0.2604334056377411, 0.2955564260482788], [0.14236541092395782, 0.056233689188957214, 0.1661246418952942, 0.4947427213191986, 0.08505930006504059, 0.05547427386045456], [0.13315145671367645, 0.0465836264193058, 0.41102108359336853, 0.21937435865402222, 0.078132264316082, 0.11173715442419052], [0.3513651192188263, 0.05398283526301384, 0.3649841248989105, 0.049986690282821655, 0.08956728875637054, 0.09011400490999222], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204], [0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204, 0.1666666716337204]])
#arch_params_raw_5 = np.array()

arch_params_raw = np.median([raw_1,raw_2,raw_3,raw_4,raw_5],axis=0)

#print(arch_params_raw)

arch_params = (arch_params_raw == arch_params_raw.max(axis=1, keepdims=1)).astype(float)

#print(arch_params)

op = np.argmax(arch_params,axis=1)

print(op.tolist())

power_srnn_op = [4, 3, 4, 3, 4, 4, 3, 4, 4, 4, 3, 4, 4, 4, 4, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
power_cwspn_op = [2, 0, 3, 0, 3, 2, 0, 0, 5, 0, 0, 0, 0, 0]
power_cwspn_op = power_cwspn_op[0:-4]

#Operations Encoding

srnn_op_0 = 'none'
srnn_op_1 = 'tanh'
srnn_op_2 = 'relu'
srnn_op_3 = 'sigmoid'
srnn_op_4 = 'identity'

cwspn_op_0 = 'none'
cwspn_op_1 = 'identity'
cwspn_op_2 = 'conv_3x3'
cwspn_op_3 = 'conv_5x5'
cwspn_op_4 = 'dil_conv_3x3'
cwspn_op_5 = 'dil_conv_5x5'