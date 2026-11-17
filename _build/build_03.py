#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成《无机及分析化学》manifest 与记忆系统文件。"""
import json, os, re, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BOOK = os.path.join(ROOT, "03-无机及分析化学")
CH = os.path.join(BOOK, "chapters")

CHAPTERS = [
    ("ch00", "第 0 章：化学基础常识（零基础入口）", "chapters/ch00-化学基础常识.md", 1,
     "《无机及分析化学》绪论 + 自编基础讲义", []),
    ("ch01", "第 1 章：物质结构", "chapters/ch01-物质结构.md", 2,
     "《无机及分析化学》第 1 章；《学习指导》第 4 章", ["ch00"]),
    ("ch02", "第 2 章：化学反应速率与化学平衡", "chapters/ch02-速率与平衡.md", 3,
     "《无机及分析化学》第 2 章；《学习指导》第 2、3 章", ["ch01"]),
    ("ch03", "第 3 章：重要元素及其化合物", "chapters/ch03-元素化学.md", 3,
     "《无机及分析化学》第 3 章；《学习指导》第 5 章", ["ch01"]),
    ("ch04", "第 4 章：定量分析基础", "chapters/ch04-定量分析基础.md", 2,
     "《无机及分析化学》第 4 章；《学习指导》第 9 章", ["ch00"]),
    ("ch05", "第 5 章：滴定分析基础", "chapters/ch05-滴定分析基础.md", 2,
     "《无机及分析化学》第 4 章；《学习指导》第 10 章", ["ch04"]),
    ("ch06", "第 6 章：酸碱平衡与酸碱滴定", "chapters/ch06-酸碱滴定.md", 3,
     "《无机及分析化学》第 5 章；《学习指导》第 6 章", ["ch05", "ch02"]),
    ("ch07", "第 7 章：配位化合物与配位滴定", "chapters/ch07-配位滴定.md", 3,
     "《无机及分析化学》第 6 章；《学习指导》第 7 章", ["ch05", "ch01"]),
    ("ch08", "第 8 章：氧化还原与电极电势", "chapters/ch08-电极电势.md", 3,
     "《无机及分析化学》第 7 章；《学习指导》第 8 章", ["ch01", "ch03"]),
    ("ch09", "第 9 章：氧化还原滴定法", "chapters/ch09-氧化还原滴定.md", 3,
     "《无机及分析化学》第 7 章；《学习指导》第 10 章", ["ch08", "ch05"]),
    ("ch10", "第 10 章：沉淀溶解平衡、沉淀滴定与重量分析", "chapters/ch10-沉淀与重量分析.md", 3,
     "《无机及分析化学》第 8 章；《学习指导》第 6、11 章", ["ch06", "ch05"]),
    ("ch11", "第 11 章：紫外-可见分光光度法", "chapters/ch11-分光光度法.md", 2,
     "《学习指导》第 12 章；《无机及分析化学》第 9 章", ["ch04"]),
    ("ch12", "第 12 章：电位分析法与分离方法", "chapters/ch12-电位分析法与分离方法.md", 3,
     "《学习指导》第 13、14 章；《无机及分析化学》第 9 章", ["ch08", "ch10"]),
]

CONCEPTS = [
    dict(id="c01", title="物质的量", file="concepts/c01-mole.md",
         chapterIds=["ch00", "ch04", "ch05"], difficulty="进阶",
         prerequisites=[], depthFragment="concepts/c01-depth.md",
         source="第 0 章 + 第 5 章"),
    dict(id="c02", title="化学平衡与平衡常数", file="concepts/c02-equilibrium.md",
         chapterIds=["ch02"], difficulty="进阶", prerequisites=["c01"],
         source="第 2 章"),
    dict(id="c03", title="酸碱质子理论与 pH", file="concepts/c03-acid-base.md",
         chapterIds=["ch06"], difficulty="进阶", prerequisites=["c02"],
         depthFragment="concepts/c03-depth.md", source="第 6 章"),
    dict(id="c04", title="条件稳定常数", file="concepts/c04-conditional-k.md",
         chapterIds=["ch07"], difficulty="高难", prerequisites=["c03"],
         depthFragment="concepts/c04-depth.md", source="第 7 章"),
    dict(id="c05", title="电极电势与 Nernst 方程", file="concepts/c05-electrode.md",
         chapterIds=["ch08"], difficulty="高难", prerequisites=["c01"],
         depthFragment="concepts/c05-depth.md", source="第 8 章"),
    dict(id="c06", title="朗伯-比尔定律", file="concepts/c06-beer.md",
         chapterIds=["ch11"], difficulty="进阶", prerequisites=["c01"],
         source="第 11 章"),
]

