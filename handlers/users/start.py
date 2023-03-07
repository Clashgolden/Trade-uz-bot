import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from data.config import ADMINS
from loader import dp, db, bot
from keyboards.default.buttons import t, daraja, menbosh, menor, darslar, orqa, orqaga, static, orr, orstr, orback, asosiykurs, kursorqa,asosi,menyu,asosiorqa

from states.reghand import register
from aiogram.dispatcher import FSMContext

@dp.message_handler(commands="restart")
async def restart(message:types.Message):
    await message.answer("Trading sohasidagi bilim darajanggiz", reply_markup=daraja)

@dp.message_handler(text = "Boshlang'ich")
async def restart_bosh(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang</b>",reply_markup=menbosh)

@dp.message_handler(text = "O'rtacha")
async def restart_or(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=menor)
@dp.message_handler(CommandStart(), state=None)
async def bot_start(message: types.Message):
    name = message.from_user.full_name
    # Foydalanuvchini bazaga qo'shamiz
    try:
        db.add_user(id=message.from_user.id,
                    name=name)
    except sqlite3.IntegrityError as err:
        await bot.send_message(chat_id=ADMINS[0], text=err)

    await message.answer(f"<b>Assalomu alaykum - <i>{message.from_user.full_name}</i> 👋 \n\nThe Tradega xush kelibsiz! 🤝\nBotimizdan foydalanish uchun iltimos\nquydagi savollarimizga javob bering:\n\n [1/3]  Ism - Familyanggizni Kiriting?</b>")
    await register.name.set()
    # Adminga xabar beramiz
    count = db.count_users()[0]
    msg = f"{message.from_user.full_name} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
    await bot.send_message(chat_id=ADMINS[0], text=msg)

@dp.message_handler(state=register.name)
async def Register_procces_ism(message: types.Message, state: FSMContext):
    name = message.text
    await state.update_data({
        "name": name
    })
    await message.answer(f"<b>[2/3] Quyidagi tugmani bosib telefon raqaminggizni jo'nating </b>👇", reply_markup=t)
    await register.next()

@dp.message_handler(content_types='contact', state=register.number)
async def Register_procces_nomeri(message: types.Message, state: FSMContext):
    number = message.contact.phone_number
    await state.update_data(
        {"number": number}
    )
    text = f"<b>[3/3] Trading sohasida bilim darajanggiz qanday?</b>"
    await message.answer(text, reply_markup=daraja)
    await register.next()

@dp.message_handler(state=register.lvl)
async def Register_procces_daraja(message: types.Message, state: FSMContext):
    lvl = message.text
    await state.update_data({
        "lvl": lvl
    })
    if message.text == "Boshlang'ich":
        await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=menbosh)
    else:
        await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=menor)
    data = await state.get_data()
    await bot.send_message(chat_id=-1001832889875, text=f"Yangi foydalanuvchi bor:\n\n"
                           f"Ismi: {data['name']}\n"
                           f"Raqami: {data['number']}\n"
                           f"Darajasi: {data['lvl']}")
    await state.finish()

@dp.message_handler(text = "Darsliklar 📚")
async def Handler_Darslar(message: types.Message):
    await message.answer(f"<b>Darsni tanlang:</b>", reply_markup=darslar)

@dp.message_handler(text = "1 - dars")
async def handler_one(message: types.Message):
    url = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/2"
    chat_id = message.chat.id
    text = f"<b>1 - dars:\n\nMeta Trader 4 - Platformasida Savdo qilish✅</b>"
    await bot.send_video(video= url, caption=text, chat_id=chat_id, reply_markup=orqa)

@dp.message_handler(text = "2 - dars")
async def handler_one(message: types.Message):
    url = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/3"
    chat_id = message.chat.id
    text = f"<b>2 - dars:\n\nBUY LIMIT va SELL LIMIT - qo'yish✅</b>"
    await bot.send_video(video= url, caption=text, chat_id=chat_id, reply_markup=orqa)

@dp.message_handler(text = "3 - dars")
async def handler_one(message: types.Message):
    url = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/4"
    chat_id = message.chat.id
    text = f"<b>3 - dars:\n\nBUY STOP va SELL STOP - qo'yish✅</b>"
    await bot.send_video(video= url, caption=text, chat_id=chat_id, reply_markup=orqa)

@dp.message_handler(text = "4 - dars")
async def handler_one(message: types.Message):
    url = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/5"
    chat_id = message.chat.id
    text = f"<b>4 - dars:\n\nTradingView - Platformasi✅</b>"
    await bot.send_video(video= url, caption=text, chat_id=chat_id, reply_markup=orqa)

