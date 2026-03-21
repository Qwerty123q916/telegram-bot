import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN topilmadi")

bot = Bot(token=TOKEN)
dp = Dispatcher()

regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo",
    "Navoiy", "Sirdaryo", "Jizzax", "Xorazm"
]

common_text = """🌟 Шаҳардаги ишончли ва қулай хизматлардан бири

📸 ФОТОЛАР РЕАЛ

📋 Хизмат турлари:
1) Классик
2) Релакс
3) Соғломлаштирувчи
4) Спорт
5) Микс 2/1
6) Микс 3/1
7) Микс 4/1
8) Умумий
9) Универсал

🗣 Тиллар: Русский, туркча, қозоқча

✅ Тўғри танлов қилинг!"""

region_photos = {
    "Toshkent": [
        "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA",
        "AgACAgIAAxkBAAIBrGm-Efnp9taM0Q42hf1DAuWBWfpfAAJyEWsbbw3wSbLvEH35KOTMAQADAgADeAADOgQ",
        "AgACAgIAAxkBAAIBq2m-EfnoBq_SJwQAAZzf3AsXYfTPxQACcRFrG28N8EkBNxAWKHNUKQEAAwIAA3gAAzoE",
    ],
    "Samarqand": [],
    "Buxoro": [],
    "Farg‘ona": [],
    "Andijon": [],
    "Namangan": [],
    "Qashqadaryo": [],
    "Surxondaryo": [],
    "Navoiy": [],
    "Sirdaryo": [],
    "Jizzax": [],
    "Xorazm": [],
}

region_texts = {
    "Toshkent": {
        "1": "1-variant matni",
        "2": "2-variant matni",
        "3": "3-variant matni",
    }
}

confirm_texts = {
    "Toshkent": {
        "1": "✅ Қабул қилинди.",
        "2": "✅ Қабул қилинди.",
        "3": "✅ Қабул қилинди.",
    }
}

user_region = {}
user_variant = {}

def region_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Toshkent"), KeyboardButton(text="Samarqand")],
            [KeyboardButton(text="Buxoro"), KeyboardButton(text="Farg‘ona")],
            [KeyboardButton(text="Andijon"), KeyboardButton(text="Namangan")],
            [KeyboardButton(text="Qashqadaryo"), KeyboardButton(text="Surxondaryo")],
            [KeyboardButton(text="Navoiy"), KeyboardButton(text="Sirdaryo")],
            [KeyboardButton(text="Jizzax"), KeyboardButton(text="Xorazm")],
        ],
        resize_keyboard=True
    )

def variant_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
            [KeyboardButton(text="⬅️ Orqaga")],
        ],
        resize_keyboard=True
    )

def confirm_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ O‘tkazdim")],
            [KeyboardButton(text="⬅️ Orqaga")],
        ],
        resize_keyboard=True
    )

@dp.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    user_region.pop(message.from_user.id, None)
    user_variant.pop(message.from_user.id, None)
    await message.answer("📍 Вилоятни танланг:", reply_markup=region_keyboard())

@dp.message(F.text.in_(regions))
async def region_handler(message: Message):
    region = message.text
    user_region[message.from_user.id] = region
    user_variant.pop(message.from_user.id, None)

    photos = region_photos.get(region, [])

    if photos:
        for photo in photos:
            await message.answer_photo(
                photo=photo,
                caption=common_text
            )

    await message.answer("👇 Керакли вариантни танланг:", reply_markup=variant_keyboard())

@dp.message(F.text.in_(["1", "2", "3"]))
async def variant_handler(message: Message):
    region = user_region.get(message.from_user.id)
    if not region:
        await message.answer("Аввал вилоятни танланг.", reply_markup=region_keyboard())
        return

    variant = message.text
    user_variant[message.from_user.id] = variant

    text = region_texts.get(region, {}).get(variant, "Матн топилмади.")
    await message.answer(text, reply_markup=confirm_keyboard())

@dp.message(F.text == "✅ O‘tkazdim")
async def confirm_handler(message: Message):
    region = user_region.get(message.from_user.id)
    variant = user_variant.get(message.from_user.id)

    if not region or not variant:
        await message.answer("Аввал вилоят ва вариантни танланг.", reply_markup=region_keyboard())
        return

    text = confirm_texts.get(region, {}).get(variant, "✅ Қабул қилинди.")
    await message.answer(text, reply_markup=confirm_keyboard())

@dp.message(F.text == "⬅️ Orqaga")
async def back_handler(message: Message):
    user_region.pop(message.from_user.id, None)
    user_variant.pop(message.from_user.id, None)
    await message.answer("📍 Вилоятни танланг:", reply_markup=region_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
