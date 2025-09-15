## 🌾 Windows Rice Installer

Welcome to the **Windows Rice Installer** by **DesignBAB**—a minimalist, expressive setup script that transforms your Windows terminal into a personalized, aesthetic workspace. This tool automates the installation of Fastfetch, Neovim, and custom ASCII art, giving your shell a sleek, functional glow-up.

---

### ⚙️ Requirements

Before running the installer, make sure you have the following installed:

- **Python 3.10+**
- **Go (Golang)**

You can verify installation with:

```bash
python --version
go version
```

---

### 📦 What This Script Does

- Installs [Fastfetch](https://github.com/fastfetch-cli/fastfetch) via `winget`
- Builds a custom ASCII art binary using Go
- Installs [Neovim](https://neovim.io/) and sets up:
  - `init.vim` configuration
  - `coc-settings.json` for autocompletion
  - `vim-plug` plugin manager

---

### 🚀 How to Run

Clone this repo and run the installer:

```bash
python MyWindowsSetup.py
```

You'll be guided step-by-step with pauses and prompts. Press `ENTER` to continue through each phase, or type `q` to quit.

---

### 🎨 Fastfetch ASCII Integration

To display your custom ASCII art on terminal launch, add this to your PowerShell startup command:

```powershell
%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe -NoExit -Command PATH\TO\THE\main.exe | fastfetch --color '38;5;32' -c neofetch --logo -
```

Replace `PATH\TO\THE\main.exe` with the actual path to your compiled Go binary.

---

### 📝 Neovim Setup Notes

After installation:

1. Launch Neovim
2. Run `:PlugInstall` to fetch plugins
3. Enjoy your custom editor setup

---

Want help turning this into a GitHub p
