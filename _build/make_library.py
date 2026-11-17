#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 26 本 Obsidian 知识库转成可直接浏览的静态资料库。"""
import os, re, glob, html, json
import markdown

SRC = "/home/user/Doubao/chats/38443717706407938/kb_build/kb/01-单书知识库"
OUT = "/home/user/Doubao/chats/38453368250906626/食品知枢/资料库/26本知识库"
os.makedirs(OUT, exist_ok=True)

CSS = """
:root{--bg:#f6f7fb;--panel:#fff;--text:#1f2937;--muted:#6b7280;--line:#e5e7eb;--accent:#2563eb}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.75 -apple-system,BlinkMacSystemFont,"PingFang SC","Microsoft YaHei",sans-serif}
header{position:sticky;top:0;z-index:10;background:rgba(255,255,255,.94);border-bottom:1px solid var(--line);backdrop-filter:blur(8px)}
header .inner{max-width:1080px;margin:0 auto;padding:12px 20px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}
header a{color:var(--accent);text-decoration:none;font-size:14px}
header h1{font-size:18px;margin:0;flex:1;min-width:200px}
main{max-width:1080px;margin:0 auto;padding:22px 20px 60px}
nav.toc{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:14px 18px;margin-bottom:22px}
nav.toc h2{font-size:16px;margin:0 0 10px}
nav.toc a{display:inline-block;margin:4px 10px 4px 0;color:var(--accent);text-decoration:none;font-size:14px}
article{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:22px 24px;margin-bottom:22px}
article h2{font-size:20px;margin:0 0 10px;padding-bottom:10px;border-bottom:1px solid var(--line)}
.md h1{font-size:20px;margin:18px 0 10px}
.md h2{font-size:18px;border:0;padding:0;margin:18px 0 8px}
.md h3{font-size:16px;margin:16px 0 8px}
.md p{margin:8px 0}
.md ul,.md ol{margin:8px 0 8px 22px}
.md table{border-collapse:collapse;width:100%;margin:12px 0;font-size:14px;overflow:auto;display:block}
.md th,.md td{border:1px solid var(--line);padding:8px 10px;text-align:left}
.md th{background:#f3f4f6}
.md code{background:#f3f4f6;padding:2px 5px;border-radius:4px;font-size:13px}
.md pre{background:#111827;color:#e5e7eb;padding:14px;border-radius:10px;overflow:auto;font-size:13px}
.md blockquote{border-left:4px solid #93c5fd;background:#eff6ff;margin:10px 0;padding:8px 14px;color:#374151}
.md img{max-width:100%}
.card{display:block;background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:16px 18px;margin:10px 0;text-decoration:none;color:var(--text)}
.card:hover{border-color:#93c5fd;box-shadow:0 5px 18px rgba(37,99,235,.08)}
.card b{font-size:16px;color:#1d4ed8}
.card span{display:block;color:var(--muted);font-size:14px;margin-top:4px}
.card span.badge{display:inline-block;width:auto;margin:0 6px 0 0;background:#eff6ff;color:#1d4ed8;border-radius:999px;padding:2px 10px;font-size:12px;margin-right:6px}
@media(max-width:600px){main{padding:14px 12px 40px}article{padding:16px 14px}header h1{font-size:16px}nav.toc a{font-size:13px}}
"""

def strip_wiki(s):
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    return s

def note_title(path, text):
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        return m.group(1).strip()
    return os.path.basename(path).replace(".md", "")

def note_html(path):
    text = open(path, encoding="utf-8").read()
    # 去掉 YAML frontmatter
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            text = parts[2]
    text = strip_wiki(text)
    text = re.sub(r"```mermaid[\s\S]*?```", "\n> Mermaid 图：请在 Obsidian 原库中查看。\n", text)
    text = text.replace("> [!info]", "> **元信息**").replace("> [!tip]", "> **提示**").replace("> [!warning]", "> **注意**")
    title = note_title(path, text)
    body = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    return title, body

