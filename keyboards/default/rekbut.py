from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

xabarlar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
xabarlar.add(KeyboardButton("Matnli xabar jo'natish"))
xabarlar.add(KeyboardButton("Rasmli xabar jo'natish"))
xabarlar.add(KeyboardButton("Videoli xabar jo'natish"))

jonat = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
jonat.add(KeyboardButton("Jo'natish ✅"))
jonat.insert(KeyboardButton("Bekor qilish ❌"))

