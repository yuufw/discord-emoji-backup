# Discord Emoji Downloader 🤖✨

A Python script that downloads custom emojis from a server using a bot token.
This project is useful for backing up or organizing custom emojis from a server.

### 📌 Features
- Connects to a server using a bot token
- Fetches and downloads custom emojis
- Saves emojis locally in an organized folder structure
- Supports static and animated emojis

### ⚙️ Requirements
Before running the project, make sure you have:
- Python 3.11 or higher
- A bot created on the platform
- A valid bot token
- Permission to view emojis on the server

### 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yuufw/discord-emoji-downloader.git
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### 🔑 Configuration
Edit the config.py file and add your credentials:
```python
BOT_TOKEN = "YOUR_BOT_TOKEN"
```
> [!WARNING]
> Never commit or share your bot token publicly.

### ▶️ Usage
Run the script with:
```bash
python main.py
```
All emojis will be downloaded and saved inside the emojis/ directory.

### 🔐 Security Notes

- Do not commit secrets or tokens
- Grant the bot only the permissions it strictly needs

### 📄 Notes
- The bot must be a member of the server
- Some servers may restrict emoji access
- Animated emojis are usually saved as .gif files

