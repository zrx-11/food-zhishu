#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = 'file://' + os.path.join(ROOT, 'index.html')
report = {'ok': [], 'fail': []}

def mark(name, cond, detail=''):
    (report['ok'] if cond else report['fail']).append({'name': name, 'detail': detail})
    print(('OK  ' if cond else 'FAIL') + ' ' + name + (' :: ' + detail if detail else ''))

BOOKS = {
    'food-direction': ('01', 12, 5),
    'food-direction-bank': ('02', 12, 12),
    'inorganic-analytical-chem': ('03', 13, 10),
    'inorganic-analytical-chem-bank': ('04', 13, 6),
}

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/local/bin/chromium', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1440, 'height': 1000})
    errs = []
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.goto(INDEX, wait_until='load'); pg.wait_for_timeout(800)
    body = pg.locator('body').inner_text()
    mark('首页四本书', all(x in body for x in ['食品类大方向', '食品类大方向题库', '无机及分析化学', '无机及分析化学题库']))
    mark('首页 412 题', '412' in body)
    mark('首页视频链接', 'b23.tv' in pg.locator('body').inner_html())
    mark('首页 26 本知识库', '26 本' in body)

    for key, (num, nch, nq) in BOOKS.items():
        pg.goto(INDEX + f'#/book/{key}/chapter/ch01', wait_until='load'); pg.wait_for_timeout(250)
        mark(f'{num} 首章可读', ('学习目标' in pg.locator('body').inner_text()) or ('考点地图' in pg.locator('body').inner_text()))
        pg.goto(INDEX + f'#/book/{key}/quiz/ch01', wait_until='load'); pg.wait_for_timeout(150)
        n = pg.locator('.quiz-item').count()
        mark(f'{num} ch01 {nq} 题', n == nq, str(n))
        pg.goto(INDEX + f'#/book/{key}/graph', wait_until='load'); pg.wait_for_timeout(500)
        st = pg.locator('#graph-status').inner_text()
        mark(f'{num} 图谱画布', pg.locator('#graph-container canvas').count() == 1, st)
        mark(f'{num} 图谱节点数', str(nch) in st or (num=='03' and '19' in st), st)
        pg.goto(INDEX + f'#/book/{key}/cards', wait_until='load'); pg.wait_for_timeout(150)
        mark(f'{num} 抽认卡页', '抽认卡' in pg.locator('body').inner_text())
        pg.goto(INDEX + f'#/book/{key}/glossary', wait_until='load'); pg.wait_for_timeout(150)
        mark(f'{num} 术语页', '术语' in pg.locator('body').inner_text())

    # 01 最后一章
    pg.goto(INDEX + '#/book/food-direction/chapter/ch12', wait_until='load'); pg.wait_for_timeout(200)
    mark('01 末章可读', '专升本' in pg.locator('body').inner_text())
    # 02 最后一章
    pg.goto(INDEX + '#/book/food-direction-bank/chapter/ch12', wait_until='load'); pg.wait_for_timeout(200)
    mark('02 末章可读', '考点地图' in pg.locator('body').inner_text())

    # 判题：01 ch02 Q1 答案 B
    pg.goto(INDEX + '#/book/food-direction/quiz/ch02', wait_until='load'); pg.wait_for_timeout(150)
    q = pg.locator('.quiz-item').nth(0)
    q.locator('input').nth(1).check(); q.locator('.quiz-check').click(); pg.wait_for_timeout(100)
    mark('01 ch02 Q1 判题正确', '正确' in q.locator('.quiz-feedback').inner_text())
    # 判题：02 ch03 Q1 答案 B
    pg.goto(INDEX + '#/book/food-direction-bank/quiz/ch03', wait_until='load'); pg.wait_for_timeout(150)
    q = pg.locator('.quiz-item').nth(0)
    q.locator('input').nth(1).check(); q.locator('.quiz-check').click(); pg.wait_for_timeout(100)
    mark('02 ch03 Q1 判题正确', '正确' in q.locator('.quiz-feedback').inner_text())
    mark('02 解析含考点', '考点' in q.locator('.quiz-explain').inner_text())

    # 搜索
    pg.goto(INDEX, wait_until='load'); pg.wait_for_timeout(400)
    inp = pg.locator('input[placeholder*="搜索"]').first
    inp.fill('苯甲酸'); pg.wait_for_timeout(600)
    mark('站内搜索有结果', pg.locator('.search-result, .search-hit, .search-item').count() > 0,
         str(pg.locator('.search-result, .search-hit, .search-item').count()))

    # 手机
    m = b.new_page(viewport={'width': 390, 'height': 844})
    merrs = []
    m.on('console', lambda x: merrs.append(x.text) if x.type == 'error' else None)
    for key, (num, nch, nq) in BOOKS.items():
        m.goto(INDEX + f'#/book/{key}/graph', wait_until='load'); m.wait_for_timeout(500)
        mark(f'390 {num} 路线图', m.locator('.kg-item').count() == nch, str(m.locator('.kg-item').count()))
        mark(f'390 {num} 无画布', m.locator('#graph-container canvas').count() == 0)
    m.goto(INDEX + '#/book/food-direction/quiz/ch01', wait_until='load'); m.wait_for_timeout(250)
    mark('390 01 测验 5 题', m.locator('.quiz-item').count() == 5)
    mw = m.evaluate('document.documentElement.scrollWidth')
    mark('390 无横向溢出', mw <= 390 + 2, str(mw))
    mark('390 控制台零错误', len(merrs) == 0, str(merrs[:2]))
    m.screenshot(path=os.path.join(ROOT, '_build', 'verify-mobile-food.png'), full_page=True)
    m.close()

    pg.goto(INDEX, wait_until='load'); pg.wait_for_timeout(300)
    pg.screenshot(path=os.path.join(ROOT, '_build', 'verify-desktop-food.png'), full_page=False)
    pg.goto(INDEX + '#/book/food-direction/graph', wait_until='load'); pg.wait_for_timeout(500)
    pg.screenshot(path=os.path.join(ROOT, '_build', 'verify-graph-food.png'), full_page=False)

    # 资料库
    lib = 'file://' + os.path.join(ROOT, '资料库', '26本知识库索引.html')
    pg.goto(lib, wait_until='load'); pg.wait_for_timeout(300)
    mark('资料库索引 26 本', pg.locator('.card').count() == 26, str(pg.locator('.card').count()))
    first = pg.locator('.card').first.get_attribute('href')
    pg.goto('file://' + os.path.join(ROOT, '资料库', first), wait_until='load'); pg.wait_for_timeout(300)
    mark('资料库单书可读', pg.locator('article').count() > 0, str(pg.locator('article').count()))
    pg.goto('file://' + os.path.join(ROOT, '资料库', '速查手册.html'), wait_until='load'); pg.wait_for_timeout(200)
    mark('速查手册网页可读', '食品' in pg.locator('body').inner_text())
    mark('桌面控制台零错误', len(errs) == 0, str(errs[:2]))
    b.close()

json.dump(report, open(os.path.join(ROOT, '_build', 'verify-food.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print(f"\n通过 {len(report['ok'])} 项，失败 {len(report['fail'])} 项")
if report['fail']:
    print(json.dumps(report['fail'], ensure_ascii=False, indent=2))
    raise SystemExit(1)
