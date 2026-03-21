import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo",
    "Navoiy", "Sirdaryo", "Jizzax", "Xorazm"
]

common_text = """📸 ФОТОЛАР РЕАЛ

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

🗣 Тиллар: Русский, Узбекча

✅ Тўғри танлов қилинг!"""

region_photos = {
    "Toshkent": [
        "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA",
        "PHOTO_ID_2",
        "PHOTO_ID_3",
    ],
    "Samarqand": [
        "PHOTO_ID_4",
        "PHOTO_ID_5",
        "PHOTO_ID_6",
    ],
    "Buxoro": [
        "PHOTO_ID_7",
        "PHOTO_ID_8",
        "PHOTO_ID_9",
    ],
    "Farg‘ona": [
        "PHOTO_ID_10",
        "PHOTO_ID_11",
        "PHOTO_ID_12",
    ],
    "Andijon": [
        "PHOTO_ID_13",
        "PHOTO_ID_14",
        "PHOTO_ID_15",
    ],
    "Namangan": [
        "PHOTO_ID_16",
        "PHOTO_ID_17",
        "PHOTO_ID_18",
    ],
    "Qashqadaryo": [
        "PHOTO_ID_19",
        "PHOTO_ID_20",
        "PHOTO_ID_21",
    ],
    "Surxondaryo": [
        "PHOTO_ID_22",
        "PHOTO_ID_23",
        "PHOTO_ID_24",
    ],
    "Navoiy": [
        "PHOTO_ID_25",
        "PHOTO_ID_26",
        "PHOTO_ID_27",
    ],
    "Sirdaryo": [
        "PHOTO_ID_28",
        "PHOTO_ID_29",
        "PHOTO_ID_30",
    ],
    "Jizzax": [
        "PHOTO_ID_31",
        "PHOTO_ID_32",
        "PHOTO_ID_33",
    ],
    "Xorazm": [
        "PHOTO_ID_34",
        "PHOTO_ID_35",
        "PHOTO_ID_36",
    ],
}

region_texts = {
    "Toshkent": {"1": common_text, "2": common_text, "3": common_text},
    "Samarqand": {"1": common_text, "2": common_text, "3": common_text},
    "Buxoro": {"1": common_text, "2": common_text, "3": common_text},
    "Farg‘ona": {"1": common_text, "2": common_text, "3": common_text},
    "Andijon": {"1": common_text, "2": common_text, "3": common_text},
    "Namangan": {"1": common_text, "2": common_text, "3": common_text},
    "Qashqadaryo": {"1": common_text, "2": common_text, "3": common_text},
    "Surxondaryo": {"1": common_text, "2": common_text, "3": common_text},
    "Navoiy": {"1": common_text, "2": common_text, "3": common_text},
    "Sirdaryo": {"1": common_text, "2": common_text, "3": common_text},
    "Jizzax": {"1": common_text, "2": common_text, "3": common_text},
    "Xorazm": {"1": common_text, "2": common_text, "3": common_text},
}

confirm_texts = {
    "Toshkent": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Samarqand": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Buxoro": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Farg‘ona": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Andijon": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Namangan": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Qashqadaryo": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Surxondaryo": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Navoiy": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Sirdaryo": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Jizzax": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
    "Xorazm": {"1": "✅ Қабул қилинди.", "2": "✅ Қабул қилинди.", "3": "✅ Қабул қилинди."},
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
    await message.answer("📍 Вилоятни танланг:", reply_markup=region_keyboard())

@dp.message(F.text.in_(regions))
async def region_handler(message: Message):
    region = message.text
    user_region[message.from_user.id] = region

    photos = region_photos.get(region, [])
    texts = region_texts.get(region, {})

    if photos:
        for i, photo in enumerate(photos, start=1):
            await message.answer_photo(
                photo=photo,
                caption=texts.get(str(i), common_text)
            )

    await message.answer("👇 Керакли вариантни танланг:", reply_markup=variant_keyboard())

@dp.message(F.text.in_(["1", "2", "3"]))
async def variant_handler(message: Message):
    region = user_region.get(message.from_user.id)
    if not region:
        await message.answer("Аввал вилоятни танланг.", reply_markup=region_keyboard())
        return

    user_variant[message.from_user.id] = message.text
    text = region_texts.get(region, {}).get(message.text, common_text)
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
    await message.answer("📍 Вилоятни танланг:", reply_markup=region_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
