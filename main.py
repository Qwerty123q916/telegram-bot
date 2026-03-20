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
        "1": "✨ Toshkent uchun Шахарни энг тоза ва ишончли салондаридан бири

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

Ёш гозал кизларни ишга оламиз ёш чегараси 18-30.",
        "2": "✨ Toshkent uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Toshkent uchun 3-matningiz shu yerga yoziladi.",
    },
    "Samarqand": {
        "1": "✨ Samarqand uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Samarqand uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Samarqand uchun 3-matningiz shu yerga yoziladi.",
    },
    "Buxoro": {
        "1": "✨ Buxoro uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Buxoro uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Buxoro uchun 3-matningiz shu yerga yoziladi.",
    },
    "Farg‘ona": {
        "1": "✨ Farg‘ona uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Farg‘ona uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Farg‘ona uchun 3-matningiz shu yerga yoziladi.",
    },
    "Andijon": {
        "1": "✨ Andijon uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Andijon uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Andijon uchun 3-matningiz shu yerga yoziladi.",
    },
    "Namangan": {
        "1": "✨ Namangan uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Namangan uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Namangan uchun 3-matningiz shu yerga yoziladi.",
    },
    "Qashqadaryo": {
        "1": "✨ Qashqadaryo uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Qashqadaryo uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Qashqadaryo uchun 3-matningiz shu yerga yoziladi.",
    },
    "Surxondaryo": {
        "1": "✨ Surxondaryo uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Surxondaryo uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Surxondaryo uchun 3-matningiz shu yerga yoziladi.",
    },
    "Navoiy": {
        "1": "✨ Navoiy uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Navoiy uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Navoiy uchun 3-matningiz shu yerga yoziladi.",
    },
    "Sirdaryo": {
        "1": "✨ Sirdaryo uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Sirdaryo uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Sirdaryo uchun 3-matningiz shu yerga yoziladi.",
    },
    "Jizzax": {
        "1": "✨ Jizzax uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Jizzax uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Jizzax uchun 3-matningiz shu yerga yoziladi.",
    },
    "Xorazm": {
        "1": "✨ Xorazm uchun 1-matningiz shu yerga yoziladi.",
        "2": "✨ Xorazm uchun 2-matningiz shu yerga yoziladi.",
        "3": "✨ Xorazm uchun 3-matningiz shu yerga yoziladi.",
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
            [KeyboardButton(text="✅ 1-variant"), KeyboardButton(text="✅ 2-variant")],
            [KeyboardButton(text="✅ 3-variant"), KeyboardButton(text="⬅️ Orqaga")],
        ],
        resize_keyboard=True
    )

@dp.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    welcome_text = (
        "🌟 Assalomu alaykum!\n\n"
        "📍 Kerakli viloyatni tanlang.\n"
        "🖼 Sizga rasmlar va variantlar ko‘rsatiladi."
    )
    await message.answer(welcome_text, reply_markup=region_keyboard())

@dp.message(F.text.in_(regions))
async def region_handler(message: Message):
    region = message.text
    user_region[message.from_user.id] = region

    title_text = f"📍 {region}\n\n🖼 Quyidagi variantlar bilan tanishing:"
    await message.answer(title_text)

    photos = region_photos.get(region, [])
    texts = region_texts.get(region, {})

    if photos:
        for i, photo in enumerate(photos, start=1):
            caption_text = texts.get(str(i), f"{region} uchun {i}-variant")
            await message.answer_photo(
                photo=photo,
                caption=caption_text
            )
    else:
        await message.answer(f"⚠️ {region} uchun rasm hali qo‘shilmagan.")

    await message.answer(
        "👇 Kerakli variantni tanlang:",
        reply_markup=variant_keyboard()
    )

@dp.message(F.text == "⬅️ Orqaga")
async def back_handler(message: Message):
    await message.answer(
        "📍 Viloyatni tanlang:",
        reply_markup=region_keyboard()
    )

@dp.message(F.text.in_(["✅ 1-variant", "✅ 2-variant", "✅ 3-variant"]))
async def variant_handler(message: Message):
    region = user_region.get(message.from_user.id)

    if not region:
        await message.answer(
            "❗ Avval viloyatni tanlang.",
            reply_markup=region_keyboard()
        )
        return

    variant_map = {
        "✅ 1-variant": "1",
        "✅ 2-variant": "2",
        "✅ 3-variant": "3",
    }

    selected_variant = variant_map[message.text]
    text = region_texts.get(region, {}).get(selected_variant, "Matn topilmadi.")

    final_text = (
        f"✅ Tanlangan viloyat: {region}\n"
        f"✅ Tanlangan variant: {selected_variant}\n\n"
        f"{text}"
    )

    await message.answer(final_text, reply_markup=variant_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
