# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from data_a import BOOK_A
from data_b import BOOK_B
from data_c import BOOK_C

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = ["01-零基础入门","02-普通化学原理","03-简明无机化学","04-有机化学基础","05-陌生方程式诊断"]
BOOKS = BOOK_A + BOOK_B + BOOK_C

PATTERNS = {
"01-零基础入门": """# 模式与框架库

## 框架：物质分类树
拿到一个物质名，先问两个问题：是不是只有一种物质？由几种元素组成？两步就能落到单质、化合物、氧化物、酸碱盐。

## 决策规则
- 判断电解质：先确认是化合物，再看水溶液或熔融态能否导电。铜能导电但是单质，不是电解质。
- 写离子方程式：写 → 拆 → 删 → 查。拆之前先问"它溶不溶、强不强"。
- 判断氧化还原：只看化合价有没有变，不看有没有氧气参加。

## 反模式
- 配平时改下标。下标一改，物质就变了，方程式再平衡也不是原反应。
- 把"能导电"当成"是电解质"。
- 平衡时认为反应停止。平衡是动态的，v正 = v逆 ≠ 0。
""",
"02-普通化学原理": """# 模式与框架库

## 框架：热力学三问
1. 这个过程的 ΔH 是多少（放热还是吸热）？
2. ΔS 是多少（混乱度增还是减）？
3. 用 ΔG = ΔH - TΔS 判断方向，必要时算转折温度。

## 决策规则
- 平衡移动：先看改变的是温度还是浓度/压强。只有温度改变 K，浓度和压强只改变 Q。
- 求平衡浓度：列 ICE 表，设变化量 x，代入 K，取正根。
- 判断电极：E° 大的作正极；算 E电池 = E正 - E负，为正则自发。
- 判断杂化：数价层电子对（σ 键 + 孤对），2/3/4 对应 sp/sp²/sp³。

## 反模式
- 只看焓判断自发。吸热反应也可能自发，必须加上 TΔS。
- 认为催化剂能提高产率。催化剂只缩短时间，不改 K。
- 把 Ksp 直接比大小判断溶解度。只有同类型（AB 型）才能直接比。
""",
"03-简明无机化学": """# 模式与框架库

## 框架：元素学习四条线
单质（颜色、状态、与酸碱水的反应）→ 氧化物（酸碱性、与水反应）→ 氢化物（稳定性、还原性）→ 含氧酸及盐（酸性、氧化性、溶解性）。

## 决策规则
- 比较非金属性：看氢化物稳定性、最高价含氧酸酸性。
- 比较金属性：看单质与水/酸反应剧烈程度、最高价氢氧化物碱性。
- 判断两性：氧化物或氢氧化物既能与强酸反应又能与强碱反应，如 Al2O3、Al(OH)3、ZnO。
- 配合物命名：配体数 + 配体名 + 合 + 中心离子（氧化数）。

## 反模式
- 把 Na2O2 当碱性氧化物。它是过氧化物，O 为 -1。
- 认为过渡金属离子都有颜色。Zn2+、Sc3+ 无色。
- 认为铝不活泼。铝表面有致密氧化膜，内部很活泼。
""",
"04-有机化学基础": """# 模式与框架库

## 框架：结构决定性质
先画碳骨架，再标官能团，最后由官能团判断反应类型：双键加成、羟基酯化、羧基酸性、卤代烃取代/消除。

## 决策规则
- 数同分异构：碳链由长到短、支链由少到多、位置由中到边。
- 判断马氏加成：看碳正离子稳定性，三级 > 二级 > 一级。
- 判断手性碳：一个碳上四个基团是否全不同；再用次序规则定 R/S。
- 卤代烃取代还是消除：弱碱低温取代，强碱高温消除。

## 反模式
- 把构象当同分异构。单键旋转不断键，是同一物质。
- 认为苯容易加成。加成破坏芳香性，苯主要发生取代。
- 认为 R 一定右旋。旋光方向必须实测，与 R/S 无固定对应。
""",
"05-陌生方程式诊断": """# 模式与框架库

## 框架：五步流水线
读信息（反应物、产物线索、环境、价态）→ 判类型（化学式/离子式/电极式）→ 定产物（价态、环境、元素守恒）→ 配平（电子、原子、电荷）→ 检查（原子、电荷、电子、符号）。

## 决策规则
- 有化合价变化：先电子守恒，再配原子，最后用 H+ 或 OH- 调电荷。
- 酸性补 H+，碱性补 OH-，熔融碳酸盐补 CO3^2-。
- 离子方程式：难溶物、气体、水、弱电解质、氧化物一律不拆。
- 电极反应：先定正负极，再写半反应，最后按电解质环境补离子。

## 反模式
- 只数原子不管电荷。离子方程式电荷不平，一定错。
- 产物全靠猜。产物要由价态、环境、元素守恒三条线索推。
- 气体、沉淀符号漏标。符号也是得分点。
"""
}

