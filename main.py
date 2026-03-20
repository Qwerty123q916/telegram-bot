import telebot
from telebot import types

TOKEN = "TOKENINGIZNI_BU_YERGA_QOYING"
bot = telebot.TeleBot(TOKEN)

# User state saqlash
user_state = {}

# =========================
# START
# =========================
@bot.message_handler(commands=['start'])
def start_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        "Toshkent", "Samarqand",
        "Buxoro", "Farg‘ona",
        "Andijon", "Namangan",
        "Qashqadaryo", "Surxondaryo",
        "Navoiy", "Sirdaryo",
        "Jizzax", "Xorazm"
    )
    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=markup)

# =========================
# db yozilganda viloyatlar chiqadi
# =========================
@bot.message_handler(func=lambda message: message.text and message.text.lower() == "db")
def db_handler(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        "Toshkent", "Samarqand",
        "Buxoro", "Farg‘ona",
        "Andijon", "Namangan",
        "Qashqadaryo", "Surxondaryo",
        "Navoiy", "Sirdaryo",
        "Jizzax", "Xorazm"
    )
    bot.send_message(message.chat.id, "Viloyatni tanlang:", reply_markup=markup)

# =========================
# TOSHKENT
# =========================
@bot.message_handler(func=lambda message: message.text == "Toshkent")
def tashkent_handler(message):
    chat_id = message.chat.id
    user_state[chat_id] = "toshkent_menu"

    # Bu yerda HECH QANDAY rasm/matn ochilmaydi
    # Faqat 1-2-3 knopka chiqadi
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    markup.add("1", "2", "3")
    markup.add("⬅️ Orqaga")
    bot.send_message(chat_id, "Toshkent bo‘yicha bo‘limni tanlang:", reply_markup=markup)

# =========================
# 1 TANLANGANDA
# =========================
@bot.message_handler(func=lambda message: message.text == "1")
def one_handler(message):
    chat_id = message.chat.id

    if user_state.get(chat_id) != "toshkent_menu":
        return

    user_state[chat_id] = "choice_1"

    # 1-variant uchun rasm va matn
    photo_1 = "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA"

    text_1 = (
        "Bu 1-variant uchun matn.\n"
        "Shu yerga kerakli yozuvni qo‘yasiz."
    )

    bot.send_photo(chat_id, photo_1, caption=text_1)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("O‘tkazdim")
    markup.add("⬅️ Orqaga")
    bot.send_message(chat_id, "Davom etish uchun tugmani bosing:", reply_markup=markup)

# =========================
# 2 TANLANGANDA
# =========================
@bot.message_handler(func=lambda message: message.text == "2")
def two_handler(message):
    chat_id = message.chat.id

    if user_state.get(chat_id) != "toshkent_menu":
        return

    user_state[chat_id] = "choice_2"

    # 2-variant uchun rasm va matn
    photo_2 = "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA"

    text_2 = (
        "Bu 2-variant uchun matn.\n"
        "Shu yerga 2-bo‘lim matnini yozasiz."
    )

    bot.send_photo(chat_id, photo_2, caption=text_2)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("O‘tkazdim")
    markup.add("⬅️ Orqaga")
    bot.send_message(chat_id, "Davom etish uchun tugmani bosing:", reply_markup=markup)

# =========================
# 3 TANLANGANDA
# =========================
@bot.message_handler(func=lambda message: message.text == "3")
def three_handler(message):
    chat_id = message.chat.id

    if user_state.get(chat_id) != "toshkent_menu":
        return

    user_state[chat_id] = "choice_3"

    # 3-variant uchun rasm va matn
    photo_3 = "AgACAgIAAxkBAAM0ab2pKkvg5q89v2i_61S_IGjEEJ4AAoUXaxsfTvFJkDRek4-ZPk0BAAMCAAN5AAM6BA"

    text_3 = (
        "Bu 3-variant uchun matn.\n"
        "Shu yerga 3-bo‘lim yozuvini qo‘yasiz."
    )

    bot.send_photo(chat_id, photo_3, caption=text_3)

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("O‘tkazdim")
    markup.add("⬅️ Orqaga")
    bot.send_message(chat_id, "Davom etish uchun tugmani bosing:", reply_markup=markup)

# =========================
# O‘TKAZDIM
# =========================
@bot.message_handler(func=lambda message: message.text == "O‘tkazdim")
def otkazdim_handler(message):
    chat_id = message.chat.id
    state = user_state.get(chat_id)

    if state == "choice_1":
        bot.send_message(chat_id, "1-variantdan keyingi matn shu yerda chiqadi.")
    elif state == "choice_2":
        bot.send_message(chat_id, "2-variantdan keyingi matn shu yerda chiqadi.")
    elif state == "choice_3":
        bot.send_message(chat_id, "3-variantdan keyingi matn shu yerda chiqadi.")
    else:
        bot.send_message(chat_id, "Avval 1, 2 yoki 3 dan birini tanlang.")
        return

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add("⬅️ Orqaga", "🏠 Bosh menu")
    bot.send_message(chat_id, "Keyingi amalni tanlang:", reply_markup=markup)

# =========================
# ORQAGA
# =========================
@bot.message_handler(func=lambda message: message.text == "⬅️ Orqaga")
def back_handler(message):
    chat_id = message.chat.id
    state = user_state.get(chat_id)

    # Agar 1/2/3 ichida bo‘lsa, Toshkent menyusiga qaytadi
    if state in ["choice_1", "choice_2", "choice_3", "toshkent_menu"]:
        user_state[chat_id] = "toshkent_menu"

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        markup.add("1", "2", "3")
        markup.add("⬅️ Orqaga", "🏠 Bosh menu")
        bot.send_message(chat_id, "Toshkent bo‘yicha bo‘limni tanlang:", reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        markup.add(
            "Toshkent", "Samarqand",
            "Buxoro", "Farg‘ona",
            "Andijon", "Namangan",
            "Qashqadaryo", "Surxondaryo",
            "Navoiy", "Sirdaryo",
            "Jizzax", "Xorazm"
        )
        bot.send_message(chat_id, "Viloyatni tanlang:", reply_markup=markup)

# =========================
# BOSH MENU
# =========================
@bot.message_handler(func=lambda message: message.text == "🏠 Bosh menu")
def home_handler(message):
    chat_id = message.chat.id
    user_state[chat_id] = "home"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    markup.add(
        "Toshkent", "Samarqand",
        "Buxoro", "Farg‘ona",
        "Andijon", "Namangan",
        "Qashqadaryo", "Surxondaryo",
        "Navoiy", "Sirdaryo",
        "Jizzax", "Xorazm"
    )
    bot.send_message(chat_id, "Bosh menyuga qaytdingiz. Viloyatni tanlang:", reply_markup=markup)

print("Bot ishga tushdi...")
bot.infinity_polling()
