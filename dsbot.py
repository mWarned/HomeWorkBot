import discord
from discord.ext import commands
from apscheduler.schedulers.background import BackgroundScheduler
import excelRead


bot = commands.Bot(command_prefix="/", intents=discord.Intents.all())

scheduler = BackgroundScheduler()
scheduler.add_job(excelRead.updatedf, 'interval', seconds=300)
scheduler.start()


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


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

bot.run("MTA2MTY1Mzc5NjY1ODM2NDQ4OA.Gz6kyO.-Ibf2pk7KxtSH0nnmtTMeiLeKxtmI4U2FHG0YI")
