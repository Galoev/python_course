import asyncio
import aiohttp
import aiofiles
import click

async def download_images(n, dir):
    async with aiohttp.ClientSession() as session:
        for i in range(n):
            async with session.get("https://picsum.photos/256") as response:
                path = f"{dir}/img_{i}.jpg"
                async with aiofiles.open(path, "wb") as file:
                    await file.write(await response.read())
            


@click.command()
@click.option('-n', '--number', default=1, type=int)
@click.option('-o', '--out', default="./artifacts")
def main(number, out):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_images(number, out))

if __name__ == "__main__":
    main()