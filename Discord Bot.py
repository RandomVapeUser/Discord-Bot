import requests, time, sys, os, discord
from colorama import Fore

X = input("Discord username: ")
Y = int(input("Discord channel ID: "))  # Convert channel ID to int

# Variables
intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
directory = "Logs"
space = os.getcwd()
path = os.path.join(space, directory)
logs_create = os.path.join(path, f"{X}.txt")
messages = []

# Creation process
print(Fore.RED + "Successfully Created")
print(Fore.BLUE + "Redirecting to the chat.....")
time.sleep(3)


@client.event
async def on_ready():
    channel = client.get_channel(Y)
    await channel.send(f"User {X} has connected!")


@client.event
async def on_message(message):
    await client.process_commands(message)

    msg = message.content

    if msg != "":
        messages.append(msg)


async def message_send(message):
    channel = client.get_channel(Y)
    await channel.send(message)


client.run("MTE4OTE4NjI4NjgyNTc4MzQyNw.G9RmQW.4jxZJFi2hazRKPK3UHGL3pFaj_bDy3ZjVtr5CU")
