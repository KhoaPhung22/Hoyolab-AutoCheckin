import os
from dotenv import load_dotenv
import requests
import time

# Load environment variables from .env file
load_dotenv()

# Use environment variables securely
token = os.getenv("TOKEN")
discord_webhook = os.getenv("DISCORD_WEBHOOK")
my_discord_id = os.getenv("MY_DISCORD_ID")


# Configuration
profiles = [
    {
        "token": token,
        "genshin": True,
        "honkai_star_rail": True,
        "honkai_3": False,
        "tears_of_themis": False,
        "zenless_zone_zero": True,
        "accountName": "Lordunti"
    }
]

discord_notify = True
# URL Dictionary
url_dict = {
    "Genshin": "https://sg-hk4e-api.hoyolab.com/event/sol/sign?lang=en-us&act_id=e202102251931481",
    "Star_Rail": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202303301540311",
    "Honkai_3": "https://sg-public-api.hoyolab.com/event/mani/sign?lang=en-us&act_id=e202110291205111",
    "Tears_of_Themis": "https://sg-public-api.hoyolab.com/event/luna/os/sign?lang=en-us&act_id=e202308141137581",
    "Zenless_Zone_Zero": "https://sg-public-api.hoyolab.com/event/luna/zzz/os/sign?lang=en-us&act_id=e202406031448091"
}

# Header Dictionary
header_dict = {
    "default": {
        "Accept": "application/json, text/plain, */*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "x-rpc-app_version": "2.34.1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        "x-rpc-client_type": "4",
        "Referer": "https://act.hoyolab.com/",
        "Origin": "https://act.hoyolab.com",
    },
    "Zenless_Zone_Zero": {
        "x-rpc-signgame": "zzz",
    }
}

def discord_ping():
    return f"<@{my_discord_id}> " if my_discord_id else ""

def post_webhook(data):
    if not discord_webhook:
        return

    payload = {
        "username": "auto-sign",
        "avatar_url": "https://i.imgur.com/LI1D4hP.png",
        "content": data
    }

    response = requests.post(discord_webhook, json=payload)
    if response.status_code != 204:
        print(f"Failed to send Discord webhook: {response.status_code} {response.text}")

def auto_sign_function(profile):
    urlsnheaders = []

    if profile.get("genshin"):
        urlsnheaders.append({
            "url": url_dict["Genshin"],
            "headers": {"Cookie": profile["token"], **header_dict["default"]}
        })
    if profile.get("honkai_star_rail"):
        urlsnheaders.append({
            "url": url_dict["Star_Rail"],
            "headers": {"Cookie": profile["token"], **header_dict["default"]}
        })
    if profile.get("honkai_3"):
        urlsnheaders.append({
            "url": url_dict["Honkai_3"],
            "headers": {"Cookie": profile["token"], **header_dict["default"]}
        })
    if profile.get("tears_of_themis"):
        urlsnheaders.append({
            "url": url_dict["Tears_of_Themis"],
            "headers": {"Cookie": profile["token"], **header_dict["default"]}
        })
    if profile.get("zenless_zone_zero"):
        urlsnheaders.append({
            "url": url_dict["Zenless_Zone_Zero"],
            "headers": {"Cookie": profile["token"], **header_dict["default"], **header_dict["Zenless_Zone_Zero"]}
        })

    response = f"Check-in completed for {profile['accountName']}"

    for urlnheaders in urlsnheaders:
        time.sleep(1)  # To prevent rate-limiting
        res = requests.post(urlnheaders["url"], headers=urlnheaders["headers"])
        
        if res.status_code == 200:
            response_json = res.json()
            message = response_json.get("message", "Unknown error")
            game_name = [key for key, val in url_dict.items() if val == urlnheaders["url"]][0]

            if response_json.get("retcode") != 0:
                response += f"\n{game_name}: {discord_ping()}Auto check-in failed: {message}"
            else:
                response += f"\n{game_name}: {message}"
        else:
            response += f"\nRequest to {urlnheaders['url']} failed with status code {res.status_code}"

    return response

def main():
    messages = [auto_sign_function(profile) for profile in profiles]
    hoyolab_resp = "\n\n".join(messages)

    print(hoyolab_resp)
    if discord_notify:
        post_webhook(hoyolab_resp)

if __name__ == "__main__":
    main()