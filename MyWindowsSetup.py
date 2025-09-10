#Author: DesignBAB
#Date: 9-9-25

import subprocess # to run O.S.commands
import os
import sys
import shutil


#defining the funtions
def install_package(package_name):
    try:
        subprocess.run(['winget', 'install', package_name], check=True)        
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

def strip_replace(file1, file2):
    shutil.copyfile(file1, file2)

def pause():
    response = input("Please press ENTER to continue... \n")
    if response.lower() == "q":
        exit()


nvimLocation = os.getlogin()
nvimLocation = "C:\\Users\\" + nvimLocation + "\\AppData\\Local\\nvim\\"
initVimString = """
This is a place were i can write into for a file
"""


print("Welcome to the Windows Rice Installer")
#now we start installing all the related programs
print("The first step: Download fastfetch 😎")
pause()
install_package('fastfetch')
print("")
print("Next we install neovim  ✏️")
pause()
install_package('neovim')
print("Now it is time to install Go! 🐹")
install_package('GoLang.Go')
#print("We will do a backup for bashrc just in case in its' same file location")
#with open(nvimLocation + "init.vim", "w") as file:
#    file.write(initVimString)
#
