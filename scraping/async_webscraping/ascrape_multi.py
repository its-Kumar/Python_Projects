import asyncio
import pathlib

from aiohttp import ClientSession


async def fetch(url, session, year=None):
    async with session.get(url) as response:
        html_body = await response.read()
        return {"body": html_body, "year": year}


async def fetch_with_sem(url, session, year, sem):
    async with sem:
        return await fetch(url, session, year)


async def main(start_year=2020, years_ago=5):
    pages_content = {}
    tasks = []
    # semaphore
    sem = asyncio.Semaphore(10)
    async with ClientSession() as session:
        for i in range(0, years_ago):
            year = start_year - i
            url = f'https://www.boxofficemojo.com/year/{year}/'
            print(year, url)
            tasks.append(
                asyncio.create_task(fetch_with_sem(url, session, year, sem))
            )
            pages_content = await asyncio.gather(*tasks)
        return pages_content


results = asyncio.run(main())
# print(results)
OUTPUT_DIR = pathlib.Path().resolve() / "snapshots"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
for result in results:
    current_year = result.get("year")
    html_data = result.get("body")
    OUTPUT_FILE = OUTPUT_DIR / f"{current_year}.html"
    OUTPUT_FILE.write_text(html_data.decode())
