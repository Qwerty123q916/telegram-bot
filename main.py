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

region_photos = {
    "Toshkent": [
        "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA",
        "TOSHKENT_2_FILE_ID",
        "TOSHKENT_3_FILE_ID",
    ],
    "Samarqand": [
        "SAMARQAND_1_FILE_ID",
        "SAMARQAND_2_FILE_ID",
        "SAMARQAND_3_FILE_ID",
    ],
    "Buxoro": [
        "BUXORO_1_FILE_ID",
        "BUXORO_2_FILE_ID",
        "BUXORO_3_FILE_ID",
    ],
    "Farg‘ona": [
        "FARGONA_1_FILE_ID",
        "FARGONA_2_FILE_ID",
        "FARGONA_3_FILE_ID",
    ],
    "Andijon": [
        "ANDIJON_1_FILE_ID",
        "ANDIJON_2_FILE_ID",
        "ANDIJON_3_FILE_ID",
    ],
    "Namangan": [
        "NAMANGAN_1_FILE_ID",
        "NAMANGAN_2_FILE_ID",
        "NAMANGAN_3_FILE_ID",
    ],
    "Qashqadaryo": [
        "QASHQADARYO_1_FILE_ID",
        "QASHQADARYO_2_FILE_ID",
        "QASHQADARYO_3_FILE_ID",
    ],
    "Surxondaryo": [
        "SURXONDARYO_1_FILE_ID",
        "SURXONDARYO_2_FILE_ID",
        "SURXONDARYO_3_FILE_ID",
    ],
    "Navoiy": [
        "NAVOIY_1_FILE_ID",
        "NAVOIY_2_FILE_ID",
        "NAVOIY_3_FILE_ID",
    ],
    "Sirdaryo": [
        "SIRDARYO_1_FILE_ID",
        "SIRDARYO_2_FILE_ID",
        "SIRDARYO_3_FILE_ID",
    ],
    "Jizzax": [
        "JIZZAX_1_FILE_ID",
        "JIZZAX_2_FILE_ID",
        "JIZZAX_3_FILE_ID",
    ],
    "Xorazm": [
        "XORAZM_1_FILE_ID",
        "XORAZM_2_FILE_ID",
        "XORAZM_3_FILE_ID",
    ],
}

region_texts = {
    "Toshkent": {
        "1": "Toshkent uchun 1-variant Шахарни энг тоза ва ишончли салондаридан бири

ФОТО 100% РЕАЛ!!!
     
Массаж нархлари: 800.000-1.800.000 сум

1)Классический 
2)Релакс
3)Оздоровительный 
4)Спортивный 
5)Микс 2/1
6)Микс 3/1
7)Микс 4/1 
8)Общий 
10)Универсальный 
11)Королевский 2 та киз бн😍

Язык: Русский, турецкий, казахискый

Танловда адашманг! 

Ёш гозал кизларни ишга оламиз ёш чегараси 18-30 matni",
        "2": "Toshkent uchun 2-variant matni",
        "3": "Toshkent uchun 3-variant matni",
    },
    "Samarqand": {
        "1": "Samarqand uchun 1-variant matni",
        "2": "Samarqand uchun 2-variant matni",
        "3": "Samarqand uchun 3-variant matni",
    },
    "Buxoro": {
        "1": "Buxoro uchun 1-variant matni",
        "2": "Buxoro uchun 2-variant matni",
        "3": "Buxoro uchun 3-variant matni",
    },
    "Farg‘ona": {
        "1": "Farg‘ona uchun 1-variant matni",
        "2": "Farg‘ona uchun 2-variant matni",
        "3": "Farg‘ona uchun 3-variant matni",
    },
    "Andijon": {
        "1": "Andijon uchun 1-variant matni",
        "2": "Andijon uchun 2-variant matni",
        "3": "Andijon uchun 3-variant matni",
    },
    "Namangan": {
        "1": "Namangan uchun 1-variant matni",
        "2": "Namangan uchun 2-variant matni",
        "3": "Namangan uchun 3-variant matni",
    },
    "Qashqadaryo": {
        "1": "Qashqadaryo uchun 1-variant matni",
        "2": "Qashqadaryo uchun 2-variant matni",
        "3": "Qashqadaryo uchun 3-variant matni",
    },
    "Surxondaryo": {
        "1": "Surxondaryo uchun 1-variant matni",
        "2": "Surxondaryo uchun 2-variant matni",
        "3": "Surxondaryo uchun 3-variant matni",
    },
    "Navoiy": {
        "1": "Navoiy uchun 1-variant matni",
        "2": "Navoiy uchun 2-variant matni",
        "3": "Navoiy uchun 3-variant matni",
    },
    "Sirdaryo": {
        "1": "Sirdaryo uchun 1-variant matni",
        "2": "Sirdaryo uchun 2-variant matni",
        "3": "Sirdaryo uchun 3-variant matni",
    },
    "Jizzax": {
        "1": "Jizzax uchun 1-variant matni",
        "2": "Jizzax uchun 2-variant matni",
        "3": "Jizzax uchun 3-variant matni",
    },
    "Xorazm": {
        "1": "Xorazm uchun 1-variant matni",
        "2": "Xorazm uchun 2-variant matni",
        "3": "Xorazm uchun 3-variant matni",
    },
}

user_region = {}

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
            [KeyboardButton(text="1"), KeyboardButton(text="2")],
            [KeyboardButton(text="3"), KeyboardButton(text="⬅️ Orqaga")],
        ],
        resize_keyboard=True
    )

@dp.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    await message.answer("Viloyatni tanlang:", reply_markup=region_keyboard())

@dp.message(F.text.in_(regions))
async def region_handler(message: Message):
    region = message.text
    user_region[message.from_user.id] = region

    photos = region_photos.get(region, [])
    if photos:
        for i, photo in enumerate(photos, start=1):
            await message.answer_photo(
                photo=photo,
                caption=f"{region}\n{i}-variant"
            )
    else:
        await message.answer(f"{region} uchun rasm hali qo‘shilmagan.")

    await message.answer("Variantni tanlang:", reply_markup=variant_keyboard())

@dp.message(F.text == "⬅️ Orqaga")
async def back_handler(message: Message):
    await message.answer("Viloyatni tanlang:", reply_markup=region_keyboard())

@dp.message(F.text.in_(["1", "2", "3"]))
async def variant_handler(message: Message):
    region = user_region.get(message.from_user.id)

    if not region:
        await message.answer("Avval viloyatni tanlang.", reply_markup=region_keyboard())
        return

    text = region_texts.get(region, {}).get(message.text, "Matn topilmadi.")
    await message.answer(text, reply_markup=variant_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
