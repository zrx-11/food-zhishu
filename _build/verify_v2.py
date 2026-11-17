#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json, os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = 'file://' + os.path.join(ROOT, 'index.html')
B3 = ['ch%02d' % i for i in range(13)]
B4 = ['ch%02d' % i for i in range(13)]
report = {'ok': [], 'fail': []}

def mark(name, cond, detail=''):
    (report['ok'] if cond else report['fail']).append({'name': name, 'detail': detail})
    print(('OK  ' if cond else 'FAIL') + ' ' + name + (' :: ' + detail if detail else ''))

with sync_playwright() as p:
    b = p.chromium.launch(executable_path='/usr/local/bin/chromium', args=['--no-sandbox'])
    pg = b.new_page(viewport={'width': 1440, 'height': 1000})
    errs = []
    pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None)
    pg.goto(INDEX, wait_until='load'); pg.wait_for_timeout(800)
    tabs = pg.locator('.book-tab, .tab, nav a').all_inner_texts()
    body = pg.locator('body').inner_text()
    mark('首页 6 本书', all(x in body for x in ['无机及分析化学', '零基础入门', '普通化学原理', '基础有机化学', '陌生方程式']))
    mark('首页 04 显示 78 题', '78 题' in body)
    mark('首页两个视频入口', body.count('B站') >= 1 or 'b23.tv' in pg.locator('body').inner_html())

    # 03 图谱桌面
    pg.goto(INDEX + '#/book/inorganic-analytical-chem/graph', wait_until='load'); pg.wait_for_timeout(900)
    st = pg.locator('#graph-status').inner_text()
    mark('03 图谱桌面画布', pg.locator('#graph-container canvas').count() == 1, st)
    mark('03 图谱节点数', '19 个节点' in st and '24 条关系' in st, st)
    mark('03 图谱侧栏入口', '知识图谱' in pg.locator('body').inner_text())

    # quiz 数量
    for cid in B3:
        pg.goto(INDEX + f'#/book/inorganic-analytical-chem/quiz/{cid}', wait_until='load'); pg.wait_for_timeout(120)
        n = pg.locator('.quiz-item').count()
        mark('03 ' + cid + ' 10 题', n == 10, str(n))
    for cid in B4:
        pg.goto(INDEX + f'#/book/inorganic-analytical-chem-bank/quiz/{cid}', wait_until='load'); pg.wait_for_timeout(120)
        n = pg.locator('.quiz-item').count()
        mark('04 ' + cid + ' 6 题', n == 6, str(n))

    # 03 第6章 Q9
    pg.goto(INDEX + '#/book/inorganic-analytical-chem/quiz/ch06', wait_until='load'); pg.wait_for_timeout(200)
    q9 = pg.locator('.quiz-item').nth(8)
    mark('03 ch06 Q9 已替换为草酸', 'H₂C₂O₄' in q9.locator('.quiz-q').inner_text())
    q9.locator('input').nth(0).check(); q9.locator('.quiz-check').click(); pg.wait_for_timeout(100)
    mark('03 ch06 Q9 判题正确', '正确' in q9.locator('.quiz-feedback').inner_text())

    # 04 变式作答
    pg.goto(INDEX + '#/book/inorganic-analytical-chem-bank/quiz/ch06', wait_until='load'); pg.wait_for_timeout(200)
    q2 = pg.locator('.quiz-item').nth(1)
    q2.locator('input').nth(1).check(); q2.locator('.quiz-check').click(); pg.wait_for_timeout(100)
    mark('04 ch06 Q2 判题正确', '正确' in q2.locator('.quiz-feedback').inner_text())
    mark('04 ch06 Q2 解析含变式', '变式' in q2.locator('.quiz-explain').inner_text())

    # 搜索
    pg.goto(INDEX, wait_until='load'); pg.wait_for_timeout(500)
    inp = pg.locator('input[placeholder*="搜索"]').first
    inp.fill('滴定'); pg.wait_for_timeout(600)
    mark('站内搜索有结果', pg.locator('.search-result, .search-hit, .search-item').count() > 0,
         str(pg.locator('.search-result, .search-hit, .search-item').count()))

    # 手机
    m = b.new_page(viewport={'width': 390, 'height': 844})
    merrs = []
    m.on('console', lambda x: merrs.append(x.text) if x.type == 'error' else None)
    for key, cnt in [('inorganic-analytical-chem', 13), ('inorganic-analytical-chem-bank', 13), ('zero-basis-chem', 10)]:
        m.goto(INDEX + f'#/book/{key}/graph', wait_until='load'); m.wait_for_timeout(500)
        mark('390 ' + key + ' 路线图', m.locator('.kg-item').count() == cnt, str(m.locator('.kg-item').count()))
        mark('390 ' + key + ' 无画布缩略', m.locator('#graph-container canvas').count() == 0)
    m.goto(INDEX + '#/book/inorganic-analytical-chem/quiz/ch00', wait_until='load'); m.wait_for_timeout(300)
    mark('390 03 测验 10 题', m.locator('.quiz-item').count() == 10)
    mw = m.evaluate('document.documentElement.scrollWidth')
    mark('390 无横向溢出', mw <= 390 + 2, str(mw))
    mark('390 控制台零错误', len(merrs) == 0, str(merrs[:2]))
    m.screenshot(path=os.path.join(ROOT, '_build', 'verify-mobile-quiz.png'), full_page=True)
    m.close()

    mark('桌面控制台零错误', len(errs) == 0, str(errs[:2]))
    pg.screenshot(path=os.path.join(ROOT, '_build', 'verify-desktop-graph.png'), full_page=True)
    b.close()

print(json.dumps({'ok': len(report['ok']), 'fail': len(report['fail']), 'failed': report['fail']}, ensure_ascii=False))
json.dump(report, open(os.path.join(ROOT, '_build', 'verify_v2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