CHEATSHEET = {
"01-零基础入门": """# 速查表

## 核心公式
| 场景 | 内容 |
|---|---|
| 物质的量 | n = m/M |
| 微粒数 | n = N/N_A，N_A = 6.02×10²³ |
| 气体体积 | n = V/V_m，标况 V_m = 22.4 L/mol |
| 浓度 | c = n/V溶液 |

## 常见化合价
| 元素 | 价态 |
|---|---|
| H | +1（金属氢化物中 -1） |
| O | -2（过氧化物 -1） |
| Na、K | +1 |
| Ca、Mg、Ba | +2 |
| Al | +3 |
| Fe | +2、+3 |
| Cu | +2（少数 +1） |
| Cl | -1（氯化物中） |
| S | -2（硫化物中） |

## 离子方程式拆写
- 拆：强酸、强碱、可溶盐
- 不拆：难溶物、气体、水、弱电解质、氧化物、微溶物悬浊液
""",
"02-普通化学原理": """# 速查表

## 热力学
| 场景 | 内容 |
|---|---|
| 第一定律 | ΔU = Q + W |
| 焓 | H = U + pV；恒压 Qp = ΔH |
| 吉布斯 | ΔG = ΔH - TΔS |
| 标准自由能 | ΔG° = -RT lnK |
| 电化学 | ΔG° = -nFE° |

## 平衡
| 场景 | 内容 |
|---|---|
| Kc | 生成物浓度幂之积 / 反应物浓度幂之积 |
| Kp | 分压形式，Kp = Kc(RT)^Δn |
| 方向 | Q<K 正向；Q>K 逆向 |
| 缓冲 | pH = pKa + lg([A-]/[HA]) |

## 结构
| 电子对 | 杂化 | 构型 |
|---|---|---|
| 2 | sp | 直线 180° |
| 3 | sp² | 平面三角 120° |
| 4 | sp³ | 四面体 109.5° |
""",
"03-简明无机化学": """# 速查表

## 常见反应
| 反应 | 方程式 |
|---|---|
| 氯气与碱 | Cl2 + 2NaOH → NaCl + NaClO + H2O |
| 钠与水 | 2Na + 2H2O → 2NaOH + H2↑ |
| 过氧化钠 | 2Na2O2 + 2H2O → 4NaOH + O2↑ |
| 铝与碱 | 2Al + 2NaOH + 2H2O → 2NaAlO2 + 3H2↑ |
| 铝热 | 2Al + Fe2O3 → Al2O3 + 2Fe |
| 合成氨 | N2 + 3H2 ⇌ 2NH3 |
| 氨催化氧化 | 4NH3 + 5O2 → 4NO + 6H2O |

## 离子颜色
| 离子 | 颜色 |
|---|---|
| Fe2+ | 浅绿 |
| Fe3+ | 黄 |
| Cu2+ | 蓝 |
| Mn2+ | 浅粉 |
| MnO4- | 紫 |
| Cr2O7^2- | 橙 |
| CrO4^2- | 黄 |
""",
"04-有机化学基础": """# 速查表

## 官能团与反应
| 官能团 | 典型反应 |
|---|---|
| C=C | 加成、氧化、聚合 |
| —OH | 与 Na 反应、酯化、氧化 |
| —COOH | 酸性、酯化 |
| —CHO | 银镜反应、还原 |
| —X | 取代、消除 |
| 苯环 | 亲电取代 |

## 规则
| 场景 | 规则 |
|---|---|
| 马氏加成 | H 加到含氢多的碳上 |
| 反马氏 | 过氧化物存在下的 HBr 加成 |
| 手性碳 | 四个基团全不同 |
| R/S | 最低优先级朝后，其余顺 R 逆 S |
| 卤代烃 | 弱碱低温取代，强碱高温消除 |
""",
"05-陌生方程式诊断": """# 速查表

## 五步
1. 读信息：反应物、产物线索、环境、价态
2. 判类型：化学式 / 离子式 / 电极式
3. 定产物：价态、环境、元素守恒
4. 配平：电子 → 原子 → 电荷
5. 检查：原子、电荷、电子、符号

## 环境补项
| 环境 | 补什么 |
|---|---|
| 酸性 | H+ 和 H2O |
| 碱性 | OH- 和 H2O |
| 熔融碳酸盐 | CO3^2- 和 CO2 |

## 高频产物
| 元素 | 常见产物 |
|---|---|
| Mn | Mn2+（酸性）、MnO2（中性/弱碱） |
| Cr | Cr3+（还原）、CrO4^2-（碱性氧化） |
| S | SO2、SO4^2-、S |
| N | NO、NO3-、N2 |
| C | CO2、CO3^2- |
"""
}