GLOSSARY = [
    ("纯净物", "只由一种物质组成、有固定组成的体系", "ch00"),
    ("混合物", "由两种或多种物质组成、各组分保持自身性质的体系", "ch00"),
    ("单质", "由同种元素组成的纯净物", "ch00"),
    ("化合物", "由两种或多种元素组成的纯净物", "ch00"),
    ("化合价", "元素在化合物中的氧化数，化合物中各元素代数和为零", "ch00"),
    ("离子方程式", "把可溶性强电解质拆成离子、删去不参加反应的离子后的方程式", "ch00"),
    ("物质的量", "表示粒子集合体多少的物理量，单位 mol", "ch00"),
    ("摩尔", "物质的量的单位，1 mol 含 6.022×10²³ 个粒子", "ch00"),
    ("摩尔质量", "1 mol 物质的质量，单位 g/mol，数值等于相对分子质量", "ch00"),
    ("气体摩尔体积", "标准状况下 1 mol 气体约占 22.4 L", "ch00"),
    ("物质的量浓度", "单位体积溶液中所含溶质的物质的量，c=n/V", "ch00"),
    ("稀释定律", "稀释前后溶质物质的量不变，c1V1=c2V2", "ch00"),
    ("原子序数", "原子核内质子数，决定元素种类", "ch01"),
    ("同位素", "质子数相同、中子数不同的原子", "ch01"),
    ("量子数", "描述核外电子运动状态的四个整数：n、l、m、ms", "ch01"),
    ("电子排布", "电子按能量最低、泡利不相容、洪特规则填入原子轨道", "ch01"),
    ("电离能", "气态基态原子失去一个电子所需的最小能量", "ch01"),
    ("电负性", "原子在化合物中吸引电子的能力", "ch01"),
    ("离子键", "阴、阳离子间通过静电引力形成的化学键", "ch01"),
    ("共价键", "原子间通过共用电子对形成的化学键", "ch01"),
    ("杂化轨道", "原子轨道重新组合成能量相同、方向不同的新轨道", "ch01"),
    ("氢键", "与电负性强的原子相连的 H 与另一电负性原子间的弱作用", "ch01"),
    ("晶格能", "气态离子形成 1 mol 离子晶体所释放的能量", "ch01"),
    ("反应速率", "单位时间内反应物浓度或生成物浓度的变化", "ch02"),
    ("速率常数", "速率方程中的比例系数 k，与浓度无关、随温度变", "ch02"),
    ("反应级数", "速率方程中各浓度项的指数之和", "ch02"),
    ("活化能", "反应物分子变为活化分子所需的最低能量", "ch02"),
    ("催化剂", "改变反应速率、自身质量和性质在反应前后不变的物质", "ch02"),
    ("化学平衡", "正逆反应速率相等、各组分浓度不再改变的状态", "ch02"),
    ("平衡常数", "平衡时生成物浓度系数次方乘积与反应物之比", "ch02"),
    ("反应商", "任意时刻按平衡常数形式计算的浓度比值 Q", "ch02"),
    ("勒夏特列原理", "改变条件时平衡向减弱这种改变的方向移动", "ch02"),
    ("转化率", "已转化的反应物占起始反应物的百分比", "ch02"),
    ("溶度积", "难溶电解质饱和溶液中离子浓度系数次方的乘积 Ksp", "ch10"),
    ("同离子效应", "加入含相同离子的电解质使难溶物溶解度降低", "ch10"),
    ("盐效应", "加入不含相同离子的强电解质使溶解度略增", "ch10"),
    ("分步沉淀", "多种离子共存时，先达到 Ksp 的先沉淀", "ch10"),
    ("沉淀转化", "Ksp 大的沉淀转化为 Ksp 小的沉淀", "ch10"),
    ("配位化合物", "由中心离子或原子与配体形成的复杂化合物", "ch07"),
    ("配体", "提供孤对电子与中心离子配位的分子或离子", "ch07"),
    ("配位数", "直接与中心离子配位的配位原子数", "ch07"),
    ("稳定常数", "配位反应平衡常数 Kf，越大配合物越稳定", "ch07"),
    ("酸效应系数", "EDTA 总浓度与游离 Y4- 浓度之比 αY(H)", "ch07"),
    ("条件稳定常数", "扣掉副反应后的有效稳定常数 K'", "ch07"),
    ("金属指示剂", "与金属离子形成有色配合物、终点变色的配体", "ch07"),
    ("掩蔽", "用掩蔽剂与干扰离子反应，降低其有效浓度", "ch07"),
    ("解蔽", "把已被掩蔽的离子重新释放出来", "ch07"),
    ("氧化数", "假设成键电子完全归电负性大原子后某原子的电荷数", "ch08"),
    ("氧化剂", "自身被还原、使对方氧化的物质", "ch08"),
    ("还原剂", "自身被氧化、使对方还原的物质", "ch08"),
    ("电极电势", "电极中氧化型得电子能力的量度", "ch08"),
    ("标准电极电势", "标准状态下以标准氢电极为基准测得的电极电势", "ch08"),
    ("原电池", "把氧化还原反应拆成两个半反应、电子经外电路流动的装置", "ch08"),
    ("盐桥", "连接两个半电池、平衡电荷的装置", "ch08"),
    ("条件电极电势", "扣掉配位、沉淀等副反应后的实际电极电势", "ch08"),
    ("滴定", "用标准溶液逐滴加入待测液直到反应完全的操作", "ch05"),
    ("化学计量点", "按计量关系恰好反应完全的理论点", "ch05"),
    ("滴定终点", "指示剂变色、停止滴定的点", "ch05"),
    ("基准物质", "能直接配制标准溶液、纯度高且稳定的物质", "ch05"),
    ("标定", "用基准物质或已知浓度溶液确定标准溶液浓度的操作", "ch05"),
    ("滴定度", "每毫升滴定剂相当于待测物的质量", "ch05"),
    ("突跃范围", "计量点附近 pH 或电势急剧变化的范围", "ch06"),
    ("缓冲溶液", "能抵抗少量酸碱、pH 基本不变的溶液", "ch06"),
    ("分布系数", "某物种占总浓度的分数", "ch06"),
    ("共轭酸碱对", "相差一个质子的一对酸和碱", "ch06"),
    ("重量分析", "通过称量沉淀或灼烧产物求待测组分含量的方法", "ch10"),
    ("沉淀形式", "沉淀剂与待测物反应生成的沉淀", "ch10"),
    ("称量形式", "沉淀经过滤、灼烧后实际称量的物质", "ch10"),
    ("换算因数", "待测物摩尔质量与称量形式摩尔质量之比（含系数）", "ch10"),
    ("共沉淀", "沉淀时杂质被吸附、夹带或混晶一起沉淀", "ch10"),
    ("后沉淀", "沉淀放置后杂质在沉淀表面继续沉淀", "ch10"),
    ("莫尔法", "以 K2CrO4 为指示剂、用 AgNO3 滴定 Cl- 的方法", "ch10"),
    ("佛尔哈德法", "以铁铵矾为指示剂、用 NH4SCN 滴定 Ag+ 的方法", "ch10"),
    ("法扬司法", "用吸附指示剂判断终点的沉淀滴定法", "ch10"),
    ("吸光度", "A=-lgT，表示溶液对光的吸收程度", "ch11"),
    ("透光率", "透射光强度与入射光强度之比 T=I/I0", "ch11"),
    ("摩尔吸光系数", "A=εbc 中的 ε，表示物质在特定波长下的吸光能力", "ch11"),
    ("标准曲线", "用系列标准溶液测 A、作 A-c 图求未知浓度的方法", "ch11"),
    ("参比电极", "电势已知且稳定、不随待测离子浓度变化的电极", "ch12"),
    ("指示电极", "电势随待测离子浓度变化的电极", "ch12"),
    ("离子选择性电极", "对特定离子有选择性响应的电极", "ch12"),
    ("电位滴定", "用电势突跃判断终点的滴定方法", "ch12"),
    ("分配系数", "物质在两种溶剂中浓度之比 KD", "ch12"),
    ("分配比", "两相中总浓度之比 D", "ch12"),
    ("萃取率", "被萃取到有机相的目标物占总量的百分比", "ch12"),
    ("离子交换", "溶液离子与树脂上可交换离子发生交换的分离方法", "ch12"),
    ("色谱", "利用组分在固定相和流动相中分配差异实现分离的方法", "ch12"),
]

