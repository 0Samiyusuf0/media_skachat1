import requests
from aiogram import Bot, Router, types
from aiogram.filters import CommandStart, Command
from data.config import GROUP_USERNAME, GROUP_USERNAME2,ADMINS
from keyboard.inline.member_group import subscribe_ikm

router = Router()

API_KEY = "bb2e134333b0372b457c0b73"
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/UZS"

response = requests.get(url=url)
result = response.json()
kurs = result['conversion_rate']

async def check_subscription(user_id, bot: Bot):
    member = await bot.get_chat_member(chat_id=GROUP_USERNAME, user_id=user_id)
    return member.status in ['member', 'administration', 'creator']



@router.message(CommandStart())
async def bot_start(message: types.Message, bot: Bot):
    user_id = message.from_user.id
    is_subscribed = await check_subscription(user_id, bot)

    if is_subscribed:
        await message.answer("Botdan foydalanishingiz mumkin!")
    else:
        await message.answer(f"Salom {message.from_user.full_name}")
        await message.answer(text="Botdan foydalanishingiz uchun guruhga a'zo bo'ling!",
                             reply_markup=subscribe_ikm())



@router.message(Command("dollar"))
async def send_start(message: types.Message):
    await message.answer(text=f"Bugungi dollar kursi {kurs} so'm")
