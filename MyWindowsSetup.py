#Author: DesignBAB
#Date: 9-15-25

import subprocess # to run O.S.commands
import os
import sys
import shutil
from pathlib import Path

#Need to define the variables first
nvimLocation = os.getlogin()
docLocation = "C:\\Users\\" + nvimLocation + "\\Documents"
nvimLocation = "C:\\Users\\" + nvimLocation + "\\AppData\\Local\\nvim\\"


def replace_windows_terminal_settings():
    # Locate the new settings.json in ./src/settings.json
    script_dir = Path(__file__).parent
    new_settings_path = script_dir / "src" / "settings.json"
    if not new_settings_path.exists():
        raise FileNotFoundError(f"❌ Custom settings.json not found at {new_settings_path}")

    # Get LOCALAPPDATA
    local_appdata = os.environ.get("LOCALAPPDATA")
    if not local_appdata:
        raise EnvironmentError("LOCALAPPDATA not found.")

    # Find the Windows Terminal settings path
    wt_base = Path(local_appdata) / "Packages"
    candidates = [p for p in wt_base.glob("Microsoft.WindowsTerminal_*") if p.is_dir()]
    if not candidates:
        raise FileNotFoundError("Windows Terminal package folder not found.")

    settings_dir = candidates[0] / "LocalState"
    settings_file = settings_dir / "settings.json"

    # Backup existing settings
    backup_file = settings_dir / "settings.backup.json"
    shutil.copy2(settings_file, backup_file)

    # Replace with new settings
    shutil.copy2(new_settings_path, settings_file)
    print(f"✅ Replaced Windows Terminal settings with: {new_settings_path}")


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
        shutil.copy("main.exe", docLocation + "\\main.exe")
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
#replace_windows_terminal_settings()
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
