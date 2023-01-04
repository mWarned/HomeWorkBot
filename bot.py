import excelRead
import logging
from aiogram import Bot, Dispatcher, executor, types

# log level
logging.basicConfig(level=logging.INFO)

# bot init
bot = Bot(token="5810303748:AAHi32NfjbjfObnFznVj6GH92OLKwNuWea0")
dp = Dispatcher(bot)

# buttons
luni = types.KeyboardButton("Luni")
marti = types.KeyboardButton("Marti")
miercuri = types.KeyboardButton("Miercuri")
joi = types.KeyboardButton("Joi")
vineri = types.KeyboardButton("Vineri")

# keyboards
keyboard1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)\
    .add(luni, marti, miercuri, joi, vineri)


# start message handling
@dp.message_handler(commands=["start", "help"])
async def welcome_text(message: types.Message):
    await bot.send_photo(message.chat.id,
                         'https://i.pinimg.com/originals/c1/2d/af/c12daffa996683fe1080c809aca58e23.png')

    await bot.send_message(message.chat.id,
                           "Salutare {0.first_name}!\n"
                           " Ai nevoie de temele pentru acasă? Eu am toate temele pentru acasă de care ai nevoie.\n\n"
                           " Scrie <b>/teme</b> pentru a afla temele".format(
                               message.from_user), parse_mode='html')


@dp.message_handler(commands=["teme"])
async def pop_menu(message: types.Message):
    await message.reply("Temele pe ce zi dorii să aflați?", reply_markup=keyboard1)


@dp.message_handler()
async def answer_to_user(message: types.Message):

    if message.text == "Luni":
        await message.answer(excelRead.dfLuni)
    elif message.text == "Marti":
        await message.answer(excelRead.dfMarti)
    elif message.text == "Miercuri":
        await message.answer(excelRead.dfMiercuri)
    elif message.text == "Joi":
        await message.answer(excelRead.dfJoi)
    elif message.text == "Vineri":
        await message.answer(excelRead.dfVineri)


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
