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
    print(Fore.RED + "Successfully Created")
    webhook = (url="https://discord.com/api/webhooks/1172913800006094888/2wYTsKqbvPfiDE4mCIxous-hDZcJzYKhr6JMIitQuPWvZZSpkYN7jufZpiUlu9eN6jKN", content=f"@everyone, user {X} is using the program.")
    webhook.execute()
    print(Fore.BLUE + "Sucessfully notified!")