CARDS = {
"ch00": [("物质分类只看哪两件事？", "是不是只有一种物质；由几种元素组成。"),
         ("常见元素化合价怎么记？", "H +1、O −2、Na/K +1、Ca/Mg/Ba +2、Al +3；化合物代数和为零。"),
         ("离子方程式拆什么、不拆什么？", "强酸强碱可溶盐拆；难溶物、气体、弱电解质、水不拆。"),
         ("物质的量四个公式？", "n=m/M、n=N/NA、n=V/Vm、c=n/V。")],
"ch01": [("四个量子数各管什么？", "n 主量子数管能层；l 管亚层形状；m 管轨道取向；ms 管自旋。"),
         ("电子排布三原则？", "能量最低、泡利不相容、洪特规则。"),
         ("VSEPR 判断分子构型的第一步？", "算中心原子价层电子对数，再看孤对电子数。"),
         ("四类晶体是什么？", "离子晶体、分子晶体、原子晶体、金属晶体。")],
"ch02": [("速率方程一般形式？", "v=k[A]^m[B]^n，m+n 为反应级数。"),
         ("Arrhenius 公式？", "k=A e^(-Ea/RT)，升温 k 增大。"),
         ("Q 与 K 比较怎么判断方向？", "Q<K 正向，Q=K 平衡，Q>K 逆向。"),
         ("勒夏特列原理四句话？", "增压向气少，升温向吸热，增浓向消耗，催化剂不移动。")],
"ch03": [("卤素氧化性顺序？", "F2>Cl2>Br2>I2；还原性 I->Br->Cl->F-。"),
         ("SO2 和 SO3 的性质差异？", "SO2 既有氧化性又有还原性；SO3 主要是酸性氧化物。"),
         ("浓硝酸与稀硝酸和铜反应产物？", "浓硝酸放 NO2，稀硝酸放 NO。"),
         ("Fe2+、Fe3+、Cu2+ 常见颜色？", "Fe2+ 浅绿，Fe3+ 黄，Cu2+ 蓝。")],
"ch04": [("误差分哪三类？", "系统误差、随机误差、过失。"),
         ("有效数字加减、乘除规则？", "加减按小数点后位数最少；乘除按有效数字位数最少。"),
         ("Q 检验用来做什么？", "判断可疑值是否应舍弃。"),
         ("置信区间表示什么？", "在一定置信度下真值所在的区间。")],
"ch05": [("化学计量点与滴定终点的区别？", "计量点是理论完全点；终点是指示剂变色点，两者有误差。"),
         ("基准物质四条件？", "纯度高、稳定、按计量反应、摩尔质量大。"),
         ("直接法与标定法各用于什么？", "基准物质直接配；NaOH、HCl、KMnO4、Na2S2O3 需标定。"),
         ("滴定计算通式？", "nA=(a/b)nB；cAVA=(a/b)cBVB。")],
"ch06": [("Ka 与 Kb 的关系？", "Ka·Kb=Kw；酸越强共轭碱越弱。"),
         ("缓冲溶液 pH 公式？", "pH=pKa+lg([A-]/[HA])。"),
         ("指示剂怎么选？", "变色范围落在突跃内，尽量靠近计量点。"),
         ("混合碱双指示剂 V1、V2 怎么判断？", "V1>V2 含 NaOH；V2>V1 含 NaHCO3；V1=V2 只有 Na2CO3。")],
"ch07": [("EDTA 与金属的配位比？", "通常 1:1。"),
         ("酸效应系数怎么定义？", "αY(H)=cY/[Y4-]，≥1。"),
         ("条件稳定常数公式？", "lgK'=lgKf−lgαY(H)（只考虑酸效应）。"),
         ("金属指示剂变色条件？", "MIn 要比 MY 不稳定，EDTA 才能夺走 M。")],
"ch08": [("标准电极电势是强度还是广度性质？", "强度性质，与配平系数无关。"),
         ("Nernst 方程？", "E=E°+(0.0592/n)lg([Ox]/[Red])。"),
         ("ΔG° 与 E° 关系？", "ΔG°=−nFE°。"),
         ("由 E° 求 K？", "lgK=nE°/0.0592。")],
"ch09": [("KMnO4 法为什么用 H2SO4 不用 HCl？", "Cl- 会被 MnO4- 氧化，消耗滴定剂。"),
         ("K2Cr2O7 法指示剂？", "二苯胺磺酸钠，终点无色变紫红。"),
         ("碘量法两种方式？", "直接法测还原性物质；间接法测氧化性物质。"),
         ("淀粉指示剂何时加？", "接近终点时加，避免吸附 I2。")],
"ch10": [("AB 型与 A2B 型溶解度公式？", "AB 型 s=√Ksp；A2B/AB2 型 s=∛(Ksp/4)。"),
         ("分步沉淀看什么？", "看开始沉淀所需沉淀剂浓度，不是只看 Ksp。"),
         ("三种沉淀滴定法条件？", "莫尔法中性/弱碱；佛尔哈德法酸性；法扬司法吸附指示剂。"),
         ("换算因数怎么写？", "F=aM(待测)/bM(称量形式)。")],
"ch11": [("A、T 关系？", "A=−lgT，T=10^-A。"),
         ("朗伯-比尔定律？", "A=εbc。"),
         ("为什么选 λmax？", "灵敏度最高，波长微小变化影响小。"),
         ("偏离比尔定律的仪器原因？", "单色光不纯、杂散光、吸收池不匹配。")],
"ch12": [("参比电极与指示电极区别？", "参比电势固定；指示电势随待测离子变。"),
         ("玻璃电极 pH 响应？", "E=K−0.0592pH（25℃）。"),
         ("萃取率公式？", "E=D/(D+V水/V有机)×100%。"),
         ("分离方法四类？", "沉淀、萃取、离子交换、色谱。")],
}

