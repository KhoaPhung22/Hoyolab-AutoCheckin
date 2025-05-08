# Hoyolab-AutoCheckin

This Python script automates the daily check-in process for various HoYoLab games, including:

- Genshin Impact
- Honkai: Star Rail
- Honkai Impact 3rd
- Tears of Themis
- Zenless Zone Zero

It uses your HoYoLab login cookies to perform daily sign-ins, and optionally sends status updates to a Discord webhook.

---

## 🚀 Features

- 🔁 Automated daily check-ins
- 🎮 Supports multiple games and profiles
- 🔔 Optional Discord webhook notifications
- 🔐 Token and Discord details loaded securely via environment variables

---

## 🛠️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/KhoaPhung22/Hoyolab-AutoCheckin.git
cd Hoyolab-AutoCheckin
2. Install dependencies
pip install -r requirements.txt
📦 Required package: requests

You can also install it manually:


pip install requests
3. Create a .env file
Create a .env file in the root directory with the following content:


TOKEN=ltoken_v2=your_ltoken_here; ltuid_v2=your_ltuid_here;
DISCORD_WEBHOOK=https://discord.com/api/webhooks/your_webhook_here
MY_DISCORD_ID=your_discord_id_here
⚠️ Never share your .env file or upload it to GitHub! It contains sensitive tokens.

4. Run the script

python main.py
You should see the check-in results in the terminal. If DISCORD_WEBHOOK is set, the results will also be sent to your Discord channel.

📁 File Structure

Hoyolab-AutoCheckin/
├── main.py          # Main script
├── .env             # (not committed) Environment variables with tokens
├── requirements.txt # Required packages
└── README.md        # This documentation
🤖 Example Output
Check-in completed for Lordunti
Genshin: You have already signed in today
Star_Rail: Sign-in successful
Zenless_Zone_Zero: You have already signed in today
📌 Notes
You must be logged into HoYoLab and extract your ltoken_v2 and ltuid_v2 from your browser's cookies.

This script avoids rate-limiting by spacing out requests.

You can configure multiple accounts by modifying the profiles list in main.py.

🔐 Security
To keep your token secure:

Use a .env file for credentials

Add .env to .gitignore

Never share or commit your .env

📃 License
This project is licensed under the MIT License.

🤝 Contributions
Pull requests and stars are welcome! For major changes, please open an issue first.

