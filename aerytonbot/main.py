import asyncio
from pyrogram import Client

api_id = "20368885"
api_hash = "1d499a8be7aad4553d3c2395829292c6"
bot = "8225602323:AAFF0R9Pju3jRaEuWC4n_jyj18VWdb-veZU"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

        

asyncio.run(main())
ERROR: Could not install packages due to an OSError: HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Max retries exceeded with url: /packages/de/f0/c81e05b613866b76d2d1066490adf1a3dbc4ee9d9c839961c3fc8a6997af/pip-26.0.1-py3-none-any.whl.metadata (Caused by ReadTimeoutError("HTTPSConnectionPool(host='files.pythonhosted.org', port=443): Read timed out. (read timeout=15)"))
