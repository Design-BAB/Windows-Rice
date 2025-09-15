#Author: DesignBAB
#Date: 9-15-25

import subprocess # to run O.S.commands
import os
import sys
import shutil
from pathlib import Path

#Need to define the variables first
nvimLocation = os.getlogin()
nvimLocation = "C:\\Users\\" + nvimLocation + "\\AppData\\Local\\nvim\\"


def install_vim_plug():
    command = (
        'iwr -useb https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim | '
        'ni $HOME\\vimfiles\\autoload\\plug.vim -Force'
    )
    try:
        subprocess.run(command, check=True)
        print("✅ vim-plug installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"❌ An error occurred while installing vim-plug: {e}")


#defining the funtions
def install_package(package_name):
    try:
        subprocess.run(['winget', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


#download Ascii Art
filename = os.getcwd()
filename = filename + "\\src\\main.go"
def setup_Ascii():
    try:
        subprocess.run(['go', 'build', filename], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")


def pause():
    response = input("Press ENTER to continue... \n")
    if response.lower() == "q":
        exit()


print("Welcome to the Windows Rice Installer")
#now we start installing all the related programs
print("The first step: Download fastfetch 😎")
pause()
install_package('Fastfetch-cli.Fastfetch')
print("")
print("Now we setup the ASCII art for fastfetch")
os.makedirs(docLocation, exist_ok=True)
setup_Ascii()
pause()
print("You can add the fastfetch as a welcome message by adding this to the commandline with powershell settings...")
print("%SystemRoot%\\System32\\WindowsPowerShell\\v1.0\\powershell.exe -NoExit -Command PATH\\TO\\THE\\main.exe | fastfetch --color '38;5;32' -c neofetch --logo -")
print("")
pause("")
print("")
print("Next we install neovim along with its' custom settings✏️")
pause()
install_package('Neovim.Neovim')
# Create the directory if it doesn't exist
os.makedirs(nvimLocation, exist_ok=True)
install_vim_plug()
shutil.copy("src\\init.vim", nvimLocation + "init.vim")
shutil.copy("src\\coc-settings.json", nvimLocation + "coc-settings.json")
print("Done!")
print("")
print("Please remember to run the :PlugInstall when you first open up nvim")
pause()
