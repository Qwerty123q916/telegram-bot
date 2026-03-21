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
    "Samarqand": [
        "PHOTO_ID_SAMARQAND_1",
        "PHOTO_ID_SAMARQAND_2",
        "PHOTO_ID_SAMARQAND_3",
    ],
    "Buxoro": [
        "PHOTO_ID_BUXORO_1",
        "PHOTO_ID_BUXORO_2",
        "PHOTO_ID_BUXORO_3",
    ],
    "Farg‘ona": [
        "PHOTO_ID_FARGONA_1",
        "PHOTO_ID_FARGONA_2",
        "PHOTO_ID_FARGONA_3",
    ],
    "Andijon": [
        "PHOTO_ID_ANDIJON_1",
        "PHOTO_ID_ANDIJON_2",
        "PHOTO_ID_ANDIJON_3",
    ],
    "Namangan": [
        "PHOTO_ID_NAMANGAN_1",
        "PHOTO_ID_NAMANGAN_2",
        "PHOTO_ID_NAMANGAN_3",
    ],
    "Qashqadaryo": [
        "PHOTO_ID_QASHQADARYO_1",
        "PHOTO_ID_QASHQADARYO_2",
        "PHOTO_ID_QASHQADARYO_3",
    ],
    "Surxondaryo": [
        "PHOTO_ID_SURXONDARYO_1",
        "PHOTO_ID_SURXONDARYO_2",
        "PHOTO_ID_SURXONDARYO_3",
    ],
    "Navoiy": [
        "PHOTO_ID_NAVOIY_1",
        "PHOTO_ID_NAVOIY_2",
        "PHOTO_ID_NAVOIY_3",
    ],
    "Sirdaryo": [
        "PHOTO_ID_SIRDARYO_1",
        "PHOTO_ID_SIRDARYO_2",
        "PHOTO_ID_SIRDARYO_3",
    ],
    "Jizzax": [
        "PHOTO_ID_JIZZAX_1",
        "PHOTO_ID_JIZZAX_2",
        "PHOTO_ID_JIZZAX_3",
    ],
    "Xorazm": [
        "PHOTO_ID_XORAZM_1",
        "PHOTO_ID_XORAZM_2",
        "PHOTO_ID_XORAZM_3",
    ],
}

region_texts = {
    "Toshkent": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Samarqand": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Buxoro": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Farg‘ona": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Andijon": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Namangan": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Qashqadaryo": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Surxondaryo": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Navoiy": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Sirdaryo": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Jizzax": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
    "Xorazm": {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"},
}

confirm_texts = {
    "Toshkent": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Samarqand": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Buxoro": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Farg‘ona": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Andijon": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Namangan": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Qashqadaryo": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Surxondaryo": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Navoiy": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Sirdaryo": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Jizzax": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
    "Xorazm": {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"},
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
            await message.answer_photo(photo=photo, caption=common_text)
    else:
        await message.answer("Бу вилоят учун ҳозирча расм қўйилмаган.")

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

    text = confirm_texts.get(region, {}).get(variant, "❌XATOLIK❌")
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
