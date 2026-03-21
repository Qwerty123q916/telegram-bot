import asyncio
import os
import json
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN topilmadi")

ADMIN_ID = 7890489981
DATA_FILE = "users_data.json"

def is_admin(user_id: int) -> bool:
    return user_id == ADMIN_ID

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"users": {}, "choices": []}
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_user(user):
    data = load_data()
    uid = str(user.id)
    data["users"][uid] = {
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username
    }
    save_data(data)

def save_choice(user, region, variant):
    data = load_data()
    data["choices"].append({
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "region": region,
        "variant": variant
    })
    save_data(data)

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
        "AgACAgEAAxkBAAICgGm-Q7y4yHvzGxic9MNSsUN3iWixAAKuC2sbRQHwRR51XU8MEv5IAQADAgADeQADOgQ",
        "AgACAgEAAxkBAAICtGm-aHQOm97NSa0rDbnTji23swhYAALEC2sbRQHwRTlO_x8vrfyGAQADAgADeQADOgQ",
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

region_texts = {r: {"1": "1-variant matni", "2": "2-variant matni", "3": "3-variant matni"} for r in regions}
confirm_texts = {r: {"1": "❌XATOLIK❌", "2": "❌XATOLIK❌", "3": "❌XATOLIK❌"} for r in regions}

user_region = {}
user_variant = {}
waiting_for_broadcast = set()

def start_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📍 Viloyatni tanlash")]
        ],
        resize_keyboard=True
    )

def region_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Toshkent"), KeyboardButton(text="Samarqand")],
            [KeyboardButton(text="Buxoro"), KeyboardButton(text="Farg‘ona")],
            [KeyboardButton(text="Andijon"), KeyboardButton(text="Namangan")],
            [KeyboardButton(text="Qashqadaryo"), KeyboardButton(text="Surxondaryo")],
            [KeyboardButton(text="Navoiy"), KeyboardButton(text="Sirdaryo")],
            [KeyboardButton(text="Jizzax"), KeyboardButton(text="Xorazm")],
            [KeyboardButton(text="🏠 Bosh menyu")],
        ],
        resize_keyboard=True
    )

def variant_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3"), KeyboardButton(text="4"), KeyboardButton(text="5"),],
            [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Bosh menyu")],
        ],
        resize_keyboard=True
    )

def confirm_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="✅ O‘tkazdim")],
            [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Bosh menyu")],
        ],
        resize_keyboard=True
    )

def admin_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="📊 Statistika"), KeyboardButton(text="👥 Foydalanuvchilar soni")],
            [KeyboardButton(text="📨 Oxirgi tanlovlar"), KeyboardButton(text="📢 Xabar yuborish")],
            [KeyboardButton(text="🏠 Bosh menyu")],
        ],
        resize_keyboard=True
    )

@dp.message(F.photo)
async def get_photo_id(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    save_user(message.from_user)
    user_region.pop(message.from_user.id, None)
    user_variant.pop(message.from_user.id, None)
    await message.answer("Xush kelibsiz", reply_markup=start_keyboard())

@dp.message(F.text == "📍 Viloyatni tanlash")
async def choose_region_handler(message: Message):
    await message.answer("📍 Viloyatni tanlang:", reply_markup=region_keyboard())

@dp.message(F.text == "/admin")
async def admin_panel(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("Admin panel", reply_markup=admin_keyboard())

@dp.message(F.text == "📊 Statistika")
async def stats_handler(message: Message):
    if not is_admin(message.from_user.id):
        return
    data = load_data()
    total_users = len(data["users"])
    total_choices = len(data["choices"])
    await message.answer(
        f"📊 Statistika\n\n"
        f"👥 Foydalanuvchilar: {total_users}\n"
        f"📨 Tanlovlar soni: {total_choices}"
    )

@dp.message(F.text == "👥 Foydalanuvchilar soni")
async def users_count_handler(message: Message):
    if not is_admin(message.from_user.id):
        return
    data = load_data()
    await message.answer(f"👥 Jami foydalanuvchilar: {len(data['users'])}")

@dp.message(F.text == "📨 Oxirgi tanlovlar")
async def last_choices_handler(message: Message):
    if not is_admin(message.from_user.id):
        return
    data = load_data()
    choices = data["choices"][-10:]
    if not choices:
        await message.answer("Hali tanlovlar yo‘q.")
        return

    text = "📨 Oxirgi tanlovlar:\n\n"
    for c in reversed(choices):
        username = f"@{c['username']}" if c["username"] else "username yo‘q"
        text += (
            f"👤 {c['full_name']} ({username})\n"
            f"🆔 {c['id']}\n"
            f"📍 {c['region']} | 🔢 {c['variant']}\n\n"
        )
    await message.answer(text)

@dp.message(F.text == "📢 Xabar yuborish")
async def broadcast_start(message: Message):
    if not is_admin(message.from_user.id):
        return
    waiting_for_broadcast.add(message.from_user.id)
    await message.answer("Yuboriladigan xabarni kiriting:")

@dp.message(F.text == "🏠 Bosh menyu")
async def home_handler(message: Message):
    user_region.pop(message.from_user.id, None)
    user_variant.pop(message.from_user.id, None)
    if is_admin(message.from_user.id):
        await message.answer("🏠 Bosh menyu", reply_markup=start_keyboard())
    else:
        await message.answer("🏠 Bosh menyu", reply_markup=start_keyboard())

@dp.message()
async def universal_handler(message: Message):
    save_user(message.from_user)

    if is_admin(message.from_user.id) and message.from_user.id in waiting_for_broadcast:
        waiting_for_broadcast.remove(message.from_user.id)
        data = load_data()
        sent = 0
        for uid in data["users"]:
            try:
                await bot.send_message(int(uid), message.text)
                sent += 1
            except:
                pass
        await message.answer(f"✅ Xabar yuborildi: {sent} ta userga", reply_markup=admin_keyboard())
        return

    if message.text in regions:
        region = message.text
        user_region[message.from_user.id] = region
        user_variant.pop(message.from_user.id, None)

        photos = region_photos.get(region, [])
        if photos:
            for photo in photos:
                await message.answer_photo(photo=photo, caption=common_text)

        await message.answer("👇 Kerakli variantni tanlang:", reply_markup=variant_keyboard())
        return

    if message.text in ["1", "2", "3"]:
        region = user_region.get(message.from_user.id)
        if not region:
            await message.answer("Avval viloyatni tanlang.", reply_markup=region_keyboard())
            return

        variant = message.text
        user_variant[message.from_user.id] = variant
        save_choice(message.from_user, region, variant)

        text = region_texts.get(region, {}).get(variant, "Matn topilmadi.")
        await message.answer(text, reply_markup=confirm_keyboard())
        return

    if message.text == "✅ O‘tkazdim":
        region = user_region.get(message.from_user.id)
        variant = user_variant.get(message.from_user.id)

        if not region or not variant:
            await message.answer("Avval viloyat va variantni tanlang.", reply_markup=region_keyboard())
            return

        text = confirm_texts.get(region, {}).get(variant, "❌XATOLIK❌")
        await message.answer(text, reply_markup=confirm_keyboard())
        return

    if message.text == "⬅️ Orqaga":
        user_region.pop(message.from_user.id, None)
        user_variant.pop(message.from_user.id, None)
        await message.answer("📍 Viloyatni tanlang:", reply_markup=region_keyboard())
        return

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
