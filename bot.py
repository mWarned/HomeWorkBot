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
marti = types.KeyboardButton("Marți")
miercuri = types.KeyboardButton("Miercuri")
joi = types.KeyboardButton("Joi")
vineri = types.KeyboardButton("Vineri")

# keyboards
keyboard1 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)\
    .add(luni, marti, miercuri, joi, vineri)
keyboard2 = types.InlineKeyboardMarkup(row_width=3)


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
        await message.answer("Temele pentru ziua de luni.")
        for i in range(len(excelRead.hwLuni)) :
            await message.answer(str(excelRead.hwLuni[i][0]) + ": \n" + str(excelRead.hwLuni[i][1]), parse_mode="html")
    elif message.text == "Marți":
        await message.answer("Temele pentru ziua de marți.")
        for i in range(len(excelRead.hwMarti)):
            await message.answer(str(excelRead.hwMarti[i][0]) + ": \n" + str(excelRead.hwMarti[i][1]), parse_mode="html")
    elif message.text == "Miercuri":
        await message.answer("Temele pentru ziua de miercuri.")
        for i in range(len(excelRead.hwMiercuri)):
            await message.answer(str(excelRead.hwMiercuri[i][0]) + ": \n" + str(excelRead.hwMiercuri[i][1]), parse_mode="html")
    elif message.text == "Joi":
        await message.answer("Temele pentru ziua de joi.")
        for i in range(len(excelRead.hwJoi)):
            await message.answer(str(excelRead.hwJoi[i][0]) + ": \n" + str(excelRead.hwJoi[i][1]), parse_mode="html")
    elif message.text == "Vineri":
        await message.answer("Temele pentru ziua de vineri.")
        for i in range(len(excelRead.hwVineri)):
            await message.answer(str(excelRead.hwVineri[i][0]) + ": \n" + str(excelRead.hwVineri[i][1]), parse_mode="html")


# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
