import requests, time, sys, os
from colorama import Fore, Back
from discord_webhook import DiscordWebhook, DiscordEmbed

X = input("Discord username: ")

directory = "Logs" #Folder name
space = os.getcwd() #Get file Path bruh
path = os.path.join(space, directory) #Full path with folder
logs_create = os.path.join(path, X)
os.mkdir(path) #Create folder 

class Background():

    def logs(X):

        content = os.listdir(path)
        with open(logs_create, "w") as file:
            file.write(X)
    logs()
    print("Successfully Created")

    def discord_check():

        DiscordWebhook = ""