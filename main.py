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

    builder = InlineKeyboardBuilder()
    builder.button(text="1", callback_data=f"text_{index}_1")
    builder.button(text="2", callback_data=f"text_{index}_2")
    builder.button(text="3", callback_data=f"text_{index}_3")
    builder.adjust(3)

    await callback.message.answer(
        f"{region} tanlandi. Variantni tanlang:",
        reply_markup=builder.as_markup()
    )
    await callback.answer()

@dp.callback_query(F.data.startswith("text_"))
async def text_handler(callback: CallbackQuery):
    _, region_index, variant = callback.data.split("_")
    region = regions[int(region_index)]

    texts = {
        "1": f"{region} uchun 1-variant matni.",
        "2": f"{region} uchun 2-variant matni.",
        "3": f"{region} uchun 3-variant matni.",
    }

    await callback.message.answer(texts.get(variant, "Matn topilmadi."))
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
