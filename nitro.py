import requests, time, sys, os
from colorama import Fore, Back
from discord_webhook import DiscordWebhook, DiscordEmbed

X = input("Discord username: ")

directory = "Logs" #Folder name
space = os.getcwd() #Get file Path bruh
path = os.path.join(space, directory) #Full path with folder
os.mkdir(path) #Create folder 

def logs(X):

    content = os.listdir(path)
    with open(f"{X}", "w") as file:
        file.write(X)

logs(X)
