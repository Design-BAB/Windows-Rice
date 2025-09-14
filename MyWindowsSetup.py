#Author: DesignBAB
#Date: 9-9-25

import subprocess # to run O.S.commands
import os
import sys
import shutil
import requests


#defining the funtions
def install_package(package_name):
    try:
        subprocess.run(['winget', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

#download Ascii Art
url = "https://raw.githubusercontent.com/Design-BAB/MyAsciiArtworks/main/WindowArt/main.go"
filename = "main.go"
def download_Ascii():
    try:
        # Send a GET request to the raw URL
        response = requests.get(url)
    
        # Raise an exception for bad status codes (e.g., 404 Not Found)
        response.raise_for_status()
    
        # Write the content of the response to a file
        with open(filename, "wb") as f:
            f.write(response.content)

        print(f"Successfully downloaded {filename}")
        print(f"File saved to: {os.path.abspath(filename)}")
        try:
            subprocess.run(['go', 'build', filename], check=True)        
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while downloading the file: {e}")
    

def pause():
    response = input("Please press ENTER to continue... \n")
    if response.lower() == "q":
        exit()


nvimLocation = os.getlogin()
nvimLocation = "C:\\Users\\" + nvimLocation + "\\AppData\\Local\\nvim\\"

print("Welcome to the Windows Rice Installer")
#now we start installing all the related programs
print("The first step: Download fastfetch 😎")
pause()
install_package('Fastfetch-cli.Fastfetch')
print("")
print("Now we download the ascii art for fastfetch")
download_Ascii()
print("")
print("Next we install neovim  ✏️")
pause()
install_package('Neovim.Neovim')
print("Now it is time to install Go! 🐹")
install_package('GoLang.Go')
# Create the directory if it doesn't exist
os.makedirs(nvimLocation, exist_ok=True)
shutil.copy("src\\init.vim", nvimLocation + "init.vim")
shutil.copy("src\\coc-settings.json", nvimLocation + "coc-settings.json")
