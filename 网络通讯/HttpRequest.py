import aiohttp
import asyncio


class HttpRequest:
    def __init__(self, url):
        self.url = url

    async def http_client_request(self):
        async with aiohttp.ClientSession() as session:
            async with session.get(url=self.url) as respond:
                self.status = respond.status
                self.content = await respond.text(encoding='utf-8')


if __name__ == "__main__":
    client = HttpRequest('http://python.org')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(client.http_client_request())
    print(client.status)
    print(client.content)
