import excelRead
import logging
from aiogram import Bot, Dispatcher, executor, types

#log level
logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token="5810303748:AAHi32NfjbjfObnFznVj6GH92OLKwNuWea0")
dp = Dispatcher(bot)

#echo
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

#run long-polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)
