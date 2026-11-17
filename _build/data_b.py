# -*- coding: utf-8 -*-
BOOK_B = [
 {
  "slug":"inorganic-chem","title":"简明无机化学：元素的性质地图","subtitle":"按周期表分区，把非金属、主族金属、过渡金属串成一张性质网",
  "book":{"title":"简明无机化学（第2版）","author":"宋天佑","source":["简明无机化学 第2版.pdf"]},
  "audience":"已读完入门篇、正在学大学的元素化学","goal":"掌握常见元素单质、氧化物、含氧酸、配合物的性质与反应",
  "chapters":[
   {"id":"ch01","title":"第 1 章：元素周期律与无机化学地图","file":"chapters/ch01-元素周期律与无机地图.md","difficulty":2,"source":"《简明无机化学》化学原理部分","prereq":[],"core":"无机化学不是背反应，而是用构型决定性质、性质决定用途这条线，把几百种物质串起来。","trap":"Al2O3 是两性氧化物，不是碱性氧化物。"},
   {"id":"ch02","title":"第 2 章：非金属元素","file":"chapters/ch02-非金属元素.md","difficulty":3,"source":"《简明无机化学》元素化学·非金属","prereq":["ch01"],"core":"非金属性越靠右上越强；同族向下，氢化物越不稳定、含氧酸越弱。","trap":"氯水不是 HCl 和 HClO 的简单混合物，是多组分平衡体系。"},
   {"id":"ch03","title":"第 3 章：主族金属","file":"chapters/ch03-主族金属.md","difficulty":2,"source":"《简明无机化学》元素化学·主族金属","prereq":["ch01"],"core":"主族金属越往下越活泼；铝是两性金属，既能与酸反应也能与强碱反应。","trap":"Na2O2 是过氧化物，不是碱性氧化物。"},
   {"id":"ch04","title":"第 4 章：过渡金属与配位化合物","file":"chapters/ch04-过渡金属与配位.md","difficulty":3,"source":"《简明无机化学》元素化学·过渡金属 + 配位化学基础","prereq":["ch01","ch03"],"core":"过渡金属的特点是多价态、有色、易形成配合物，这三条决定它们的化学行为。","trap":"Zn2+ 无色，不是所有过渡金属离子都有颜色。"}
  ],
  "concepts":[
   {"id":"c01","title":"配合物与配位键","file":"concepts/c01-配合物.md","chapters":["ch04"],"difficulty":"进阶","source":"《简明无机化学》配位化学基础","prereq":["ch01"]}
  ],
  "path":[
   {"step":"01","title":"先拿地图","chapterIds":["ch01"],"checkpoint":"能说出五个分区和四条周期性主线"},
   {"step":"02","title":"非金属","chapterIds":["ch02"],"checkpoint":"能写卤素、硫、氮、硅的关键反应"},
   {"step":"03","title":"主族金属","chapterIds":["ch03"],"checkpoint":"能写钠、镁、铝的反应并解释两性"},
   {"step":"04","title":"过渡金属与配合物","chapterIds":["ch04"],"checkpoint":"能写 Fe2+/Fe3+ 转化、Cu2+ 配合、命名配合物"}
  ],
  "glossary":[
   {"term":"两性氧化物","def":"既能与酸反应又能与碱反应生成盐和水的氧化物","chapterId":"ch01"},
   {"term":"惰性电子对效应","def":"同族向下 ns2 电子对越来越难参与成键的现象","chapterId":"ch03"},
   {"term":"配位键","def":"配体提供孤对电子、中心离子提供空轨道形成的共价键","chapterId":"ch04"},
   {"term":"配位数","def":"中心离子周围配位原子的数目","chapterId":"ch04"},
   {"term":"稳定常数","def":"配合物生成反应的平衡常数，越大越稳定","chapterId":"ch04"},
   {"term":"铝热反应","def":"铝与金属氧化物在高温下反应，放出大量热并还原出金属","chapterId":"ch03"}
  ],
  "quizzes":[
   {"id":"q01","chapterId":"ch01","type":"single","question":"下列元素属于 p 区的是？","options":["Na","Fe","S","Ag"],"answer":2,"explain":"S 的价电子构型 3s2 3p4，属 p 区。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q02","chapterId":"ch01","type":"single","question":"F、Cl、Br 非金属性由强到弱是？","options":["F>Cl>Br","Br>Cl>F","Cl>F>Br","F>Br>Cl"],"answer":0,"explain":"同主族从上到下非金属性减弱。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q03","chapterId":"ch02","type":"single","question":"下列氢化物最稳定的是？","options":["HF","HCl","HBr","HI"],"answer":0,"explain":"F 的非金属性最强，H—F 键最稳定。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q04","chapterId":"ch02","type":"single","question":"氯气与氢氧化钠反应生成？","options":["NaCl 和 NaClO","NaCl 和 NaClO3","NaClO 和 O2","NaCl 和 HClO4"],"answer":0,"explain":"Cl2+2NaOH→NaCl+NaClO+H2O。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q05","chapterId":"ch03","type":"single","question":"钠与水反应的现象不包括？","options":["浮在水面","熔成小球","沉入水底","四处游动"],"answer":2,"explain":"钠密度比水小，浮在水面而不是沉底。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q06","chapterId":"ch03","type":"single","question":"Al 与 NaOH 溶液反应生成？","options":["Al(OH)3 和 H2","NaAlO2 和 H2","Al2O3 和 H2O","AlCl3 和 H2"],"answer":1,"explain":"2Al+2NaOH+2H2O→2NaAlO2+3H2↑。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q07","chapterId":"ch04","type":"single","question":"检验 Fe3+ 常用的试剂是？","options":["NaOH","KSCN","BaCl2","AgNO3"],"answer":1,"explain":"Fe3+ 与 SCN- 生成血红色配合物。","relatedConceptId":"c01","optionMisconceptions":[]},
   {"id":"q08","chapterId":"ch04","type":"single","question":"Cu2+ 与过量氨水反应的现象是？","options":["生成白色沉淀","生成蓝色沉淀后溶解变深蓝","生成红褐色沉淀","无现象"],"answer":1,"explain":"先生成 Cu(OH)2 蓝色沉淀，继续加氨水生成深蓝色 [Cu(NH3)4]2+。","relatedConceptId":"c01","optionMisconceptions":[]}
  ]
 },
 {
  "slug":"organic-chem","title":"基础有机化学：从碳骨架到手性","subtitle":"按官能团组织，讲清烷、烯、芳、卤代与立体化学",
  "book":{"title":"基础有机化学（第4版）上册","author":"邢其毅、裴伟伟、徐瑞秋、裴坚","source":["基础有机化学 上册.pdf"]},
  "audience":"读完入门篇、准备学有机","goal":"掌握有机物的结构语言、常见官能团反应与立体化学基础",
  "chapters":[
   {"id":"ch01","title":"第 1 章：有机化学的结构语言","file":"chapters/ch01-有机结构语言.md","difficulty":2,"source":"《基础有机化学》上册·绪论","prereq":[],"core":"有机分子靠碳骨架加官能团两件事描述；同一分子式画出不同骨架，就是不同物质。","trap":"分子式相同不一定是同一种物质。"},
   {"id":"ch02","title":"第 2 章：烷烃与构象","file":"chapters/ch02-烷烃与构象.md","difficulty":2,"source":"《基础有机化学》上册·饱和烃","prereq":["ch01"],"core":"烷烃的 C—C 单键可以自由旋转，不同旋转角度形成不同构象；化学性质以自由基取代为主。","trap":"构象不同不断键，是同一物质。"},
   {"id":"ch03","title":"第 3 章：烯烃与亲电加成","file":"chapters/ch03-烯烃与亲电加成.md","difficulty":3,"source":"《基础有机化学》上册·烯烃","prereq":["ch02"],"core":"C=C 由一个 σ 键和一个 π 键组成，π 电子云暴露在外，容易被亲电试剂进攻发生加成。","trap":"过氧化物存在下 HBr 加成是反马氏，是特例。"},
   {"id":"ch04","title":"第 4 章：芳香烃、卤代烃与立体化学","file":"chapters/ch04-芳香烃卤代烃与立体化学.md","difficulty":3,"source":"《基础有机化学》上册·芳香烃、卤代烃、立体化学","prereq":["ch03"],"core":"苯环的 π 电子离域使体系特别稳定，倾向取代；手性来自四个不同基团连在同一个碳上。","trap":"R 不一定是右旋，S 不一定是左旋，必须实测。"}
  ],
  "concepts":[
   {"id":"c01","title":"手性与对映异构","file":"concepts/c01-手性.md","chapters":["ch04"],"difficulty":"高难","source":"《基础有机化学》上册·立体化学","prereq":["ch01","ch03"],"depth":"concepts/c01-手性-depth.md"}
  ],
  "path":[
   {"step":"01","title":"学会画结构和命名","chapterIds":["ch01"],"checkpoint":"能把分子式画成键线式并命名"},
   {"step":"02","title":"饱和烃","chapterIds":["ch02"],"checkpoint":"能解释构象与自由基取代"},
   {"step":"03","title":"不饱和烃","chapterIds":["ch03"],"checkpoint":"能用马氏规则预测产物"},
   {"step":"04","title":"芳香、卤代与手性","chapterIds":["ch04"],"checkpoint":"能写苯的亲电取代、判断手性碳"}
  ],
  "glossary":[
   {"term":"键线式","def":"省略碳和碳氢键、只画碳骨架与官能团的结构式","chapterId":"ch01"},
   {"term":"同分异构体","def":"分子式相同、结构不同的化合物","chapterId":"ch01"},
   {"term":"构象","def":"单键旋转形成的不同空间排列，不断键即可互变","chapterId":"ch02"},
   {"term":"马氏规则","def":"不对称烯烃与 HX 加成时 H 加在含氢较多的碳上","chapterId":"ch03"},
   {"term":"芳香性","def":"环状、平面、π 电子数为 4n+2 的体系具有的特殊稳定性","chapterId":"ch04"},
   {"term":"手性碳","def":"连有四个不同基团的碳原子","chapterId":"ch04"},
   {"term":"对映异构体","def":"互为镜像、不能重合的一对立体异构体","chapterId":"ch04"},
   {"term":"外消旋体","def":"等量对映异构体的混合物，旋光相互抵消","chapterId":"ch04"}
  ],
  "quizzes":[
   {"id":"q01","chapterId":"ch01","type":"single","question":"下列属于官能团的是？","options":["—CH3","—OH","—C2H5","苯环"],"answer":1,"explain":"羟基是官能团；甲基、乙基是取代基。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q02","chapterId":"ch01","type":"single","question":"C4H10 的同分异构体有几种？","options":["1","2","3","4"],"answer":1,"explain":"正丁烷和异丁烷两种。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q03","chapterId":"ch02","type":"single","question":"甲烷的空间构型是？","options":["平面正方形","正四面体","三角锥","直线形"],"answer":1,"explain":"sp3 杂化，四个键指向四面体顶点。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q04","chapterId":"ch02","type":"single","question":"乙烷最稳定的构象是？","options":["交叉式","重叠式","半重叠式","平面式"],"answer":0,"explain":"交叉式氢与氢错开，排斥最小。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q05","chapterId":"ch03","type":"single","question":"丙烯与 HBr 加成的主要产物是？","options":["1-溴丙烷","2-溴丙烷","1,2-二溴丙烷","丙醇"],"answer":1,"explain":"马氏规则，H 加在含氢多的碳上。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q06","chapterId":"ch03","type":"single","question":"下列能发生顺反异构的是？","options":["CH2=CH2","CH2=CHCH3","CH3CH=CHCH3","CH2=C(CH3)2"],"answer":2,"explain":"两个双键碳各连两个不同基团。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q07","chapterId":"ch04","type":"single","question":"苯的硝化反应条件是？","options":["浓硝酸、浓硫酸、加热","稀硝酸、常温","氯气、光照","氢氧化钠、加热"],"answer":0,"explain":"混酸硝化，浓硫酸作催化剂和脱水剂。","relatedConceptId":"","optionMisconceptions":[]},
   {"id":"q08","chapterId":"ch04","type":"single","question":"下列化合物中有手性碳的是？","options":["CH3Cl","CH2Cl2","CH3CHClCH3","CH3CHClCH2CH3"],"answer":3,"explain":"2 号碳连 H、Cl、CH3、C2H5 四个不同基团。","relatedConceptId":"c01","optionMisconceptions":[]}
  ]
 }
]