@dp.message_handler(text = "5 - dars")
async def handler_one(message: types.Message):
    url = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/6"
    chat_id = message.chat.id
    text = f"<b>5 - dars:\n\nForex Factor - Fundamentals✅</b>"
    await bot.send_video(video= url, caption=text, chat_id=chat_id, reply_markup=orqa)
    await bot.send_message(chat_id = message.chat.id, text = f"<b>Mana siz 5 ta darsimiz bilan tanishib chiqdinggiz va boshlang'ich <i>BILIM</i> ga ega bo'ldinggiz.\n\nBu <i>TRADING</i> ni 100% dan 3% ni tashkil qiladi. Sizga yanada ko'proq <i>BILIM</i> lar o'rganishni maslahat beraman.\n\n <i>HURMAT BILAN - THE TRADE JAMOASI 🤝.</i></b>")


@dp.message_handler(text = f"◀️orqaga")
async def handler_back(message: types.Message):
    await message.answer(f"<b>Bosh menyuga qaytdinggiz:</b>",reply_markup=menbosh)

@dp.message_handler(text = f"◀️orqa")
async def handler(message: types.Message):
    await message.answer(f"<b>Kerakli Darsni Tanlang:</b>", reply_markup=darslar)

@dp.message_handler(text = f"Pattern Book     📕")
async def handler_book(message: types.Message):
    file = "https://t.me/hudsvcfkjkdsbfvrgwviuekf/7"
    await bot.send_document(document=file, chat_id=message.chat.id,caption=f"<b>Internatda mashxur bo'lgan - Pattern Book kitobchasi sizlar uchun. Kitobcha shaklida chiqarib, bemalol foydalansanggiz bo'ladi!</b>", reply_markup=orqaga)

