from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

inline_button_accept = InlineKeyboardButton('купить', callback_data='подтвердить')
inline_button_cancel = InlineKeyboardButton('отмена', callback_data='отмена')
inline_kb = InlineKeyboardMarkup()
inline_kb.add(inline_button_cancel, inline_button_accept)
