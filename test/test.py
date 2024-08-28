import sys
sys.path.append('../')

from enkanetwork import EnkaNetworkAPI, Language
import asyncio

async def main():
    client = EnkaNetworkAPI(lang=Language.JP)
    resp = await client.fetch_user_by_uid(800857830)
    print(resp.player.tower_act)
    print("fetch user OK")
    await client.fetch_user_by_username("tankload")
    print("fetch hoyos OK")

asyncio.run(main())