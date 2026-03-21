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
        "AgACAgIAAxkBAAIBrGm-Efnp9taM0Q42hf1DAuWBWfpfAAJyEWsbbw3wSbLvEH35KOTMAQADAgADeAADOgQ",
        "AgACAgIAAxkBAAIBpmm-EZ7wzDBA7M6n8-XfLisX83zGAAJwEWsbbw3wSfJVsSWx1vXEAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBpWm-EZ60wvN8u5H_C9dqWvC5BnJnAAJvEWsbbw3wSYcuoFPvk38bAQADAgADeAADOgQ",
    ],
    "Buxoro": [
        "AgACAgIAAxkBAAIBpGm-EZ5qGMFYLCVegPTu93ECO8GcAAJuEWsbbw3wSbtf6OKst8XVAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBo2m-EZ529U35M_WvjcjgXfnOFTKTAAJtEWsbbw3wSWRlkk_8zpGbAQADAgADeAADOgQ",
        "AgACAgIAAxkBAAIBkGm-EZtrIdy4vP5VoUSadpwbB-jJAAJkEWsbbw3wSXQwptPkqllzAQADAgADeQADOgQ",
    ],
    "Farg‘ona": [
        "AgACAgIAAxkBAAIBmGm-EZvgxqX3KKHD-w3xcwl84TdLAAJsEWsbbw3wSf0x2yJPdkZaAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBlmm-EZt0fzANg5iEfCWim3cnZ7BuAAJqEWsbbw3wSfbCfU97BJUUAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBlGm-EZvU0MVt7X8stuaFe1xuUBACAAJoEWsbbw3wScISI5evoDSYAQADAgADeQADOgQ",
    ],
    "Andijon": [
        "AgACAgIAAxkBAAIBl2m-EZsvxbA90BOvOTTQlbYyr1ywAAJrEWsbbw3wSTs0ywradwABfAEAAwIAA3kAAzoE",
        "AgACAgIAAxkBAAIBlWm-EZuSE2V1eib2BwvIoHWus87rAAJpEWsbbw3wSbmUSSOYO640AQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBj2m-EZvhK3H6QgABdb0Bm6XNUYlgFwACYxFrG28N8En2A7fn1ggidQEAAwIAA3gAAzoE",
    ],
    "Namangan": [
        "AgACAgIAAxkBAAIBk2m-EZvz7nlsjd4YaWdfEpUFiwR9AAJnEWsbbw3wSd9Ik2fwfK5mAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBkmm-EZtu7JlRiaEAAZZ9HV3UbkLNUgACZhFrG28N8EmNoqaXn4vf6wEAAwIAA3gAAzoE",
        "AgACAgIAAxkBAAIBkWm-EZsh5mI4FvkzZwE0Cgh9qBDOAAJlEWsbbw3wSYEtyBflQyQEAQADAgADeQADOgQ",
    ],
    "Qashqadaryo": [
        "AgACAgIAAxkBAAIBg2m-EGPz9GkkCVfGBx3f8UYViB3UAAJeEWsbbw3wSUCogyO7ORoIAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBfWm-EGOq_UDG74wWuEEnUwNQPBniAAJYEWsbbw3wSeGoHl5V8neqAQADAgADeAADOgQ",
        "AgACAgIAAxkBAAIBfmm-EGP-Bw8-5zIFTQ-9kelWw_j2AAJZEWsbbw3wSbme3dPYdlKMAQADAgADeAADOgQ",
    ],
    "Surxondaryo": [
        "AgACAgIAAxkBAAIBhGm-EGPwZZiAzcH1ywsfrPChHYm1AAJfEWsbbw3wSS3A6o5MAQ69AQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBgmm-EGOldql8L2Roec2QS938TsOZAAJdEWsbbw3wSWyzgaAm8KB8AQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBgGm-EGM7y74tDbCWJP7hukET6Qe_AAJbEWsbbw3wSbPOY-c-GLFqAQADAgADeQADOgQ",
    ],
    "Navoiy": [
        "AgACAgIAAxkBAAIBgWm-EGPwBWXJZtQgCQzeU-23-rypAAJcEWsbbw3wSX6gI2plsJoaAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBf2m-EGNYJCS9jepX2NQ1j-f_qbDUAAJaEWsbbw3wST-DEhvMXZqQAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBb2m-EFxxiPD8wYlRsFlCai4hrYloAAJUEWsbbw3wSfK6Oz2JlaXnAQADAgADeQADOgQ",
    ],
    "Sirdaryo": [
        "AgACAgIAAxkBAAIBcWm-EFxRKup3r0u8xwteFwk_IvmNAAJWEWsbbw3wSQXxZMRqegJ_AQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBcGm-EFywXyGzrDLTUKBsGu3z58k5AAJVEWsbbw3wSYU7_z9fkUMqAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBa2m-EFwKFO83WBQwN_0uZh1V002eAAJQEWsbbw3wSfa1CcZ6p9wYAQADAgADeAADOgQ",
    ],
    "Jizzax": [
        "AgACAgIAAxkBAAIBhWm-EGMInyvel6fDOSvb-UtZ3NQ2AAJgEWsbbw3wSUx0sPKwfsUeAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBamm-EFzLmFiX_mPJpMI3rS4nxSxfAAJPEWsbbw3wSXbfnxNiaMksAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAIBbWm-EFxXwVqZ-zZGhMZwdalbLg17AAJSEWsbbw3wSUo1m_6JujirAQADAgADeQADOgQ",
    ],
    "Xorazm": [
        "AgACAgIAAxkBAAICGGm-KEaMT6YDQ_1B53wv_eQj4QSpAAKrEWsbbw3wSaax7utFyQ8nAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAICFmm-KEYhyg1AgZyNk_NcWiVT_VRpAAKpEWsbbw3wSYUIYXUvL4hTAQADAgADeQADOgQ",
        "AgACAgIAAxkBAAICHGm-KFpcOTw3yCl7FbIyZ0ODIU3sAAKsEWsbbw3wSbQZSsGipScaAQADAgADeQADOgQ",
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
