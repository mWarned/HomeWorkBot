import os
from dotenv import load_dotenv
import discord
import datetime
from discord.ext import commands
from apscheduler.schedulers.background import BackgroundScheduler
import excelRead

# bot init
bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

# dataframes update
scheduler = BackgroundScheduler()
scheduler.add_job(excelRead.updatedf, 'interval', seconds=300)
scheduler.start()


# notification for bot start
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# command for homework for the next day
@bot.command()
async def hwnext(message):
    # automatic get of the day of week
    dayIndex = datetime.datetime.today().weekday()

    temelend = ""

    if dayIndex == 0:
        for i in range(len(excelRead.hwMarti)):
            temelend += str(excelRead.hwMarti[i][0]) + ": \n" + str(excelRead.hwMarti[i][1]) + "\n\n"
    elif dayIndex == 1:
        for i in range(len(excelRead.hwMiercuri)):
            temelend += str(excelRead.hwMiercuri[i][0]) + ": \n" + str(excelRead.hwMiercuri[i][1]) + "\n\n"
    elif dayIndex == 2:
        for i in range(len(excelRead.hwJoi)):
            temelend += str(excelRead.hwJoi[i][0]) + ": \n" + str(excelRead.hwJoi[i][1]) + "\n\n"
    elif dayIndex == 3:
        for i in range(len(excelRead.hwVineri)):
            temelend += str(excelRead.hwVineri[i][0]) + ": \n" + str(excelRead.hwVineri[i][1]) + "\n\n"
    else:
        for i in range(len(excelRead.hwLuni)):
            temelend += str(excelRead.hwLuni[i][0]) + ": \n" + str(excelRead.hwLuni[i][1]) + "\n\n"

    await message.send("Temele pentru ziua de miine:\n" + temelend)


# command for the homework for a specified day
@bot.command()
async def hw(message, ctx):
    temele = ""

    if ctx == "Luni":
        await message.send("Temele pentru ziua de luni.")
        for i in range(len(excelRead.hwLuni)):
            temele += str(excelRead.hwLuni[i][0]) + ": \n" + str(excelRead.hwLuni[i][1]) + "\n\n"

        await message.send(temele)

    if ctx == "Marti" or ctx == "Marți":
        await message.send("Temele pentru ziua de marți.")
        for i in range(len(excelRead.hwMarti)):
            temele += str(excelRead.hwMarti[i][0]) + ": \n" + str(excelRead.hwMarti[i][1]) + "\n\n"

        await message.send(temele)

    if ctx == "Miercuri":
        await message.send("Temele pentru ziua de miercuri.")
        for i in range(len(excelRead.hwMiercuri)):
            temele += str(excelRead.hwMiercuri[i][0]) + ": \n" + str(excelRead.hwMiercuri[i][1]) + "\n\n"

        await message.send(temele)

    if ctx == "Joi":
        await message.send("Temele pentru ziua de joi.")
        for i in range(len(excelRead.hwJoi)):
            temele += str(excelRead.hwJoi[i][0]) + ": \n" + str(excelRead.hwJoi[i][1]) + "\n\n"

        await message.send(temele)

    if ctx == "Vineri":
        await message.send("Temele pentru ziua de vineri.")
        for i in range(len(excelRead.hwVineri)):
            temele += str(excelRead.hwVineri[i][0]) + ": \n" + str(excelRead.hwVineri[i][1]) + "\n\n"

        await message.send(temele)

# bot running
load_dotenv()
bot.run(os.getenv("DSTOKEN"))
