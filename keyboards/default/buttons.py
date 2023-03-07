from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

t = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
t.add(KeyboardButton(f"📲 Telefon Raqamini Jo'natish", request_contact=True))

daraja = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

daraja.add(KeyboardButton("Boshlang'ich"))
daraja.insert(KeyboardButton("O'rtacha"))

menbosh = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menbosh.add(KeyboardButton(f"Darsliklar 📚"))
menbosh.insert(KeyboardButton(f"Signallar 📊"))
menbosh.add(KeyboardButton("Pattern Book     📕"))
menbosh.insert(KeyboardButton("Mart oyi - Yangiliklari 📅"))
menbosh.add(KeyboardButton(f"Asosiy kurs haqida to'liq ma'lumot 📈"))
menbosh.add(KeyboardButton(f"Admin 👨‍💻"))

menor = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menor.add(KeyboardButton(f"Strategiyalar 📈"))
menor.insert(KeyboardButton(f"Fundamentals 📅"))
menor.add(KeyboardButton(f"Asosiy kurs haqida to'liq ma'lumot ✅"))
menor.add(KeyboardButton(f"Admin👨‍💻"))

darslar = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
darslar.add(KeyboardButton(f"1 - dars"))
darslar.insert(KeyboardButton(f"2 - dars"))
darslar.add(KeyboardButton(f"3 - dars"))
darslar.insert(KeyboardButton(f"4 - dars"))
darslar.add(KeyboardButton(f"5 - dars"))
darslar.add(KeyboardButton("◀️orqaga"))

orqa = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
orqa.add(KeyboardButton("◀️orqa"))

orqaga = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
orqaga.add(KeyboardButton("◀️orqaga"))

orr = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
orr.add(KeyboardButton("⬅️orqaga"))

static = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
static.add(KeyboardButton("1 - Signal"))
static.insert(KeyboardButton("2 - Signal"))
static.insert(KeyboardButton("3 - Signal"))
static.add(KeyboardButton("◀️orqaga"))

orstrat = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

orstrat.add(KeyboardButton("1 - Dars. FIBO 0.5"))
orstrat.add(KeyboardButton("2 - Dars. ORDER BLOCK VA YAKKA SVICHA"))
orstrat.add(KeyboardButton("3 - Dars. FVG ZONA"))
orstrat.add(KeyboardButton("4 - Dars. ISHONCHLI BROKER TANLASH"))

orstr = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
orstr.add(KeyboardButton(f"1 - Strategiya"))
orstr.insert(KeyboardButton(f"2 - Strategiya"))
orstr.add(KeyboardButton(f"3 - Strategiya"))
orstr.insert(KeyboardButton(f"4 - Strategiya"))
orstr.add(KeyboardButton(f"◀️ Orqaga Qaytish"))

orback = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

orback.add(KeyboardButton("◀️ Strategiyalarga qaytish"))

asosiykurs = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
asosiykurs.add(KeyboardButton("ONLINE SIMPLE"))
asosiykurs.insert(KeyboardButton("ONLINE THE BEST"))
asosiykurs.add(KeyboardButton("OFFLINE SIMPLE"))
asosiykurs.insert(KeyboardButton("OFFLINE AVARAGE"))
asosiykurs.add(KeyboardButton("OFFLINE THE BEST"))
asosiykurs.add(KeyboardButton("◀️orqaga"))

asosi = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
asosi.add(KeyboardButton("ONLINE SIMPLE."))
asosi.insert(KeyboardButton("ONLINE THE BEST."))
asosi.add(KeyboardButton("OFFLINE SIMPLE."))
asosi.insert(KeyboardButton("OFFLINE AVARAGE."))
asosi.add(KeyboardButton("OFFLINE THE BEST"))
asosi.add(KeyboardButton("◀️Menyu"))

asosiorqa = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
asosiorqa.add(KeyboardButton("◀️Menyuga Qaytish"))

menyu =ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
menyu.add(KeyboardButton("◀️Menyuga qaytish"))
kursorqa = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kursorqa.add(KeyboardButton("◀️Kurslarga qaytish"))



