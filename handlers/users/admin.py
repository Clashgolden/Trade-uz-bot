import asyncio

from aiogram import types

from data.config import ADMINS
from loader import dp, db, bot
from aiogram.dispatcher import FSMContext
from states.rekadmin import textm
from keyboards.default.rekbut import xabarlar,jonat
from keyboards.default.buttons import menbosh

@dp.message_handler(text="/allusers", user_id=ADMINS)
async def get_all_users(message: types.Message):
    users = db.select_all_users()
    print(users[0][0])
    await message.answer(users)

@dp.message_handler(text="/reklama", user_id=ADMINS, state=None)
async def send_ad_to_all(message: types.Message):
    await message.answer("<b>Foydalanuvchilarga qanday xabar jo'natmoqchisiz\n\n1 - Text xabar\n2 - Rasmli xabar\n3 - Videoli xabar</b>", reply_markup=xabarlar)
@dp.message_handler(text = "Matnli xabar jo'natish",user_id=ADMINS, state=None)
async def state_text(message: types.Message):
    await message.answer("<b>Reklama uchun matnni jo'nating:</b>")
    await textm.tekst.set()

@dp.message_handler(state=textm.tekst)
async def text_rek(message: types.Message, state:FSMContext):
    tekst = message.text
    await state.update_data({
        "tekst": tekst
    })
    await message.answer("Matn to'g'ri kiritilganligiga ishonchinggiz komilmi?\n\n- Agar hammasi to'g'ri bo'lsa - jo'natish tugmasini bosing.\n- Agarda biror xatolik bo'lsa - bekor qilish tugmasini bosing va jarayonni boshidan boshlang.", reply_markup=jonat)
    await textm.next()

@dp.message_handler(text = "Jo'natish ✅",state=textm.jon)
async def text_jon(message:types.Message, state: FSMContext):
    data = await state.get_data()
    users = db.select_all_users()
    for user in users:
        user_id = user[0]
        await bot.send_message(chat_id=user_id, text=f"{data['tekst']}")
        await asyncio.sleep(0.05)
    await message.answer("Jonatildi")
    await state.finish()
@dp.message_handler(text = "Bekor qilish ❌")
async def bekor_qilish(message: types.Message):
    await message.answer("<b>Bosh menyu:</b>", reply_markup=menbosh)
@dp.message_handler(text="/cleandb", user_id=ADMINS)
async def get_all_users(message: types.Message):
    db.delete_users()
    await message.answer("Baza tozalandi!")