@dp.message_handler(text = f"Mart oyi - Yangiliklari 📅")
async def handler_news(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/8",caption=f"<b>Mart - oyidagi barcha yangiliklar bir jadvalda! Sizga qulay bo'lishi uchun.</b>",reply_markup=orqaga)

@dp.message_handler(text = f"Signallar 📊")
async def handler_signal(message: types.Message):
    await message.answer(f"<b>Bu bo'limda:  Sizga 3 ta <i>ДОЛГОСРОЧНЫЙ</i> SIGNALLAR beriladi📊</b>", reply_markup=static)

@dp.message_handler(text = "1 - Signal")
async def handler_one_signal(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/9", caption=f"<b>USD/CAD - SELL LIMIT\n\nSavdo nuqta: <i> 1.36800</i>\nStop lose: <i> 1.38200</i>\nTake profit: <i> 1.28000</i></b>",reply_markup=orr)

@dp.message_handler(text = "2 - Signal")
async def handler_one_signal(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/10", caption=f"<b>NFLX - SELL LIMIT\n\nSavdo nuqta: <i> 347.50</i>\nStop lose: <i> 385.00</i>\nTake profit: <i> 165.00</i></b>",reply_markup=orr)

@dp.message_handler(text = "3 - Signal")
async def handler_one_signal(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/11", caption=f"<b>BABA - BUY LIMIT\n\nSavdo nuqta: <i> 90.50</i>\nStop lose: <i> 71.00</i>\nTake profit: <i> 160.00</i></b>",reply_markup=orr)
    await bot.send_message(chat_id=message.chat.id, text = f"<b>Ushbu - <i>SIGNALLAR</i> uzoq muddatli berilgan. Sabrli bo'lsanggiz unumli foydalanib olasiz!\n\nBOZOR - SABRLI INSONLARNI YOQTIRADI!\n\n<i>ASOSIY SIGNAL KANALIMIZGA QO'SHILISHNI XOXLASANGGIZ ADMINGA MUROJAAT QILING: @THETRADE_ADMIN\n\nHURMAT BILAN - THE TRADE JAMOASI🤝</i></b>")

@dp.message_handler(text = f"⬅️orqaga")
async def handler_signal_back(message: types.Message):
    await bot.send_message(text= f"<b>Signal raqamini tanlang:</b>", reply_markup=static, chat_id=message.chat.id)

@dp.message_handler(text = f"Admin 👨‍💻")
async def handler_admin_state(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/13   "  ,caption = f"<b>👨‍💻 Admin bilan bog'lanish:</b>\n\n🕓 <b>Ish vaqti:</b> 09 : 00 - 00 : 00\n\n<b>✔️ Telegram:</b> @thetrade_admin\n📞 <b>Telefon Raqam:</b> +998 93 534 75 00",reply_markup=menbosh)

@dp.message_handler(text = "Asosiy kurs haqida to'liq ma'lumot 📈")
async def handler_about(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text = f"<b>Kerakli menyuni tanlang:</b>",reply_markup=asosiykurs)

@dp.message_handler(text = "ONLINE SIMPLE")
async def handler_online_simple(message:types.Message):
    await message.answer("""<b>ONLINE SIMPLE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 3 kun bo'ladi
- Savdo uchun kapital berilmaydi
- Sovg'a sifatda: 2 ta ROBOT va 3 ta INDIKATOR. Signal kanalga 6 oylik obuna beriladi.

Kurs narxi: 129$
Bu bir martalik to'lov!

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=kursorqa)

@dp.message_handler(text = "◀️Kurslarga qaytish")
async def handler_back(message: types.Message):
    await message.answer("<b>Kerakli kursni tanlang:</b>", reply_markup=asosiykurs)

@dp.message_handler(text = "ONLINE THE BEST")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>ONLINE THE BEST:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 3 kun bo'ladi
- 10.000$ Kapital beriladi
- Sovg'a sifatida: 3 ta ROBOT, 5 ta INDIKATOR, Signal kanalga 1 yillik obuna beriladi.

Kurs narxi: 229$
Bu bir martalik to'lov!

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=kursorqa)

@dp.message_handler(text = "OFFLINE SIMPLE")
async def handler_kur_best(message: types.Message):
    await message.answer("""<b>OFFLINE SIMPLE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 10 ta strategiya o'rgatiladi
- Savdo uchun 5.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi:  390$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=kursorqa)

@dp.message_handler(text = "OFFLINE AVARAGE")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>OFFLINE AVARAGE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 15 ta strategiya o'rgatiladi
- Savdo uchun 10.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi: 590$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=kursorqa)
@dp.message_handler(text = f"O'rtacha")

@dp.message_handler(text = "OFFLINE THE BEST")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>OFFLINE THE BEST:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 20 ta strategiya o'rgatiladi
- Savdo uchun 20.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi: 790$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=kursorqa)
# --------------------------------------------------------------------------------------------------------------------------------------------------------





@dp.message_handler(text = "ONLINE SIMPLE.")
async def handler_online_simple(message:types.Message):
    await message.answer("""<b>ONLINE SIMPLE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 3 kun bo'ladi
- Savdo uchun kapital berilmaydi
- Sovg'a sifatda: 2 ta ROBOT va 3 ta INDIKATOR. Signal kanalga 6 oylik obuna beriladi.

Kurs narxi: 129$
Bu bir martalik to'lov!

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=asosiorqa)

@dp.message_handler(text = "◀️Kurslarga qaytish")
async def handler_back(message: types.Message):
    await message.answer("<b>Kerakli kursni tanlang:</b>", reply_markup=asosi)

@dp.message_handler(text = "ONLINE THE BEST.")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>ONLINE THE BEST:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 3 kun bo'ladi
- 10.000$ Kapital beriladi
- Sovg'a sifatida: 3 ta ROBOT, 5 ta INDIKATOR, Signal kanalga 1 yillik obuna beriladi.

Kurs narxi: 229$
Bu bir martalik to'lov!

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=asosiorqa)

@dp.message_handler(text = "OFFLINE SIMPLE.")
async def handler_kur_best(message: types.Message):
    await message.answer("""<b>OFFLINE SIMPLE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 10 ta strategiya o'rgatiladi
- Savdo uchun 5.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi:  390$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=asosiorqa)

@dp.message_handler(text = "OFFLINE AVARAGE.")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>OFFLINE AVARAGE:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 15 ta strategiya o'rgatiladi
- Savdo uchun 10.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi: 590$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=asosiorqa)
@dp.message_handler(text = f"O'rtacha")

@dp.message_handler(text = "OFFLINE THE BEST.")
async def handler_kurs_best(message: types.Message):
    await message.answer("""<b>OFFLINE THE BEST:

- Bu sohani 0 dan boshlaymiz
- Texnik va Fundamentals analiz darslar
- Darslar haftada 4 kun bo'ladi
- Dars vaqti 14:00
- Har bitta STRATEGIYA bir hafta davomida mukammal o'rganiladi, Kursda 20 ta strategiya o'rgatiladi
- Savdo uchun 20.000$ KAPITAL beriladi
- Savdo va bonuslar beriladi, eng asosiysi OFFLINE AMALIYOT bo'ladi

Kurs narxi: 790$
Bu bir martalik to'lov

<a href='https://t.me/thetrade_admin'>KURSNI SOTIB OLISH</a></b>""", disable_web_page_preview=True, reply_markup=asosiorqa)

@dp.message_handler(text = "◀️Menyuga Qaytish")
async def back_usr(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=asosi)

async def handler_or(message: types.Message):
    await message.answer(f"Ma'lumotlaringgiz qabul qilindi! Kerakli bo'limni tanlang:")

@dp.message_handler(text = f"Asosiy kurs haqida to'liq ma'lumot ✅")
async def handler_kurs(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang</b>", reply_markup=asosi)

@dp.message_handler(text = f"◀️Menyu")
async def handler_menyu(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=menor)
@dp.message_handler(text = f"Admin👨‍💻")
async def handler_or_admin(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/13", caption = f"<b>👨‍💻 Admin bilan bog'lanish:</b>\n\n🕓 <b>Ish vaqti:</b> 09 : 00 - 00 : 00\n\n<b>✔️ Telegram:</b> @thetrade_admin\n📞 <b>Telefon Raqam:</b> +998 93 534 75 00",reply_markup=menor)

@dp.message_handler(text = f"Strategiyalar 📈")
async def handler_strat(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,text = f"<b>Kerakli darsni tanlang:</b>", reply_markup=orstr)

@dp.message_handler(text = f"◀️ Orqaga Qaytish")
async def back_user(message:types.Message):
    await message.answer("<b>Kerakli menyuni tanlang:</b>", reply_markup=menor)

@dp.message_handler(text = f"1 - Strategiya")
async def handler_one_str(message: types.Message):
    await bot.send_video(video="https://t.me/hudsvcfkjkdsbfvrgwviuekf/19",chat_id=message.chat.id, caption="<b>FIBO 0.5 - Strategiyasi</b>", reply_markup=orback)

@dp.message_handler(text = f"◀️ Strategiyalarga qaytish")
async def handler_orback(message: types.Message):
    await message.answer("<b>Kerakli menyuni tanlang:</b>",reply_markup=orstr)

@dp.message_handler(text = f"2 - Strategiya")
async def handler_one_str(message: types.Message):
    await bot.send_video(video="https://t.me/hudsvcfkjkdsbfvrgwviuekf/20",chat_id=message.chat.id,caption="<b>ORDER BLOCK VA YAKKA SVICHA</b>", reply_markup=orback)

@dp.message_handler(text = f"3 - Strategiya")
async def handler_one_str(message: types.Message):
    await bot.send_video(video="https://t.me/hudsvcfkjkdsbfvrgwviuekf/21",chat_id=message.chat.id,caption="<b>ORDER BLOCK + FVG ZONA</b>", reply_markup=orback)

@dp.message_handler(text = f"4 - Strategiya")
async def handler_one_str(message: types.Message):
    await bot.send_video(video="https://t.me/hudsvcfkjkdsbfvrgwviuekf/22",chat_id=message.chat.id,caption="<b>TO'G'RI BROKER TANLASH</b>", reply_markup=orback)
    await bot.send_message(chat_id=message.chat.id, text = "Mana sizga 3 ta STRATEGIYA va ISHONCHLI BROKER tanlash o'rgatildi.\n\nBu BILIM xech nima emas, Yanada ko'proq BILIM lar o'rganishinggizni maslahat beraman. O'rgangan 3 ta STRATEGIYA ni amaliyotda sinab ko'ring!\n\nHURMAT BILAN - THE TRADE JAMOASI🤝")

@dp.message_handler(text = f"Fundamentals 📅")
async def handler_news(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://t.me/hudsvcfkjkdsbfvrgwviuekf/8",caption=f"<b>Mart - oyi Yangiliklar Sahifasi!\n\nBu yerda eng kerakli yangiliklar inobatga olingan.\n\nBu imkoniyatdan unumli foydalaning!</b>",reply_markup=menyu)

@dp.message_handler(text = f"◀️Menyuga qaytish")
async def menyu_handler(message:types.Message):
    await message.answer("<b>Kerakli menyuni tanlang</b>",reply_markup=menor)
async def handler_men(message: types.Message):
    await message.answer("Kerakli menyuni tanlang:", reply_markup=menor)