import asyncio
from pyrogram import Client

api_id = "20368885"
api_hash = "1d499a8be7aad4553d3c2395829292c6"
bot = "8225602323:AAFF0R9Pju3jRaEuWC4n_jyj18VWdb-veZU"

async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")

        

asyncio.run(main())
