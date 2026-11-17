# 食品知枢 · 食品类大方向学习系统

把无机化学、分析化学、食品化学、食品营养、理化检验、微生物与快检、数据法规整合成一套可学、可练、可判的学习系统。

## 入口

打开 `index.html`。左侧切书，右侧读章节；每章底部有自测；题库按考点练。

## 四本书

- `01-食品类大方向精讲`：12 章，60 道自测，75 条术语，24 张抽认卡。
- `02-食品类大方向题库`：12 章，48 个考点，144 题，每考点 1 母题 + 2 变式。
- `03-无机及分析化学`：13 章，130 题，来自化学知枢。
- `04-无机及分析化学题库`：13 章，78 题，来自化学知枢。

合计 50 章、412 道题。

## 配套

- `资料库/26本食品检验检测全流程-Obsidian知识库.zip`：26 本书、约 1276 篇笔记。
- `资料库/26本知识库索引.html`：26 本书的站内浏览入口。
- `资料库/速查手册.html`：术语、标准、职业路径速查。
- `资料库/食品检验检测_知识与术语速查手册.md`：速查手册的 Markdown 原文。
- 外部链接：化学知枢、食品专业高等数学、Pages 索引。

## 部署 GitHub Pages

```bash
cd 食品知枢
git init
git add -A
git commit -m "食品知枢：食品类大方向学习系统"
git branch -M main
git remote add origin https://github.com/zrx-11/food-zhishu.git
git push -u origin main
```

仓库 Settings → Pages → Source: Deploy from a branch → Branch: main → 目录: / (root) → Save。

约 1—2 分钟后访问：https://zrx-11.github.io/food-zhishu/

## 构建

```bash
python3 _build/tools/build_companion.py --manifest 01-食品类大方向精讲/manifest.json --out 01-食品类大方向精讲/food-direction学习伴侣.html
python3 _build/tools/build_companion.py --manifest 02-食品类大方向题库/manifest.json --out 02-食品类大方向题库/food-direction-bank学习伴侣.html
python3 _build/tools/build_handbook.py --root .
python3 _build/tools/verify_handbook.py --index index.html --chromium /usr/local/bin/chromium
```

## 说明

学习材料，不是标准文本。限量、方法、判定以现行国家标准和当年招生文件为准。
