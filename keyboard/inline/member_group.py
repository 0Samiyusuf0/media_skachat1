from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data.config import *


def subscribe_ikm():
    button = InlineKeyboardButton(text="Guruhga obuna bo'lish", url=f"https://t.me/{GROUP_USERNAME.strip('@')}")
    button1 = InlineKeyboardButton(text="Guruhga obuna bo'lish", url=f"https://t.me/{GROUP_USERNAME2.strip('@')}")
    button2 = InlineKeyboardButton(text="Guruhga obuna bo'lish", url=f"https://t.me/{GROUP_USERNAME3.strip('@')}")
    button3 = InlineKeyboardButton(text="Guruhga obuna bo'lish", url=f"https://t.me/{GROUP_USERNAME4.strip('@')}")
    button4 = InlineKeyboardButton(text="Tekshirish☑️", callback_data="tekshirish")

    ikm = InlineKeyboardMarkup(
        inline_keyboard=[
            [button],
            [button1],
            [button2],
            [button3],
            [button4]
        ])

    return ikm
