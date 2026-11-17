import asyncio, json
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/local/bin/chromium", args=["--no-sandbox"])
        pg = await b.new_page(viewport={"width":1440,"height":900})
        errs=[]
        pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
        await pg.goto("file:///home/user/Doubao/chats/38453368250906626/化学知枢/index.html")
        await pg.wait_for_timeout(3000)
        # 深度片段
        await pg.evaluate("location.hash='#/book/general-chem/concept/c02'")
        await pg.wait_for_timeout(800)
        d = await pg.evaluate("""() => {
          const el=document.querySelector('details.depth-fragment');
          return el ? {exists:true, open:el.open, text:el.innerText.length} : {exists:false};
        }""")
        # 展开
        if d.get("exists"):
            await pg.click("details.depth-fragment summary")
            await pg.wait_for_timeout(400)
            d2 = await pg.evaluate("document.querySelector('details.depth-fragment').open")
        else:
            d2=None
        # 公式
        katex = await pg.evaluate("document.querySelectorAll('.katex').length")
        # 表格溢出
        overflow = await pg.evaluate("""() => {
          const bad=[]; document.querySelectorAll('.main table, #view table').forEach(t=>{
            if(t.scrollWidth > t.parentElement.clientWidth+2) bad.push(t.innerText.slice(0,20));
          }); return bad;
        }""")
        # 390 视口
        await pg.set_viewport_size({"width":390,"height":844})
        await pg.evaluate("location.hash='#/book/general-chem/chapter/ch04'")
        await pg.wait_for_timeout(600)
        box = await pg.evaluate("""() => {
          const v=document.querySelector('#view');
          const cs=getComputedStyle(v);
          return {left:cs.paddingLeft, right:cs.paddingRight, width:v.clientWidth, tables:[...v.querySelectorAll('table')].map(t=>t.scrollWidth>t.clientWidth+2)};
        }""")
        await pg.screenshot(path="_build/mobile.png", full_page=False)
        await pg.set_viewport_size({"width":1440,"height":900})
        await pg.wait_for_timeout(300)
        await pg.screenshot(path="_build/desktop.png", full_page=False)
        print(json.dumps({"depth":d,"depth_open_after":d2,"katex":katex,"table_overflow":overflow,"mobile":box,"console_errors":errs[:5]}, ensure_ascii=False, indent=1))
        await b.close()

asyncio.run(main())
