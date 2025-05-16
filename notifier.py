import requests

BOT_TOKEN = "7459341936:AAGF4xcm-ESyYT8BFtwGJDtNFUHB36a"
CHAT_ID = " 1673000"

def send_telegram_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    try:
        response = requests.post(url, data=payload)
        if response.status_code != 200:
            print("❌ Telegramga yuborishda xatolik:", response.text)
    except Exception as e:
        print("❌ Yuborishda xatolik:", e)
