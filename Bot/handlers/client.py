from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from Bot.app import dp, bot
from Bot.backend.datafetcher import get, list_product
from Bot.handlers.FsmProduct import ProductState
from Bot.keyboards.client_kb import inline_kb


async def start(message: types.Message):
    await bot.send_message(message.from_user.id, f'Привет {message.from_user.first_name}!\n'
                                                 f'Вот команды которые у нас есть: \n'
                                                 f'/info : Инфорация об онлайн магазине \n'
                                                 f'/random : Выводит рандомный товар из магазина \n'
                                                 f'/products : Выводит все продукты которые у нас есть \n', )


async def random_product(message: types.Message, state: FSMContext):
    res = await get()
    async with state.proxy() as data:
        data['title'] = res.get('title')
        data['descriptions'] = res.get('descriptions')
        data['price'] = res.get('price')
        await message.reply(f'Название: {data["title"]}\n'
                            f'Описание товара: {data["descriptions"]}\n'
                            f'Цена: {data["price"]}', reply_markup=inline_kb)


async def products(message: types.Message, state: FSMContext):
    res = await list_product()
    async with state.proxy() as data:
        if isinstance(res, list):
            products = res
            data['products'] = products
            for product in products:
                product_name = product.get('title', 'Нет названия')
                product_descriptions = product.get('descriptions', 'Нет описание')
                product_price = product.get('price', 'Нет цены')
                await message.reply(f'Название продукта: {product_name}\n'
                                    f'Описание продукта: {product_descriptions}\n'
                                    f'Цена: {product_price}', reply_markup=inline_kb)
        else:
            await message.reply('Данные о продуктах не найдены.')


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(random_product, commands=['random'], state=['*'])
    dp.register_message_handler(products, commands=['products'])
