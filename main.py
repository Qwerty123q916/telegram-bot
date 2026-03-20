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
        "TOSHKENT_1_FILE_ID",
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
        "1": """Шахардаги ишончли ва қулай хизматлардан бири.

ФОТОЛАР РЕАЛ

Хизмат турлари:
1) Классик
2) Релакс
3) Соғломлаштирувчи
4) Спорт
5) Микс 2/1
6) Микс 3/1
7) Микс 4/1
8) Умумий
9) Универсал

Тиллар: Русский, туркча, қозоқча

Тўғри танлов қилинг!""",
        "2": "Бу ерга Тошкент учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Тошкент учун 3-вариант матнини ёзинг",
    },
    "Samarqand": {
        "1": "Бу ерга Самарқанд учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Самарқанд учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Самарқанд учун 3-вариант матнини ёзинг",
    },
    "Buxoro": {
        "1": "Бу ерга Бухоро учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Бухоро учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Бухоро учун 3-вариант матнини ёзинг",
    },
    "Farg‘ona": {
        "1": "Бу ерга Фарғона учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Фарғона uchun 2-вариант матнини ёзинг",
        "3": "Бу ерга Фарғона учун 3-вариант матнини ёзинг",
    },
    "Andijon": {
        "1": "Бу ерга Андижон учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Андижон учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Андижон учун 3-вариант матнини ёзинг",
    },
    "Namangan": {
        "1": "Бу ерга Наманган учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Наманган учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Наманган учун 3-вариант матнини ёзинг",
    },
    "Qashqadaryo": {
        "1": "Бу ерга Қашқадарё учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Қашқадарё учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Қашқадарё учун 3-вариант матнини ёзинг",
    },
    "Surxondaryo": {
        "1": "Бу ерга Сурхондарё учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Сурхондарё учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Сурхондарё учун 3-вариант матнини ёзинг",
    },
    "Navoiy": {
        "1": "Бу ерга Навоий учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Навоий учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Навоий учун 3-вариант матнини ёзинг",
    },
    "Sirdaryo": {
        "1": "Бу ерга Сирдарё учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Сирдарё учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Сирдарё учун 3-вариант матнини ёзинг",
    },
    "Jizzax": {
        "1": "Бу ерга Жиззах учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Жиззах учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Жиззах учун 3-вариант матнини ёзинг",
    },
    "Xorazm": {
        "1": "Бу ерга Хоразм учун 1-вариант матнини ёзинг",
        "2": "Бу ерга Хоразм учун 2-вариант матнини ёзинг",
        "3": "Бу ерга Хоразм учун 3-вариант матнини ёзинг",
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
    await message.answer(
        "🌟 Ассалому алайкум!\n\n📍 Вилоятни танланг:",
        reply_markup=region_keyboard()
    )

@dp.message(F.text.in_(regions))
async def region_handler(message: Message):
    region = message.text
    user_region[message.from_user.id] = region

    photos = region_photos.get(region, [])
    texts = region_texts.get(region, {})

    if photos:
        for i, photo in enumerate(photos, start=1):
            caption_text = texts.get(str(i), f"{region} учун {i}-вариант")
            await message.answer_photo(
                photo=photo,
                caption=caption_text
            )
    else:
        await message.answer(f"{region} учун расм ҳали қўшилмаган.")

    await message.answer(
        "👇 Керакли вариантни танланг:",
        reply_markup=variant_keyboard()
    )

@dp.message(F.text == "⬅️ Orqaga")
async def back_handler(message: Message):
    await message.answer(
        "📍 Вилоятни танланг:",
        reply_markup=region_keyboard()
    )

@dp.message(F.text.in_(["✅ 1-variant", "✅ 2-variant", "✅ 3-variant"]))
async def variant_handler(message: Message):
    region = user_region.get(message.from_user.id)

    if not region:
        await message.answer(
            "❗ Аввал вилоятни танланг.",
            reply_markup=region_keyboard()
        )
        return

    variant_map = {
        "✅ 1-variant": "1",
        "✅ 2-variant": "2",
        "✅ 3-variant": "3",
    }

    selected_variant = variant_map[message.text]
    text = region_texts.get(region, {}).get(selected_variant, "Матн топилмади.")

    await message.answer(text, reply_markup=variant_keyboard())

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
