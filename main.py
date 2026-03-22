import asyncio
import os
import json
from aiogram import Bot, Dispatcher, F
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardRemove,
)
from aiogram.exceptions import TelegramBadRequest


TOKEN = os.getenv("TOKEN")
if not TOKEN:
    raise ValueError("TOKEN topilmadi")

ADMIN_ID = 7890489981
DATA_FILE = "users_data.json"

bot = Bot(token=TOKEN)
dp = Dispatcher()


# =========================
# DATA
# =========================
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
        "username": user.username,
    }
    save_data(data)


def save_choice(user, region, variant):
    data = load_data()
    data["choices"].append({
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "region": region,
        "variant": variant,
    })
    save_data(data)


# =========================
# CONTENT
# =========================
regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo",
    "Navoiy", "Sirdaryo", "Jizzax", "Xorazm"
]

common_text = """🌟 Shahardagi ishonchli va qulay xizmatlardan biri

📸 Fotolar real

📋 Xizmat turlari:
1) Klassik
2) Relaks
3) Sog‘lomlashtiruvchi

🗣 Tillar: Русский, turkcha, qozoqcha

✅ To‘g‘ri tanlov qiling!"""

SERVICES_TEXT = """📋 Xizmatlar

✅ Klassik
✅ Relaks
✅ Sog‘lomlashtiruvchi
✅ Sport
✅ Mix xizmatlar

Kerakli viloyatni tanlab, variantni tanlashingiz mumkin."""

PRICES_TEXT = """💰 Narxlar

Narxlar viloyat va tanlangan variantga qarab farq qilishi mumkin.

📍 Viloyatni tanlang
🔢 Variantni tanlang
📩 Keyin sizga mos ma’lumot chiqadi"""

CONTACT_TEXT = """📞 Bog‘lanish

Admin: @username_yoki_raqam
Ish vaqti: 24/7

Qo‘shimcha ma’lumot uchun yozing."""

ABOUT_TEXT = """ℹ️ Biz haqimizda

Sizga qulay va tartibli ma’lumot berish uchun ushbu bot ishlab chiqilgan.

📍 Viloyat tanlash
📸 Rasmlar ko‘rish
🔢 Variant tanlash
📩 Kerakli ma’lumotni olish"""

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

# Har viloyat uchun variantlar
# keyin xohlasang 4,5,6 ham qo‘shish oson
region_texts = {
    r: {
        "1": f"{r} uchun 1-variant matni",
        "2": f"{r} uchun 2-variant matni",
        "3": f"{r} uchun 3-variant matni",
    }
    for r in regions
}

confirm_texts = {
    r: {
        "1": f"✅ {r} / 1-variant bo‘yicha qayd qilindi",
        "2": f"✅ {r} / 2-variant bo‘yicha qayd qilindi",
        "3": f"✅ {r} / 3-variant bo‘yicha qayd qilindi",
    }
    for r in regions
}


# =========================
# STATES
# =========================
user_region = {}
user_variant = {}
waiting_for_broadcast = set()


# =========================
# KEYBOARDS
# =========================
def start_keyboard():
    rows = [
        [KeyboardButton(text="📍 Viloyatlar")],
        [KeyboardButton(text="📋 Xizmatlar"), KeyboardButton(text="💰 Narxlar")],
        [KeyboardButton(text="📞 Bog‘lanish"), KeyboardButton(text="ℹ️ Biz haqimizda")],
    ]
    if ADMIN_ID:
        rows.append([KeyboardButton(text="/admin")])

    return ReplyKeyboardMarkup(keyboard=rows, resize_keyboard=True)


def region_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Toshkent"), KeyboardButton(text="Samarqand")],
            [KeyboardButton(text="Buxoro"), KeyboardButton(text="Farg‘ona")],
            [KeyboardButton(text="Andijon"), KeyboardButton(text="Namangan")],
            [KeyboardButton(text="Qashqadaryo"), KeyboardButton(text="Surxondaryo")],
            [KeyboardButton(text="Navoiy"), KeyboardButton(text="Sirdaryo")],
            [KeyboardButton(text="Jizzax"), KeyboardButton(text="Xorazm")],
            [KeyboardButton(text="⬅️ Orqaga"), KeyboardButton(text="🏠 Bosh menyu")],
        ],
        resize_keyboard=True
    )


def variant_keyboard(region: str):
    # Shu joyda regionga qarab variantlar sonini ko‘paytirish ham mumkin
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="1"), KeyboardButton(text="2"), KeyboardButton(text="3")],
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


# =========================
# HELPERS
# =========================
async def send_region_photos(message: Message, region: str):
    photos = region_photos.get(region, [])
    if not photos:
        await message.answer("Bu viloyat uchun hozircha rasmlar qo‘shilmagan.")
        return

    for i, photo in enumerate(photos):
        caption = common_text if i == 0 else None
        try:
            await message.answer_photo(photo=photo, caption=caption)
        except TelegramBadRequest:
            await message.answer("Rasmlardan birini yuborishda xatolik bo‘ldi.")


def reset_user_state(user_id: int):
    user_region.pop(user_id, None)
    user_variant.pop(user_id, None)


