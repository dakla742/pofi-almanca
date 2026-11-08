import asyncio, os
from playwright.async_api import async_playwright

FPS = 24
TOTAL = 33.2

async def main():
    os.makedirs("frames", exist_ok=True)
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 400, "height": 900}, device_scale_factor=3)
        await page.goto("file://" + os.path.abspath("index.html") + "?render=1")
        await page.wait_for_timeout(500)
        stage = page.locator("#stage")
        for i in range(int(TOTAL * FPS)):
            await page.evaluate(f"renderAt({i / FPS})")
            await stage.screenshot(path=f"frames/f{i:05d}.jpg", type="jpeg", quality=92)
        await browser.close()

asyncio.run(main())
