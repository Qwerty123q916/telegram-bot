import Bot, Dispatcher, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()

regions = [
    "Toshkent", "Samarqand", "Buxoro", "Farg‘ona",
    "Andijon", "Namangan", "Qashqadaryo", "Surxondaryo",
    "Xorazm", "Navoiy", "Jizzax", "Sirdaryo"
]

@dp.message(F.text == "/start")
async def start_handler(message: Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=region, callback_data=f"region_{i}")]
            for i, region in enumerate(regions)
        ]
    )
    await message.answer("Viloyatni tanlang:", reply_markup=keyboard)

@dp.callback_query(F.data.startswith("region_"))
async def region_handler(callback: CallbackQuery):
    index = int(callback.data.split("_")[1])
    region = regions[index]

    photos = [
        ("https://via.placeholder.com/600x400.png?text=1-variant", "1-variant"),
        ("https://via.placeholder.com/600x400.png?text=2-variant", "2-variant"),
        ("https://via.placeholder.com/600x400.png?text=3-variant", "3-variant"),
    ]

    for i, (photo, caption) in enumerate(photos, start=1):
        await callback.message.answer_photo(
            photo=photo,
            caption=f"{region}\n{i} - {caption}"
        )

    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="1", callback_data=f"text_{index}_1"),
                
