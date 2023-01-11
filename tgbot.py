import os
from dotenv import load_dotenv
import logging
from aiogram import Bot, Dispatcher, executor, types
import datetime
from apscheduler.schedulers.background import BackgroundScheduler
import excelRead

# log level
logging.basicConfig(level=logging.INFO)

# bot init
load_dotenv()
bot = Bot(token=os.getenv("TGTOKEN"))
dp = Dispatcher(bot)

# dataframe update
scheduler = BackgroundScheduler()
scheduler.add_job(excelRead.updatedf, 'interval', seconds=300)
scheduler.start()

# buttons
luni = types.KeyboardButton("Luni")
marti = types.KeyboardButton("Marți")
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
                           " Scrie <b>/teme</b> pentru a afla temele pentru o zi concreta.\n"
                           " Sau scrie <b>/next_day</b> pentru a afla temele pe ziua de mâine.".format(
                               message.from_user), parse_mode='html')


# commands handler
@dp.message_handler(commands=["teme"])
async def pop_menu(message: types.Message):
    await message.reply("Temele pe ce zi dorii să aflați?", reply_markup=keyboard1)


@dp.message_handler()
async def answer_to_user(message: types.Message):
    if message.text == "Luni":
        await message.answer("Temele pentru ziua de luni.")
        for i in range(len(excelRead.hwLuni)):
            await message.answer(str(excelRead.hwLuni[i][0]) + ": \n" + str(excelRead.hwLuni[i][1]), parse_mode="html")
    elif message.text == "Marți":
        await message.answer("Temele pentru ziua de marți.")
        for i in range(len(excelRead.hwMarti)):
            await message.answer(str(excelRead.hwMarti[i][0]) + ": \n" + str(excelRead.hwMarti[i][1]),
                                 parse_mode="html")
    elif message.text == "Miercuri":
        await message.answer("Temele pentru ziua de miercuri.")
        for i in range(len(excelRead.hwMiercuri)):
            await message.answer(str(excelRead.hwMiercuri[i][0]) + ": \n" + str(excelRead.hwMiercuri[i][1]),
                                 parse_mode="html")
    elif message.text == "Joi":
        await message.answer("Temele pentru ziua de joi.")
        for i in range(len(excelRead.hwJoi)):
            await message.answer(str(excelRead.hwJoi[i][0]) + ": \n" + str(excelRead.hwJoi[i][1]), parse_mode="html")
    elif message.text == "Vineri":
        await message.answer("Temele pentru ziua de vineri.")
        for i in range(len(excelRead.hwVineri)):
            await message.answer(str(excelRead.hwVineri[i][0]) + ": \n" + str(excelRead.hwVineri[i][1]),
                                 parse_mode="html")

    if message.text == "/next_day":
        # automatic get of the day of week
        dayIndex = datetime.datetime.today().weekday()

        await message.answer("Temele pentru ziua urmatoare.", parse_mode="html")

        if dayIndex == 0:
            for i in range(len(excelRead.hwMarti)):
                await message.answer(str(excelRead.hwMarti[i][0]) + ": \n" + str(excelRead.hwMarti[i][1]),
                                     parse_mode="html")
        elif dayIndex == 1:
            for i in range(len(excelRead.hwMiercuri)):
                await message.answer(str(excelRead.hwMiercuri[i][0]) + ": \n" + str(excelRead.hwMiercuri[i][1]),
                                     parse_mode="html")
        elif dayIndex == 2:
            for i in range(len(excelRead.hwJoi)):
                await message.answer(str(excelRead.hwJoi[i][0]) + ": \n" + str(excelRead.hwJoi[i][1]),
                                     parse_mode="html")
        elif dayIndex == 3:
            for i in range(len(excelRead.hwVineri)):
                await message.answer(str(excelRead.hwVineri[i][0]) + ": \n" + str(excelRead.hwVineri[i][1]),
                                     parse_mode="html")
        else:
            for i in range(len(excelRead.hwLuni)):
                await message.answer(str(excelRead.hwLuni[i][0]) + ": \n" + str(excelRead.hwLuni[i][1]),
                                     parse_mode="html")


# @dp.message_handler(commands=["next_day"])
# async def hw_next_day(message: types.Message):

# run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
