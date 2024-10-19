import asyncio
import pathlib

from aiohttp import ClientSession


async def main():
    url = 'https://www.boxofficemojo.com/year/2019'
    async with ClientSession() as session:
        async with session.get(url) as response:
            html_body = await response.read()
            return html_body

html_data = asyncio.run(main())
OUTPUT_DIR = pathlib.Path().resolve() / "snapshots"
OUTPUT_DIR.mkdir(parent=True, exist_ok=True)
OUTPUT_FILE = OUTPUT_DIR / "2019.html"
OUTPUT_FILE.write_text(html_data.decode())
