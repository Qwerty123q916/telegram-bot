import asyncio
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo",
    "Xorazm", "Navoiy", "Jizzax", "Sirdaryo"
]

region_photos = {
    "Toshkent": [
        ("AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA", "1-variant"),
        ("AgACAgIAAxkBAANPab2s-Q__7C4HQKR1gzEKj74V84MAApkXaxsfTvFJosNaYYyS1MEBAAMCAAN5AAM6BA", "2-variant"),
        ("TOSHKENT_3_FILE_ID", "3-variant"),
    ],
    "Samarqand": [
        ("SAMARQAND_1_FILE_ID", "1-variant"),
        ("SAMARQAND_2_FILE_ID", "2-variant"),
        ("SAMARQAND_3_FILE_ID", "3-variant"),
    ],
    "Buxoro": [
        ("BUXORO_1_FILE_ID", "1-variant"),
        ("BUXORO_2_FILE_ID", "2-variant"),
        ("BUXORO_3_FILE_ID", "3-variant"),
    ],
    "Farg‘ona": [
        ("FARGONA_1_FILE_ID", "1-variant"),
        ("FARGONA_2_FILE_ID", "2-variant"),
        ("FARGONA_3_FILE_ID", "3-variant"),
    ],
    "Andijon": [
        ("ANDIJON_1_FILE_ID", "1-variant"),
        ("ANDIJON_2_FILE_ID", "2-variant"),
        ("ANDIJON_3_FILE_ID", "3-variant"),
    ],
    "Namangan": [
        ("NAMANGAN_1_FILE_ID", "1-variant"),
        ("NAMANGAN_2_FILE_ID", "2-variant"),
        ("NAMANGAN_3_FILE_ID", "3-variant"),
    ],
    "Qashqadaryo": [
        ("QASHQADARYO_1_FILE_ID", "1-variant"),
        ("QASHQADARYO_2_FILE_ID", "2-variant"),
        ("QASHQADARYO_3_FILE_ID", "3-variant"),
    ],
    "Surxondaryo": [
        ("SURXONDARYO_1_FILE_ID", "1-variant"),
        ("SURXONDARYO_2_FILE_ID", "2-variant"),
        ("SURXONDARYO_3_FILE_ID", "3-variant"),
    ],
    "Xorazm": [
        ("XORAZM_1_FILE_ID", "1-variant"),
        ("XORAZM_2_FILE_ID", "2-variant"),
        ("XORAZM_3_FILE_ID", "3-variant"),
    ],
    "Navoiy": [
        ("NAVOIY_1_FILE_ID", "1-variant"),
        ("NAVOIY_2_FILE_ID", "2-variant"),
        ("NAVOIY_3_FILE_ID", "3-variant"),
    ],
    "Jizzax": [
        ("JIZZAX_1_FILE_ID", "1-variant"),
        ("JIZZAX_2_FILE_ID", "2-variant"),
        ("JIZZAX_3_FILE_ID", "3-variant"),
    ],
    "Sirdaryo": [
        ("SIRDARYO_1_FILE_ID", "1-variant"),
        ("SIRDARYO_2_FILE_ID", "2-variant"),
        ("SIRDARYO_3_FILE_ID", "3-variant"),
    ],
}

region_texts = {
    "Toshkent": {
        "1": "Toshkent uchun 1-variant matni",
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
    "Xorazm": {
        "1": "Xorazm uchun 1-variant matni",
        "2": "Xorazm uchun 2-variant matni",
        "3": "Xorazm uchun 3-variant matni",
    },
    "Navoiy": {
        "1": "Navoiy uchun 1-variant matni",
        "2": "Navoiy uchun 2-variant matni",
        "3": "Navoiy uchun 3-variant matni",
    },
    "Jizzax": {
        "1": "Jizzax uchun 1-variant matni",
        "2": "Jizzax uchun 2-variant matni",
        "3": "Jizzax uchun 3-variant matni",
    },
    "Sirdaryo": {
        "1": "Sirdaryo uchun 1-variant matni",
        "2": "Sirdaryo uchun 2-variant matni",
        "3": "Sirdaryo uchun 3-variant matni",
    },
}

@dp.message(F.photo)
async def get_photo_id(message: Message):
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    builder = InlineKeyboardBuilder()
    for i, region in enumerate(regions):
        builder.button(text=region, callback_data=f"region_{i}")
    builder.adjust(1)
    await message.answer("Viloyatni tanlang:", reply_markup=builder.as_markup())

@dp.callback_query(F.data.startswith("region_"))
async def region_handler(callback: CallbackQuery):
    index = int(callback.data.split("_")[1])
    region = regions[index]

    photos = region_photos.get(region, [])
    for i, (photo, caption) in enumerate(photos, start=1):
        await callback.message.answer_photo(
            photo=photo,
            caption=f"{region}\n{i} - {caption}"
        )

    builder = InlineKeyboardBuilder()
    builder.button(text="1", callback_data=f"text_{index}_1")
    builder.button(text="2", callback_data=f"text_{index}_2")
    builder.button(text="3", callback_data=f"text_{index}_3")
    builder.adjust(3)

    await callback.message.answer("Variantni tanlang:", reply_markup=builder.as_markup())
    await callback.answer()

@dp.callback_query(F.data.startswith("text_"))
async def text_handler(callback: CallbackQuery):
    _, region_index, variant = callback.data.split("_")
    region = regions[int(region_index)]

    text = region_texts.get(region, {}).get(variant, "Matn topilmadi.")
    await callback.message.answer(text)
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