def parse_quizzes():
    quizzes = []
    idx = 0
    for cid, title, rel, diff, src, pre in CHAPTERS:
        text = open(os.path.join(BOOK, rel), encoding="utf-8").read()
        if "## 自测题" not in text:
            print("NO QUIZ", cid); continue
        sec = text.split("## 自测题")[1].split("## 复习锚点")[0]
        blocks = re.split(r"\n(?=\d+\.\s)", "\n" + sec)
        for block in blocks:
            block = block.strip()
            if not re.match(r"\d+\.\s", block):
                continue
            m = re.search(r"（答案：([^；。]+)[；。](?:解析：)?\s*(.*)）", block, re.S)
            if not m:
                print("NO ANSWER", cid, block[:40]); continue
            ans_text, explain = m.group(1).strip(), m.group(2).strip().replace("\n", " ")
            stem = block[:m.start()].strip()
            stem = re.sub(r"^\d+\.\s*", "", stem).strip()
            opt_line = ""
            lines = [l.strip() for l in stem.split("\n") if l.strip()]
            qlines = []
            for l in lines:
                if re.match(r"A\.\s", l):
                    opt_line = l
                else:
                    qlines.append(l)
            q = " ".join(qlines).strip()
            idx += 1
            if opt_line:
                parts = [p.strip() for p in re.split(r"\s(?=[A-D]\.\s)", opt_line) if p.strip()]
                opts = [re.sub(r"^[A-D]\.\s*", "", p).strip() for p in parts]
                letter = ans_text.strip()[0].upper()
                if len(opts) == 2 and opts[0] == "正确" and opts[1] == "错误":
                    ans = 0 if ans_text.strip().startswith("正确") else 1
                elif letter in "ABCD" and len(opts) == 4:
                    ans = "ABCD".index(letter)
                else:
                    print("BAD SINGLE", cid, q[:30], opts, ans_text); continue
                quizzes.append(dict(id=f"q{idx:02d}", chapterId=cid, type="single",
                                    question=q, options=opts, answer=ans,
                                    explain=explain, relatedConceptId="", optionMisconceptions=[]))
            else:
                # 判断题转成二选一，避免填空题判定过严
                opts = ["正确", "错误"]
                ans = 0 if ans_text.startswith("正确") else 1
                quizzes.append(dict(id=f"q{idx:02d}", chapterId=cid, type="single",
                                    question=q, options=opts, answer=ans,
                                    explain=explain, relatedConceptId="", optionMisconceptions=[]))
    # 关联概念
    cmap = {"ch00":"c01","ch02":"c02","ch06":"c03","ch07":"c04","ch08":"c05","ch11":"c06"}
    for q in quizzes:
        q["relatedConceptId"] = cmap.get(q["chapterId"], "")
    return quizzes

