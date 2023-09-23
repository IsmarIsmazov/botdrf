import aiohttp
from .API import PRODUCT_API_URL_RANDOM, PRODUCT_API_URL_LIST


async def get():
    async with aiohttp.ClientSession() as sessions:
        async with sessions.get(PRODUCT_API_URL_RANDOM) as response:
            return await response.json()


async def list_product():
    async with aiohttp.ClientSession() as sessions:
        async with sessions.get(PRODUCT_API_URL_LIST) as response:
            return await response.json()
