import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, '..'))
sys.path.append(parent_dir)
# Some CGPT Code

import asyncio

from enkanetwork import EnkaNetworkAPI

client = EnkaNetworkAPI()

async def main():
    async with client:
        await client.update_assets()
        # You can see the progress download new assets in console

asyncio.run(main())