# =========================
# HANDLERS
# =========================
@dp.message(F.photo)
async def get_photo_id(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer(f"PHOTO_ID:\n{message.photo[-1].file_id}")


@dp.message(F.text == "/start")
async def start_handler(message: Message):
    save_user(message.from_user)
    reset_user_state(message.from_user.id)
    await message.answer(
        "Xush kelibsiz 👋\nKerakli bo‘limni tanlang:",
        reply_markup=start_keyboard()
    )


@dp.message(F.text == "/admin")
async def admin_panel(message: Message):
    if not is_admin(message.from_user.id):
        return
    await message.answer("Admin panelga xush kelibsiz.", reply_markup=admin_keyboard())


@dp.message(F.text == "📍 Viloyatlar")
async def choose_region_handler(message: Message):
    reset_user_state(message.from_user.id)
    await message.answer("📍 Viloyatni tanlang:", reply_markup=region_keyboard())


@dp.message(F.text == "📋 Xizmatlar")
async def services_handler(message: Message):
    await message.answer(SERVICES_TEXT, reply_markup=start_keyboard())


@dp.message(F.text == "💰 Narxlar")
async def prices_handler(message: Message):
    await message.answer(PRICES_TEXT, reply_markup=start_keyboard())


@dp.message(F.text == "📞 Bog‘lanish")
async def contact_handler(message: Message):
    await message.answer(CONTACT_TEXT, reply_markup=start_keyboard())


@dp.message(F.text == "ℹ️ Biz haqimizda")
async def about_handler(message: Message):
    await message.answer(ABOUT_TEXT, reply_markup=start_keyboard())


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
        f"📝 Tanlovlar soni: {total_choices}",
        reply_markup=admin_keyboard()
    )


@dp.message(F.text == "👥 Foydalanuvchilar soni")
async def users_count_handler(message: Message):
    if not is_admin(message.from_user.id):
        return
    data = load_data()
    await message.answer(
        f"👥 Jami foydalanuvchilar: {len(data['users'])}",
        reply_markup=admin_keyboard()
    )


@dp.message(F.text == "📨 Oxirgi tanlovlar")
async def last_choices_handler(message: Message):
    if not is_admin(message.from_user.id):
        return

    data = load_data()
    choices = data["choices"][-10:]

    if not choices:
        await message.answer("Hali tanlovlar yo‘q.", reply_markup=admin_keyboard())
        return

    text = "📨 Oxirgi 10 ta tanlov:\n\n"
    for c in reversed(choices):
        username = f"@{c['username']}" if c["username"] else "username yo‘q"
        text += (
            f"👤 {c['full_name']} ({username})\n"
            f"🆔 {c['id']}\n"
            f"📍 {c['region']} | 🔢 {c['variant']}\n\n"
        )

    await message.answer(text, reply_markup=admin_keyboard())


@dp.message(F.text == "📢 Xabar yuborish")
async def broadcast_start(message: Message):
    if not is_admin(message.from_user.id):
        return
    waiting_for_broadcast.add(message.from_user.id)
    await message.answer("Yuboriladigan xabarni yuboring:", reply_markup=ReplyKeyboardRemove())


@dp.message(F.text == "🏠 Bosh menyu")
async def home_handler(message: Message):
    reset_user_state(message.from_user.id)
    if message.from_user.id in waiting_for_broadcast:
        waiting_for_broadcast.remove(message.from_user.id)
    await message.answer("🏠 Bosh menyuga qaytdingiz.", reply_markup=start_keyboard())


@dp.message(F.text == "⬅️ Orqaga")
async def back_handler(message: Message):
    user_id = message.from_user.id

    # variant tanlagan bo‘lsa, region tanlashga qaytadi
    if user_id in user_variant:
        user_variant.pop(user_id, None)
        await message.answer("📍 Viloyatni qayta tanlang:", reply_markup=region_keyboard())
        return

    # region tanlagan bo‘lsa, bosh menyuga qaytadi
    if user_id in user_region:
        user_region.pop(user_id, None)
        await message.answer("🏠 Bosh menyuga qaytdingiz.", reply_markup=start_keyboard())
        return

    await message.answer("🏠 Bosh menyu", reply_markup=start_keyboard())


@dp.message()
async def universal_handler(message: Message):
    save_user(message.from_user)
    user_id = message.from_user.id
    text = message.text.strip() if message.text else ""

    # Broadcast mode
    if is_admin(user_id) and user_id in waiting_for_broadcast:
        waiting_for_broadcast.remove(user_id)
        data = load_data()
        sent = 0

        for uid in data["users"]:
            try:
                await bot.send_message(int(uid), text)
                sent += 1
            except Exception:
                pass

        await message.answer(
            f"✅ Xabar yuborildi: {sent} ta foydalanuvchiga",
            reply_markup=admin_keyboard()
        )
        return

    # Region tanlash
    if text in regions:
        region = text
        user_region[user_id] = region
        user_variant.pop(user_id, None)

        await message.answer(f"📍 Siz tanlagan viloyat: {region}")
        await send_region_photos(message, region)
        await message.answer("👇 Kerakli variantni tanlang:", reply_markup=variant_keyboard(region))
        return

    # Variant tanlash
    if text in ["1", "2", "3"]:
        region = user_region.get(user_id)

        if not region:
            await message.answer("Avval viloyatni tanlang.", reply_markup=region_keyboard())
            return

        user_variant[user_id] = text
        save_choice(message.from_user, region, text)

        result_text = region_texts.get(region, {}).get(text, "Matn topilmadi.")
        await message.answer(result_text, reply_markup=confirm_keyboard())
        return

    # Confirm
    if text == "✅ O‘tkazdim":
        region = user_region.get(user_id)
        variant = user_variant.get(user_id)

        if not region or not variant:
            await message.answer("Avval viloyat va variantni tanlang.", reply_markup=region_keyboard())
            return

        result_text = confirm_texts.get(region, {}).get(variant, "❌ Xatolik")
        await message.answer(result_text, reply_markup=confirm_keyboard())
        return

    await message.answer(
        "Kerakli tugmalardan birini tanlang.",
        reply_markup=start_keyboard()
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
