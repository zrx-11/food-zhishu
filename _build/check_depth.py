import asyncio, json
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(executable_path="/usr/local/bin/chromium",args=["--no-sandbox"])
        pg=await b.new_page(viewport={"width":1440,"height":900})
        out={}
        for book,con in [("general-chem","c02"),("general-chem","c03"),("general-chem","c05"),("organic-chem","c01")]:
            await pg.goto("file:///home/user/Doubao/chats/38453368250906626/化学知枢/index.html")
            await pg.wait_for_timeout(1200)
            await pg.evaluate(f"location.hash='#/book/{book}/concept/{con}'")
            await pg.wait_for_timeout(800)
            before=await pg.evaluate("document.querySelectorAll('.katex').length")
            if await pg.query_selector("details.depth-fragment"):
                await pg.click("details.depth-fragment summary")
                await pg.wait_for_timeout(1200)
                after=await pg.evaluate("""() => ({len:document.querySelector('details.depth-fragment').innerText.length,
                   katex:document.querySelectorAll('.katex').length,
                   h2:document.querySelectorAll('details.depth-fragment h2, details.depth-fragment h3').length})""")
                out[f"{book}/{con}"]={"before_katex":before, **after}
            else:
                out[f"{book}/{con}"]={"exists":False}
        print(json.dumps(out,ensure_ascii=False,indent=1))
        await b.close()
asyncio.run(main())