def book_desc(bookdir):
    mocs = glob.glob(os.path.join(bookdir, "00-总览与学习路径", "*总MOC.md"))
    if not mocs:
        return ""
    txt = open(mocs[0], encoding="utf-8").read()
    m = re.search(r"内容定位\*\*：(.*)", txt)
    if m:
        return m.group(1).strip()
    m = re.search(r"内容定位[：:]\s*(.*)", txt)
    return m.group(1).strip() if m else ""

books = sorted([d for d in os.listdir(SRC) if os.path.isdir(os.path.join(SRC, d))])
index_cards = []
cat_map = {
 "化学": ["基础概念","五彩绳高中化学","普通化学原理","简明无机化学","基础化学","基础有机化学-上册","陌生方程式书写"],
 "检验检测": ["食品理化检验技术","食品安全快速检测","微生物检验方法实操指南","食品检验操作技术规范","食品检验工基础知识","食品检验工技能","食品检验工试题库"],
 "食品科学": ["食物与厨艺-奶蛋肉鱼","食物与厨艺-蔬果香料谷物","食物与厨艺-面食酱料甜点饮料","世界上最酸甜可口的化学书"],
 "统计与数据": ["食品试验设计与统计分析","SPSS统计分析","概率论与数理统计","Excel2016数据透视表"],
 "食品史与监管": ["A-Rainbow-Palate","试毒小组","屠场"],
 "微生物科普": ["微生物的秘密战争"],
}
for b in books:
    bdir = os.path.join(SRC, b)
    notes = []
    for f in sorted(glob.glob(os.path.join(bdir, "**", "*.md"), recursive=True)):
        if os.path.basename(f).startswith("."):
            continue
        try:
            title, body = note_html(f)
        except Exception as e:
            continue
        notes.append((title, body))
    rel = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", b).strip("-")
    outfile = os.path.join(OUT, rel + ".html")
    toc = "".join(f'<a href="#n{i}">{html.escape(t)}</a>' for i, (t, _) in enumerate(notes))
    arts = "".join(f'<article id="n{i}"><div class="md">{body}</div></article>' for i, (_, body) in enumerate(notes))
    page = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{html.escape(b)} · 食品资料库</title><style>{CSS}</style></head><body>
<header><div class="inner"><a href="../26本知识库索引.html">← 资料库索引</a><h1>{html.escape(b)}</h1><a href="../../index.html">主站</a></div></header>
<main><nav class="toc"><h2>{len(notes)} 篇笔记</h2>{toc}</nav>{arts}</main></body></html>"""
    open(outfile, "w", encoding="utf-8").write(page)
    desc = book_desc(bdir)
    cat = "其他"
    for k, vals in cat_map.items():
        if b in vals or any(v in b for v in vals):
            cat = k; break
    index_cards.append(f'<a class="card" href="26本知识库/{html.escape(rel)}.html"><b>{html.escape(b)}</b><span><span class="badge">{html.escape(cat)}</span>{html.escape(desc or "点击浏览全书笔记")}</span><span>{len(notes)} 篇笔记</span></a>')

index = f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>26 本食品检验检测知识库 · 资料库</title><style>{CSS}</style></head><body>
<header><div class="inner"><a href="../index.html">← 返回主站</a><h1>26 本食品检验检测知识库</h1><a href="26本食品检验检测全流程-Obsidian知识库.zip">下载原始 Obsidian 包</a></div></header>
<main>
<article><div class="md"><h1>这是什么</h1><p>这里是 26 本食品科学、检验、化学、统计、食品史书籍的 Obsidian 笔记的静态镜像。原始双链结构仍在 zip 里；这里按书拆成 HTML，方便在手机和浏览器里直接翻阅、搜索、摘句。</p><p>它不是学习主线。主线在《食品类大方向精讲》和《食品类大方向题库》；这里用于查细节、查标准、查案例。</p></div></article>
{''.join(index_cards)}
</main></body></html>"""
open(os.path.join(OUT, "..", "26本知识库索引.html"), "w", encoding="utf-8").write(index)
print("books", len(index_cards), "output", OUT)
