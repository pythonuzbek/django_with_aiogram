from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.api import get_category

ikm = InlineKeyboardMarkup()
ikm = ikm.add(InlineKeyboardButton('Get', callback_data='11'),
              InlineKeyboardButton('Post', callback_data='12'))

get = InlineKeyboardMarkup()
get_button = get.add(InlineKeyboardButton('Get Categories', callback_data='1'),
                     InlineKeyboardButton('Get Products', callback_data='2'))

post = InlineKeyboardMarkup()
post_button = post.add(InlineKeyboardButton('Add User', callback_data='3'),
                       InlineKeyboardButton('Add Category', callback_data='4'),
                       InlineKeyboardButton('Add Product', callback_data='5'))