def main():
    quizzes = parse_quizzes()
    print("quizzes:", len(quizzes))
    chapters = []
    for cid, title, rel, diff, src, pre in CHAPTERS:
        chapters.append(dict(id=cid, title=title, file=rel, difficulty=diff,
                             source=src, prerequisites=pre))
    learning = [
        dict(step="01", title="化学语言与基本计算", chapterIds=["ch00"], checkpoint="能独立完成物质的量、浓度、稀释计算"),
        dict(step="02", title="物质结构", chapterIds=["ch01"], checkpoint="能写电子排布、判断分子构型与晶体类型"),
        dict(step="03", title="反应原理", chapterIds=["ch02"], checkpoint="能写速率方程、算 K、判断平衡移动"),
        dict(step="04", title="元素化学", chapterIds=["ch03"], checkpoint="能写常见元素的重要反应方程式"),
        dict(step="05", title="定量分析基础", chapterIds=["ch04", "ch05"], checkpoint="能处理误差、有效数字、滴定计算"),
        dict(step="06", title="四大滴定", chapterIds=["ch06", "ch07", "ch08", "ch09", "ch10"], checkpoint="能选指示剂、设计滴定方案、完成计算"),
        dict(step="07", title="仪器分析与分离", chapterIds=["ch11", "ch12"], checkpoint="能做分光光度法和电位分析计算"),
    ]
    manifest = dict(
        slug="inorganic-analytical-chem",
        title="无机及分析化学：考纲主线",
        subtitle="从化学常识到四大滴定、仪器分析，按零基础能读懂的方式重写",
        book=dict(title="无机及分析化学（考纲主线）",
                  author="韩忠霄、孙乃有；马凤霞、王秀彦",
                  source=["无机及分析化学 (韩忠霄, 孙乃有).pdf",
                          "无机及分析化学学习指导与习题解析 (马凤霞, 王秀彦).pdf"]),
        audience="化学几乎零基础，目标通过无机及分析化学课程考试",
        goal="覆盖化学常识、物质结构、反应原理、元素化学、四大滴定、重量分析、分光光度法与电位分析，能读材料后直接做题",
        learningPath=learning, chapters=chapters, concepts=CONCEPTS,
        glossary=[{"term": t, "def": d, "chapterId": c} for t, d, c in GLOSSARY],
        patterns=dict(file="patterns.md"), cheatsheet=dict(file="cheatsheet.md"),
        quizzes=quizzes,
        flashcards=[dict(id=f"f{i:02d}", chapterId=cid, front=f, back=b, tags=[cid])
                    for i, (cid, items) in enumerate(CARDS.items(), 1)
                    for f, b in items],
        companion="inorganic-analytical-chem学习伴侣.html",
    )
    # flashcard id 需要全局唯一，重排
    for i, fc in enumerate(manifest["flashcards"], 1):
        fc["id"] = f"f{i:02d}"
    json.dump(manifest, open(os.path.join(BOOK, "manifest.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    # quiz.md
    out = ["# 无机及分析化学 测验", ""]
    for cid, title, *_ in CHAPTERS:
        qs = [q for q in quizzes if q["chapterId"] == cid]
        if not qs: continue
        out.append(f"## {title}")
        for i, q in enumerate(qs, 1):
            out.append(f"### Q{i}. {q['question']}")
            if q.get("options"):
                out.append("  ".join(f"{chr(65+j)}. {o}" for j, o in enumerate(q["options"])))
            ans = q["answer"]
            out.append(f"**答案**：{chr(65+ans) if isinstance(ans,int) and q.get('options') else ans}")
            out.append(f"**解析**：{q['explain']}")
            out.append("")
    open(os.path.join(BOOK, "quiz.md"), "w", encoding="utf-8").write("\n".join(out))

    # flashcards.md
    out = ["# 无机及分析化学 抽认卡", ""]
    for cid, title, *_ in CHAPTERS:
        out.append(f"## {title}")
        for fc in [x for x in manifest["flashcards"] if x["chapterId"] == cid]:
            out += [f"### 卡片：{fc['front']}", f"- **背面**：{fc['back']}",
                    f"- **标签**：{cid}", f"- **章节**：{cid}", ""]
    open(os.path.join(BOOK, "flashcards.md"), "w", encoding="utf-8").write("\n".join(out))

    # glossary.md
    out = ["# 术语表", "", "| 术语 | 白话定义 | 首次出现 |", "|---|---|---|"]
    for term, d, cid in GLOSSARY:
        out.append(f"| {term} | {d} | {cid} |")
    open(os.path.join(BOOK, "glossary.md"), "w", encoding="utf-8").write("\n".join(out))
    print("chapters", len(chapters), "concepts", len(CONCEPTS), "glossary", len(GLOSSARY),
          "cards", len(manifest["flashcards"]), "quizzes", len(quizzes))

if __name__ == "__main__":
    main()
