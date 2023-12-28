import discord, time, sys, os
from colorama import Fore

X = input("Discord username: ")
Y = int(input("Discord channel ID: "))  #

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
    await channel.send(f"@everyone, User {X} has connected!")


@client.event
async def on_message(message):

    msg = message.content

    if msg != "" and message.author != client.user:
        messages.append(msg)
        print(msg)

@client.event
async def on_ready():
    
    global X

    while True:
        
        O = input("You: ")

        if O != "69":
            channel = client.get_channel(Y)
            await channel.send(f"User {X} says {O}")
            continue
        elif O == "69":
            print("Exiting....")
            time.sleep(4)
            sys.exit()

client.run("Your Bot token here :D")
