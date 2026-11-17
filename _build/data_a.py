# -*- coding: utf-8 -*-
BOOK_A = [
 {
  "slug":"zero-basis-chem","title":"零基础入门：化学的第一套语言","subtitle":"给几乎没学过化学的人，从物质分类讲到有机初识",
  "book":{"title":"基础概念 + 高中化学基础知识大全","author":"自编讲义 / 一龙","source":["基础概念.pdf","五彩绳 高中化学基础知识大全.pdf"]},
  "audience":"文科零基础、化学几乎没学过","goal":"建立化学的语言与符号系统，能读懂方程式、会算物质的量、会写离子方程式",
  "chapters":[
   {"id":"ch01","title":"第 1 章：物质怎么分类","file":"chapters/ch01-物质分类.md","difficulty":1,"source":"《基础概念》第一节 + 高中化学基础知识大全","prereq":[],"core":"分类只看两件事：里面是不是只有一种东西，以及它由几种元素组成。","trap":"冰水混合物是纯净物，不是混合物。"},
   {"id":"ch02","title":"第 2 章：原子、分子、离子","file":"chapters/ch02-微观粒子.md","difficulty":1,"source":"《基础概念》第二节","prereq":["ch01"],"core":"化学反应只动最外层电子，原子核不变；带电与否看质子数和电子数是否相等。","trap":"NaCl 固体不导电，但里面有离子，只是不能自由移动。"},
   {"id":"ch03","title":"第 3 章：化学式与化合价","file":"chapters/ch03-化学式与化合价.md","difficulty":1,"source":"《基础概念》第三节","prereq":["ch02"],"core":"化学式是物质的配方标签：元素种类不能错，正负化合价代数和必须为零。","trap":"配平不能改化学式右下角的下标。"},
   {"id":"ch04","title":"第 4 章：化学方程式与配平","file":"chapters/ch04-化学方程式与配平.md","difficulty":2,"source":"《基础概念》第三节 + 高中化学基础知识大全","prereq":["ch03"],"core":"方程式是化学反应的账单：反应前后每种元素的原子个数必须一模一样。","trap":"有化合价变化时，先电子守恒，再数原子。"},
   {"id":"ch05","title":"第 5 章：物质的量","file":"chapters/ch05-物质的量.md","difficulty":2,"source":"《基础概念》第二节 核心计算体系","prereq":["ch04"],"core":"摩尔把数不清的微粒换成可以称量的份数，1 mol 就是 6.02×10²³ 个。","trap":"22.4 L/mol 只对气体、只在标准状况成立。"},
   {"id":"ch06","title":"第 6 章：电解质与离子反应","file":"chapters/ch06-离子反应.md","difficulty":2,"source":"《基础概念》第四节","prereq":["ch04","ch05"],"core":"离子方程式只留下真正参加反应的离子，但难溶物、气体、水、弱电解质不能拆。","trap":"能导电的铜不是电解质，电解质必须是化合物。"},
   {"id":"ch07","title":"第 7 章：氧化还原反应","file":"chapters/ch07-氧化还原.md","difficulty":3,"source":"《基础概念》第三节 + 高中化学基础知识大全","prereq":["ch04","ch06"],"core":"升失氧、降得还：化合价升高、失电子、被氧化；降低、得电子、被还原。","trap":"氧化剂被还原，不是被氧化。"},
   {"id":"ch08","title":"第 8 章：元素周期表与化学键","file":"chapters/ch08-元素周期表与化学键.md","difficulty":2,"source":"《基础概念》第五节 + 高中化学基础知识大全","prereq":["ch02","ch07"],"core":"周期表按电子层数分行、按最外层电子数分列；原子靠凑成稳定电子结构成键。","trap":"NaOH 有共价键，但它是离子化合物。"},
   {"id":"ch09","title":"第 9 章：反应速率与化学平衡","file":"chapters/ch09-速率与平衡.md","difficulty":2,"source":"《基础概念》第六节","prereq":["ch07"],"core":"速率管多快，平衡管最终生成多少；催化剂只改速率，不改平衡。","trap":"平衡时反应没有停止，v正 = v逆 ≠ 0。"},
   {"id":"ch10","title":"第 10 章：有机化学初识","file":"chapters/ch10-有机化学初识.md","difficulty":2,"source":"《基础概念》第七节","prereq":["ch08"],"core":"有机化学研究含碳化合物，碳能形成四个共价键，官能团决定性质。","trap":"CO2、碳酸盐是无机物，不是有机物。"}
  ],
  "concepts":[
   {"id":"c01","title":"物质的量","file":"concepts/c01-物质的量.md","chapters":["ch05"],"difficulty":"进阶","source":"《基础概念》核心计算体系","prereq":["ch03"]},
   {"id":"c02","title":"离子方程式","file":"concepts/c02-离子方程式.md","chapters":["ch06"],"difficulty":"进阶","source":"《基础概念》第四节","prereq":["ch04","ch05"]},
   {"id":"c03","title":"氧化还原反应","file":"concepts/c03-氧化还原.md","chapters":["ch07"],"difficulty":"高难","source":"《基础概念》第三节","prereq":["ch04","c02"]}
  ],
  "path":[
   {"step":"01","title":"先学会给物质分类","chapterIds":["ch01"],"checkpoint":"能独立判断 6 种常见物质的类别"},
   {"step":"02","title":"看懂微观粒子和符号","chapterIds":["ch02","ch03"],"checkpoint":"能写常见化学式并检查化合价"},
   {"step":"03","title":"会写会配平方程式","chapterIds":["ch04"],"checkpoint":"独立配平 3 个方程式"},
   {"step":"04","title":"掌握化学计算的语言","chapterIds":["ch05"],"checkpoint":"四条换算各做对 2 题"},
   {"step":"05","title":"进入溶液与离子","chapterIds":["ch06"],"checkpoint":"能写出 3 个离子方程式"},
   {"step":"06","title":"理解电子转移","chapterIds":["ch07"],"checkpoint":"能判断氧化剂还原剂并配平"},
   {"step":"07","title":"结构与周期律","chapterIds":["ch08"],"checkpoint":"能判断键型和金属性顺序"},
   {"step":"08","title":"反应快慢与限度","chapterIds":["ch09"],"checkpoint":"能判断平衡移动方向"},
   {"step":"09","title":"有机入门","chapterIds":["ch10"],"checkpoint":"能认出四种官能团"}
  ],
  "glossary":[
   {"term":"纯净物","def":"只由一种物质组成、有固定化学式的体系","chapterId":"ch01"},
   {"term":"电解质","def":"在水溶液或熔融状态下能导电的化合物","chapterId":"ch06"},
   {"term":"离子方程式","def":"删去旁观离子后只保留实际参加反应离子的方程式","chapterId":"ch06"},
   {"term":"氧化剂","def":"得电子、化合价降低、被还原的物质","chapterId":"ch07"},
   {"term":"还原剂","def":"失电子、化合价升高、被氧化的物质","chapterId":"ch07"},
   {"term":"物质的量","def":"表示微粒集合份数的物理量，单位 mol","chapterId":"ch05"},
   {"term":"摩尔质量","def":"1 mol 物质的质量，单位 g/mol","chapterId":"ch05"},
   {"term":"官能团","def":"决定有机物化学性质的原子或原子团","chapterId":"ch10"}
  ],
  "quizzes":[
   {"id":"q01","chapterId":"ch01","type":"single","question":"下列属于纯净物的是？","options":["洁净的空气","冰水混合物","生理盐水","大理石"],"answer":1,"explain":"冰和水都是 H2O，只有一种物质；其余都含多种物质。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q02","chapterId":"ch01","type":"single","question":"下列物质中属于氧化物的是？","options":["O2","KClO3","Fe3O4","H2SO4"],"answer":2,"explain":"Fe3O4 只含 Fe、O 两种元素；A 是单质，B、D 含三种元素。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q03","chapterId":"ch02","type":"single","question":"17O 的质子数、中子数、电子数分别是？","options":["8、9、8","9、8、9","8、9、9","17、8、17"],"answer":0,"explain":"O 的原子序数 8，质子数 8；中子数 17-8=9；中性原子电子数=质子数=8。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q04","chapterId":"ch02","type":"blank","question":"Mg2+ 的质子数为 12，它的电子数是多少？","options":[],"answer":"10","explain":"带 2 个单位正电，电子比质子少 2 个：12-2=10。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q05","chapterId":"ch03","type":"single","question":"氧化铁的化学式是？","options":["FeO","Fe2O3","Fe3O4","Fe(OH)3"],"answer":1,"explain":"铁为 +3，氧为 -2，交叉得 Fe2O3。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q06","chapterId":"ch03","type":"blank","question":"KMnO4 中 Mn 的化合价是多少？（写带符号的数字，如 +7）","options":[],"answer":"+7","explain":"K 为 +1，O 为 -2，设 Mn 为 x：1+x+4×(-2)=0，x=+7。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q07","chapterId":"ch04","type":"single","question":"配平 Al + O2 → Al2O3，正确系数是？","options":["2、1、1","4、3、2","2、3、2","4、2、2"],"answer":1,"explain":"2 个 Al2O3 含 4 个 Al、6 个 O，需要 3 个 O2。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q08","chapterId":"ch04","type":"single","question":"配平时允许改动的是？","options":["化学式右下角的下标","元素符号","前面的系数","反应条件"],"answer":2,"explain":"只能改系数，改下标就改变了物质本身。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q09","chapterId":"ch05","type":"single","question":"18 g 水的物质的量是多少？（M=18 g/mol）","options":["0.5 mol","1 mol","2 mol","18 mol"],"answer":1,"explain":"n=m/M=18/18=1 mol。","relatedConceptId":"c01","optionMisconceptions":[]},
   {"id":"q10","chapterId":"ch05","type":"blank","question":"标准状况下 11.2 L CO2 的质量是多少克？（M=44 g/mol，填数字）","options":[],"answer":"22","explain":"n=11.2/22.4=0.5 mol；m=0.5×44=22 g。","relatedConceptId":"c01","optionMisconceptions":[]},
   {"id":"q11","chapterId":"ch06","type":"single","question":"下列物质属于强电解质的是？","options":["CH3COOH","NH3·H2O","NaCl","蔗糖"],"answer":2,"explain":"NaCl 是盐，完全电离；A、B 是弱电解质，D 是非电解质。","relatedConceptId":"c02","optionMisconceptions":[]},
   {"id":"q12","chapterId":"ch06","type":"single","question":"CaCO3 与盐酸反应的离子方程式中，CaCO3 应怎么写？","options":["拆成 Ca2+ 和 CO3^2-","写化学式不拆","写成 CaO 和 CO2","删掉不写"],"answer":1,"explain":"CaCO3 难溶，不能拆，必须写化学式。","relatedConceptId":"c02","optionMisconceptions":[]},
   {"id":"q13","chapterId":"ch07","type":"single","question":"下列反应属于氧化还原反应的是？","options":["NaOH+HCl→NaCl+H2O","CaCO3→CaO+CO2","Zn+CuSO4→ZnSO4+Cu","CO2+Ca(OH)2→CaCO3+H2O"],"answer":2,"explain":"Zn 0→+2，Cu +2→0，有化合价变化。","relatedConceptId":"c03","optionMisconceptions":[]},
   {"id":"q14","chapterId":"ch07","type":"single","question":"Fe + 2HCl → FeCl2 + H2 中，氧化剂是？","options":["Fe","HCl","FeCl2","H2"],"answer":1,"explain":"HCl 中的 H 从 +1 降到 0，得电子，是氧化剂。","relatedConceptId":"c03","optionMisconceptions":[]},
   {"id":"q15","chapterId":"ch08","type":"single","question":"下列化合物中只含共价键的是？","options":["NaCl","NaOH","CO2","K2O"],"answer":2,"explain":"CO2 由 C、O 非金属原子通过共价键结合。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q16","chapterId":"ch08","type":"single","question":"Na、Mg、Al 金属性由强到弱的顺序是？","options":["Al>Mg>Na","Na>Mg>Al","Mg>Na>Al","Na>Al>Mg"],"answer":1,"explain":"同周期从左到右金属性减弱。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q17","chapterId":"ch09","type":"single","question":"升高温度，反应速率通常？","options":["一定加快","一定减慢","不变","无法判断"],"answer":0,"explain":"升温使活化分子比例增加，正逆反应速率都加快。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q18","chapterId":"ch09","type":"single","question":"2SO2+O2⇌2SO3（放热）增大压强，平衡向？","options":["正反应方向","逆反应方向","不移动","先正后逆"],"answer":0,"explain":"右边气体分子数少，加压向分子数少的方向移动。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q19","chapterId":"ch10","type":"single","question":"下列属于有机物的是？","options":["CO2","CH4","Na2CO3","H2CO3"],"answer":1,"explain":"CH4 是含碳的烃；其余归为无机物。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q20","chapterId":"ch10","type":"single","question":"乙烯与溴水反应属于？","options":["取代反应","加成反应","酯化反应","复分解反应"],"answer":1,"explain":"碳碳双键打开，溴原子加在两个碳上。","relatedConceptId":"","optionMisconceptions":[]}
  ]
 },
 {
  "slug":"general-chem","title":"普通化学原理：大学化学的主干","subtitle":"以华彤文《普通化学原理》为主线，讲透热力学、平衡、电化学与结构",
  "book":{"title":"普通化学原理（第4版）","author":"华彤文、王颖霞、卞江、陈景祖","source":["普通化学原理 第4版.pdf"]},
  "audience":"零基础起步，目标系统掌握","goal":"掌握大学普通化学的十二条主线：气体、热力学、平衡、电化学、速率、结构",
  "chapters":[
   {"id":"ch01","title":"第 1 章：气体","file":"chapters/ch01-气体.md","difficulty":2,"source":"《普通化学原理》第2章","prereq":[],"core":"理想气体把分子当成没有体积、彼此不吸引的质点，pV=nRT 是这种假设下的状态方程。","trap":"温度必须用 K，不能用摄氏度。"},
   {"id":"ch02","title":"第 2 章：热力学第一定律与焓","file":"chapters/ch02-热力学第一定律.md","difficulty":3,"source":"《普通化学原理》第5章","prereq":["ch01"],"core":"能量守恒：体系内能的改变，等于它吸收的热加上外界对它做的功。","trap":"焓不是热，只有恒压且只做体积功时 ΔH 才等于 Qp。"},
   {"id":"ch03","title":"第 3 章：热化学与盖斯定律","file":"chapters/ch03-热化学.md","difficulty":2,"source":"《普通化学原理》第5章","prereq":["ch02"],"core":"反应热只由始末态决定，可以把已知反应像代数式一样相加。","trap":"热化学方程式必须标物质状态。"},
   {"id":"ch04","title":"第 4 章：熵与吉布斯自由能","file":"chapters/ch04-熵与吉布斯自由能.md","difficulty":3,"source":"《普通化学原理》第5章","prereq":["ch02","ch03"],"core":"自发性由放热和熵增共同决定，ΔG = ΔH - TΔS 把两者合成一个判据。","trap":"ΔG<0 只说明方向，不说明速率。"},
   {"id":"ch05","title":"第 5 章：化学平衡","file":"chapters/ch05-化学平衡.md","difficulty":3,"source":"《普通化学原理》第6章","prereq":["ch03","ch04"],"core":"平衡常数 K 只随温度变化；Q 与 K 的比较告诉你反应往哪边走。","trap":"催化剂不改变 K。"},
   {"id":"ch06","title":"第 6 章：酸碱电离平衡与缓冲溶液","file":"chapters/ch06-酸碱平衡.md","difficulty":3,"source":"《普通化学原理》第8章","prereq":["ch05"],"core":"酸碱反应是质子转移；弱酸的 Ka 与共轭碱的 Kb 通过 Kw 联系。","trap":"pH=7 只在 25℃ 是中性。"},
   {"id":"ch07","title":"第 7 章：沉淀溶解平衡","file":"chapters/ch07-沉淀溶解平衡.md","difficulty":2,"source":"《普通化学原理》第9章","prereq":["ch05","ch06"],"core":"难溶电解质并非完全不溶，Ksp 是溶解与沉淀平衡的定量表达。","trap":"Ksp 小的先沉淀，不是大的先沉淀。"},
   {"id":"ch08","title":"第 8 章：氧化还原与电化学","file":"chapters/ch08-电化学.md","difficulty":3,"source":"《普通化学原理》第10章","prereq":["ch04","ch05"],"core":"氧化还原是电子转移；原电池把这种转移拆成两半，让电子走外电路做功。","trap":"原电池负极是阳极（氧化），别和电解池混。"},
   {"id":"ch09","title":"第 9 章：化学反应速率","file":"chapters/ch09-反应速率.md","difficulty":2,"source":"《普通化学原理》第7章","prereq":["ch05"],"core":"速率由活化能和碰撞频率决定；催化剂降低能垒，不改平衡。","trap":"反应级数不一定等于方程式系数。"},
   {"id":"ch10","title":"第 10 章：原子结构","file":"chapters/ch10-原子结构.md","difficulty":3,"source":"《普通化学原理》第11章","prereq":["ch04"],"core":"电子没有确定轨道，只有概率分布；量子数描述这种分布的形状、方向和能量。","trap":"Cr、Cu 的排布是半充满/全充满特例。"},
   {"id":"ch11","title":"第 11 章：化学键与分子结构","file":"chapters/ch11-分子结构.md","difficulty":3,"source":"《普通化学原理》第12章","prereq":["ch10"],"core":"分子形状由中心原子周围电子对互相排斥决定；杂化轨道是为成键重组的轨道。","trap":"有极性键的分子不一定有极性。"},
   {"id":"ch12","title":"第 12 章：晶体结构与配位化合物","file":"chapters/ch12-晶体与配位.md","difficulty":3,"source":"《普通化学原理》第13、14章","prereq":["ch11"],"core":"晶体性质由构成粒子和粒子间作用力决定；配合物是中心离子与配体通过配位键结合的整体。","trap":"配位数不一定等于配体个数。"}
  ],
  "concepts":[
   {"id":"c01","title":"化学平衡常数","file":"concepts/c01-化学平衡常数.md","chapters":["ch05"],"difficulty":"进阶","source":"《普通化学原理》第6章","prereq":["ch04"]},
   {"id":"c02","title":"吉布斯自由能","file":"concepts/c02-吉布斯自由能.md","chapters":["ch04"],"difficulty":"高难","source":"《普通化学原理》第5章","prereq":["ch02","ch03"],"depth":"concepts/c02-吉布斯自由能-depth.md"},
   {"id":"c03","title":"电极电势与 Nernst 方程","file":"concepts/c03-电极电势.md","chapters":["ch08"],"difficulty":"高难","source":"《普通化学原理》第10章","prereq":["c02","ch05"],"depth":"concepts/c03-电极电势-depth.md"},
   {"id":"c04","title":"原子轨道与量子数","file":"concepts/c04-原子轨道.md","chapters":["ch10"],"difficulty":"高难","source":"《普通化学原理》第11章","prereq":[],"depth":""},
   {"id":"c05","title":"杂化轨道","file":"concepts/c05-杂化轨道.md","chapters":["ch11"],"difficulty":"高难","source":"《普通化学原理》第12章","prereq":["c04"],"depth":"concepts/c05-杂化轨道-depth.md"}
  ],
  "path":[
   {"step":"01","title":"气体与状态方程","chapterIds":["ch01"],"checkpoint":"能算 p、V、n、T 与分压"},
   {"step":"02","title":"能量与焓","chapterIds":["ch02","ch03"],"checkpoint":"能写热化学方程式并用盖斯定律算 ΔH"},
   {"step":"03","title":"自发方向","chapterIds":["ch04"],"checkpoint":"能判断四种 ΔH/ΔS 组合并算转折温度"},
   {"step":"04","title":"平衡","chapterIds":["ch05"],"checkpoint":"能写 K、算 Q、用 ICE 表算浓度"},
   {"step":"05","title":"水溶液平衡","chapterIds":["ch06","ch07"],"checkpoint":"能算 pH、缓冲、Ksp 与沉淀顺序"},
   {"step":"06","title":"电化学","chapterIds":["ch08"],"checkpoint":"能写电极反应并用 Nernst 算电动势"},
   {"step":"07","title":"速率","chapterIds":["ch09"],"checkpoint":"能定级数、算活化能"},
   {"step":"08","title":"结构","chapterIds":["ch10","ch11","ch12"],"checkpoint":"能写排布、判构型与杂化、认晶体与配合物"}
  ],
  "glossary":[
   {"term":"状态函数","def":"只由体系当前状态决定、与路径无关的物理量","chapterId":"ch02"},
   {"term":"焓","def":"H = U + pV，恒压热等于 ΔH","chapterId":"ch02"},
   {"term":"熵","def":"体系混乱度的量度，单位 J/(mol·K)","chapterId":"ch04"},
   {"term":"吉布斯自由能","def":"G = H - TS，恒温恒压下 ΔG<0 自发","chapterId":"ch04"},
   {"term":"平衡常数","def":"平衡时生成物浓度幂之积与反应物浓度幂之积的比值","chapterId":"ch05"},
   {"term":"缓冲溶液","def":"能抵抗少量酸碱、pH 基本不变的溶液","chapterId":"ch06"},
   {"term":"溶度积","def":"难溶电解质饱和溶液中离子浓度幂之积","chapterId":"ch07"},
   {"term":"标准电极电势","def":"电极相对标准氢电极的电势","chapterId":"ch08"},
   {"term":"活化能","def":"反应物分子变成活化分子所需的最小能量","chapterId":"ch09"},
   {"term":"杂化","def":"原子轨道重新组合成能量相同、方向更合理的新轨道","chapterId":"ch11"}
  ],
  "quizzes":[
   {"id":"q01","chapterId":"ch01","type":"single","question":"25℃、100 kPa 下 2 mol N2 的体积约为？","options":["24.8 L","49.6 L","22.4 L","98.2 L"],"answer":1,"explain":"V=nRT/p=2×8.314×298.15/100000≈0.0496 m3=49.6 L。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q02","chapterId":"ch01","type":"single","question":"容器中 0.2 mol O2 与 0.8 mol N2，总压 100 kPa，O2 分压为？","options":["20 kPa","80 kPa","100 kPa","8 kPa"],"answer":0,"explain":"摩尔分数 0.2，分压=0.2×100=20 kPa。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q03","chapterId":"ch02","type":"single","question":"下列属于状态函数的是？","options":["Q","W","H","反应热"],"answer":2,"explain":"焓只由状态决定，Q、W 是过程量。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q04","chapterId":"ch02","type":"single","question":"恒压下某反应放热 50 kJ，ΔH 为？","options":["+50 kJ","-50 kJ","0","无法判断"],"answer":1,"explain":"放热 Qp<0，恒压热等于 ΔH。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q05","chapterId":"ch03","type":"single","question":"热化学方程式中 ΔH=+58 kJ/mol 表示？","options":["放热","吸热","不吸不放","无法判断"],"answer":1,"explain":"ΔH 为正表示体系吸热。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q06","chapterId":"ch03","type":"single","question":"N2+3H2→2NH3，ΔH=-92 kJ/mol；写成 ½N2+1.5H2→NH3 时 ΔH 为？","options":["-92 kJ/mol","-46 kJ/mol","+46 kJ/mol","-184 kJ/mol"],"answer":1,"explain":"系数减半，ΔH 也减半。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q07","chapterId":"ch04","type":"single","question":"下列过程熵增的是？","options":["水结冰","气体液化","CaCO3 分解产生 CO2","溶液结晶"],"answer":2,"explain":"固体分解出气体，混乱度增大。","relatedConceptId":"c02","optionMisconceptions":[]},
   {"id":"q08","chapterId":"ch04","type":"single","question":"ΔH=-50 kJ/mol、ΔS=-100 J/(mol·K)，298 K 时反应？","options":["自发","不自发","处于平衡","无法判断"],"answer":0,"explain":"ΔG=-50-298×(-0.1)=-20.2 kJ/mol<0，自发。单位要先换成 kJ。","relatedConceptId":"c02","optionMisconceptions":[]},
   {"id":"q09","chapterId":"ch05","type":"single","question":"C(s)+CO2(g)⇌2CO(g) 的 Kc 表达式是？","options":["[CO]2/[CO2]","[CO]2/([C][CO2])","[CO2]/[CO]2","[C][CO2]/[CO]2"],"answer":0,"explain":"纯固体 C 不写入平衡常数表达式。","relatedConceptId":"c01","optionMisconceptions":[]},
   {"id":"q10","chapterId":"ch05","type":"single","question":"某温度 K=10，当前 Q=5，反应向？","options":["正方向","逆方向","不移动","先正后逆"],"answer":0,"explain":"Q<K，生成物不足，向正方向进行。","relatedConceptId":"c01","optionMisconceptions":[]},
   {"id":"q11","chapterId":"ch06","type":"single","question":"0.01 mol/L HCl 的 pH 是？","options":["1","2","7","12"],"answer":1,"explain":"强酸完全电离，[H+]=0.01，pH=2。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q12","chapterId":"ch06","type":"single","question":"缓冲溶液 pH 的计算式是？","options":["pH=pKa+lg([碱]/[酸])","pH=pKa-lg([碱]/[酸])","pH=pKw-pKa","pH=-lgKa"],"answer":0,"explain":"Henderson-Hasselbalch 方程：pH=pKa+lg([A-]/[HA])。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q13","chapterId":"ch07","type":"single","question":"BaSO4 的 Ksp 表达式是？","options":["[Ba2+][SO4^2-]","[Ba2+]+[SO4^2-]","[BaSO4]/([Ba2+][SO4^2-])","[Ba2+][SO4^2-]/[BaSO4]"],"answer":0,"explain":"固体不写入 Ksp 表达式。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q14","chapterId":"ch07","type":"single","question":"AgCl 在 0.10 mol/L NaCl 中的溶解度比纯水中？","options":["更大","更小","相同","无法比较"],"answer":1,"explain":"同离子效应使平衡向沉淀方向移动，溶解度降低。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q15","chapterId":"ch08","type":"single","question":"原电池中电子从？","options":["正极流向负极","负极流向正极","溶液流向电极","盐桥流向电极"],"answer":1,"explain":"负极失电子，电子经外电路流向正极。","relatedConceptId":"c03","optionMisconceptions":[]},
   {"id":"q16","chapterId":"ch08","type":"single","question":"E°(Ag+/Ag)=+0.80 V，E°(Cu2+/Cu)=+0.34 V，Cu+2Ag+→Cu2++2Ag 的电动势是？","options":["1.14 V","0.46 V","-0.46 V","0.23 V"],"answer":1,"explain":"E=0.80-0.34=0.46 V。","relatedConceptId":"c03","optionMisconceptions":[]},
   {"id":"q17","chapterId":"ch09","type":"single","question":"某反应浓度加倍，速率变为 4 倍，反应级数是？","options":["0","1","2","3"],"answer":2,"explain":"v∝[A]^2，浓度 2 倍则速率 4 倍。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q18","chapterId":"ch09","type":"single","question":"催化剂对平衡的影响是？","options":["向正方向移动","向逆方向移动","不移动","改变 K"],"answer":2,"explain":"催化剂同等加快正逆反应，不改变平衡位置和 K。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q19","chapterId":"ch10","type":"single","question":"n=3 时 l 可以取？","options":["0、1、2","1、2、3","0、1、2、3","只有 3"],"answer":0,"explain":"l 取 0 到 n-1，即 0、1、2。","relatedConceptId":"c04","optionMisconceptions":[]},
   {"id":"q20","chapterId":"ch10","type":"single","question":"1s2 2s2 2p6 3s2 3p5 是几号元素？","options":["15","16","17","18"],"answer":2,"explain":"电子总数 2+2+6+2+5=17，是氯。","relatedConceptId":"c04","optionMisconceptions":[]},
   {"id":"q21","chapterId":"ch11","type":"single","question":"CH4 的中心原子杂化类型是？","options":["sp","sp2","sp3","未杂化"],"answer":2,"explain":"4 个 σ 键、无孤对，4 对电子，sp3。","relatedConceptId":"c05","optionMisconceptions":[]},
   {"id":"q22","chapterId":"ch11","type":"single","question":"NH3 的空间构型是？","options":["平面三角形","三角锥","正四面体","直线形"],"answer":1,"explain":"4 对电子中有 1 对孤对，三角锥。","relatedConceptId":"c05","optionMisconceptions":[]},
   {"id":"q23","chapterId":"ch12","type":"single","question":"下列晶体中熔点最高的是？","options":["NaCl","干冰","金刚石","冰"],"answer":2,"explain":"金刚石是共价晶体，整个晶体由共价键连接。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q24","chapterId":"ch12","type":"single","question":"[Cu(NH3)4]2+ 的中心离子和配位数是？","options":["Cu2+、4","Cu2+、6","Cu+、4","NH3、4"],"answer":0,"explain":"中心离子 Cu2+，4 个 NH3 配体，配位数 4。","relatedConceptId":"","optionMisconceptions":[]}
  ]
 }
]
