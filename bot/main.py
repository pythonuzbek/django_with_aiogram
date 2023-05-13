import os

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv
import logging
from bot.api import get_category, get_product, add_user, create_category, create_product
from bot.buttons import ikm, get_button, post_button
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

load_dotenv()
logging.basicConfig(level=logging.INFO)
token = os.getenv('TG_TOKEN')
bot = Bot(token)

storage = MemoryStorage()

dp = Dispatcher(bot, storage=storage)


class AddCategory(StatesGroup):
    name = State()


class UpdateCategory(StatesGroup):
    name = State()


class AddProduct(StatesGroup):
    name = State()
    description = State()
    category = State()


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Welcome My Bot')
    await message.answer('select one', reply_markup=ikm)


@dp.callback_query_handler(lambda msg: msg.data == '11')
async def get_method(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.from_user.id, message.message.message_id, reply_markup=get_button)


@dp.callback_query_handler(lambda msg: msg.data == '12')
async def post_method(message: types.CallbackQuery):
    await bot.edit_message_reply_markup(message.from_user.id, message.message.message_id, reply_markup=post_button)




@dp.callback_query_handler()
async def get(message: types.CallbackQuery):
    if message.data == '1':
        for i in get_category():
            result = {
                'id': i['id'],
                'name': i['name'],
            }
            for k, v in result.items():
                await bot.send_message(message.from_user.id, f'{k} : {v}')

    elif message.data == '2':
        data = get_product()
        for i in data:
            await bot.send_message(message.from_user.id, i)
    elif message.data == '3':
        await bot.send_message(message.from_user.id, add_user(message.from_user.id,
                                                              message.from_user.first_name,
                                                              message.from_user.username))

    elif message.data == '4':
        await AddCategory.name.set()
        await bot.send_message(message.from_user.id, 'enter name of category')

    elif message.data == '5':
        await AddProduct.name.set()
        await bot.send_message(message.from_user.id, 'enter name of product')

    elif message.data == '17':
        await UpdateCategory.name.set()
        await bot.send_message(message.from_user.id, 'enter name of category')


@dp.message_handler(state=AddCategory.name)
async def add_category(message: types.Message, state=FSMContext):
    await state.update_data(name=message.text)
    await bot.send_message(message.from_user.id, create_category(message.text))

    await state.finish()




@dp.message_handler(state=AddProduct.name)
async def add_product(message: types.Message, state=FSMContext):
    await state.update_data(name=message.text)
    await AddProduct.next()
    await message.answer('enter description of the product')


@dp.message_handler(state=AddProduct.description)
async def add_product(message: types.Message, state=FSMContext):
    await state.update_data(description=message.text)
    await AddProduct.next()
    rkm = InlineKeyboardMarkup()
    data = []
    for i in get_category():
        result = {
            'id': i['id'],
            'name': i['name']
        }
        rkm.add(InlineKeyboardButton(result['name'], callback_data=result['id']))
    await message.answer('enter category of the product', reply_markup=rkm)


@dp.callback_query_handler(state=AddProduct.category)
async def add_category(message: types.CallbackQuery, state=FSMContext):
    async with state.proxy() as data:
        data['category'] = message.data
        await bot.send_message(message.from_user.id,
                               create_product(name=data['name'],
                                              description=data['description'],
                                              category=data['category']))
    await state.finish()


executor.start_polling(dp, skip_updates=True)
