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
    "Toshkent": {
        "1": "Toshkent 1-variant matni",
        "2": "Toshkent 2-variant matni",
        "3": "Toshkent 3-variant matni",
    },
    "Samarqand": {
        "1": "Samarqand 1-variant matni",
        "2": "Samarqand 2-variant matni",
        "3": "Samarqand 3-variant matni",
    },
    "Buxoro": {
        "1": "Buxoro 1-variant matni",
        "2": "Buxoro 2-variant matni",
        "3": "Buxoro 3-variant matni",
    },
    "Farg‘ona": {
        "1": "Farg‘ona 1-variant matni",
        "2": "Farg‘ona 2-variant matni",
        "3": "Farg‘ona 3-variant matni",
    },
    "Andijon": {
        "1": "Andijon 1-variant matni",
        "2": "Andijon 2-variant matni",
        "3": "Andijon 3-variant matni",
    },
    "Namangan": {
        "1": "Namangan 1-variant matni",
        "2": "Namangan 2-variant matni",
        "3": "Namangan 3-variant matni",
    },
    "Qashqadaryo": {
        "1": "Qashqadaryo 1-variant matni",
        "2": "Qashqadaryo 2-variant matni",
        "3": "Qashqadaryo 3-variant matni",
    },
    "Surxondaryo": {
        "1": "Surxondaryo 1-variant matni",
        "2": "Surxondaryo 2-variant matni",
        "3": "Surxondaryo 3-variant matni",
    },
    "Navoiy": {
        "1": "Navoiy 1-variant matni",
        "2": "Navoiy 2-variant matni",
        "3": "Navoiy 3-variant matni",
    },
    "Sirdaryo": {
        "1": "Sirdaryo 1-variant matni",
        "2": "Sirdaryo 2-variant matni",
        "3": "Sirdaryo 3-variant matni",
    },
    "Jizzax": {
        "1": "Jizzax 1-variant matni",
        "2": "Jizzax 2-variant matni",
        "3": "Jizzax 3-variant matni",
    },
    "Xorazm": {
        "1": "Xorazm 1-variant matni",
        "2": "Xorazm 2-variant matni",
        "3": "Xorazm 3-variant matni",
    },
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
        for i, photo in enumerate(photos, start=1):
            if i == 3:
                await message.answer_photo(
                    photo=photo,
                    caption=common_text
                )
            else:
                await message.answer_photo(photo=photo)

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
