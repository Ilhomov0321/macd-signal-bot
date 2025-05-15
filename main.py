import time
from data_fetcher import fetch_data
from macd_calculator import calculate_macd, get_macd_signal
from notifier import send_telegram_message

LOG_FILE = 'signal_log.txt'

def load_last_signal():
    try:
        with open(LOG_FILE, 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return "NO SIGNAL"

def save_last_signal(signal):
    with open(LOG_FILE, 'w') as f:
        f.write(signal)

def main_loop():
    while True:
        print("🔄 Tekshirish boshlandi...")

        df = fetch_data(symbol="XAUT/USDT", timeframe="15m", limit=100)

        if df.empty:
            print("❌ Ma'lumotlar olinmadi.")
        else:
            df = calculate_macd(df)
            signal = get_macd_signal(df)
            last_signal = load_last_signal()

            if signal != "NO SIGNAL" and signal != last_signal:
                message = f"📢 Yangi signal: {signal} (XAUT/USDT)"
                send_telegram_message(message)
                save_last_signal(signal)
                print("✅ Yangi signal yuborildi:", message)
            else:
                print(f"⏸️ Signal o'zgarmagan yoki yo'q: {signal}")

        print("🕒 15 daqiqa kutyapmiz...\n")
        time.sleep(900)

if __name__ == "__main__":
    main_loop()