def write_book(book, dirname):
    d = os.path.join(ROOT, dirname)
    chapters = []
    for ch in book["chapters"]:
        chapters.append({
            "id": ch["id"], "title": ch["title"], "file": ch["file"],
            "difficulty": ch["difficulty"], "source": ch["source"],
            "prerequisites": ch["prereq"]
        })
    concepts = []
    for c in book["concepts"]:
        item = {"id": c["id"], "title": c["title"], "file": c["file"],
                "chapterIds": c["chapters"], "difficulty": c["difficulty"],
                "source": c["source"], "prerequisites": c["prereq"]}
        if c.get("depth"):
            item["depthFragment"] = c["depth"]
        concepts.append(item)
    flashcards = []
    n = 0
    for ch in book["chapters"]:
        n += 1
        flashcards.append({"id": f"f{n:02d}", "chapterId": ch["id"],
                           "front": f"{ch['title'].split('：')[-1]}：一句话核心是什么？",
                           "back": ch["core"], "tags": [ch["id"]]})
        n += 1
        flashcards.append({"id": f"f{n:02d}", "chapterId": ch["id"],
                           "front": f"{ch['title'].split('：')[-1]}最容易错在哪？",
                           "back": ch["trap"], "tags": [ch["id"], "易错"]})
    manifest = {
        "slug": book["slug"], "title": book["title"], "subtitle": book["subtitle"],
        "book": book["book"], "audience": book["audience"], "goal": book["goal"],
        "learningPath": book["path"], "chapters": chapters, "concepts": concepts,
        "glossary": book["glossary"],
        "patterns": {"file": "patterns.md"}, "cheatsheet": {"file": "cheatsheet.md"},
        "quizzes": book["quizzes"], "flashcards": flashcards,
        "companion": "学习伴侣.html"
    }
    with open(os.path.join(d, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    # SKILL.md 总纲
    lines = [f"# {book['title']}", "", "## 这本在讲什么", book["goal"], "",
             "## 学习路径（推荐顺序）", "| 步骤 | 主题 | 章节 | 检查点 |", "|---|---|---|---|"]
    for s in book["path"]:
        lines.append(f"| {s['step']} | {s['title']} | {'、'.join(s['chapterIds'])} | {s['checkpoint']} |")
    lines += ["", "## 章节索引"]
    for ch in book["chapters"]:
        lines.append(f"- {ch['title']}（难度 {'★'*ch['difficulty']}{'☆'*(3-ch['difficulty'])}）→ {ch['file']}")
    lines += ["", "## 前置缺口", "| 缺口 | 补讲位置 | 学完标志 |", "|---|---|---|"]
    for ch in book["chapters"]:
        if ch["prereq"]:
            lines.append(f"| {'、'.join(ch['prereq'])} | 对应前置章节 | 能复述前置章的一句话核心 |")
    lines += ["", "## 术语 / 模式 / 速查入口", "- 术语表：glossary.md", "- 模式库：patterns.md", "- 速查表：cheatsheet.md"]
    with open(os.path.join(d, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    # glossary.md
    gl = ["# 术语表", "", "| 术语 | 白话定义 | 章节 |", "|---|---|---|"]
    for g in book["glossary"]:
        gl.append(f"| {g['term']} | {g['def']} | {g['chapterId']} |")
    with open(os.path.join(d, "glossary.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(gl) + "\n")

    # flashcards.md
    fc = ["# 抽认卡", ""]
    for ch in book["chapters"]:
        fc.append(f"## {ch['title']}")
        for card in [c for c in flashcards if c["chapterId"] == ch["id"]]:
            fc += [f"### 卡片：{card['front']}", f"- **背面**：{card['back']}", f"- **标签**：{', '.join(card['tags'])}", f"- **章节**：{ch['id']}", ""]
    with open(os.path.join(d, "flashcards.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(fc) + "\n")

    # quiz.md（05 已有手写版，保留）
    qp = os.path.join(d, "quiz.md")
    if not os.path.exists(qp) or dirname != "05-陌生方程式诊断":
        qm = ["# 测验题库", ""]
        for q in book["quizzes"]:
            qm.append(f"### {q['id']}（{q['type']}）{q['question']}")
            if q.get("options"):
                for i, o in enumerate(q["options"]):
                    qm.append(f"- {'ABCD'[i]}. {o}")
            qm += [f"**答案**：{q['answer']}", f"**解析**：{q['explain']}", ""]
        with open(qp, "w", encoding="utf-8") as f:
            f.write("\n".join(qm) + "\n")

    with open(os.path.join(d, "patterns.md"), "w", encoding="utf-8") as f:
        f.write(PATTERNS[dirname])
    with open(os.path.join(d, "cheatsheet.md"), "w", encoding="utf-8") as f:
        f.write(CHEATSHEET[dirname])
    print("wrote", dirname, len(chapters), len(concepts), len(book["quizzes"]))

for b, dn in zip(BOOKS, DIRS):
    write_book(b, dn)
