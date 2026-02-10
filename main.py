import requests
from flask import Flask, request

BOT_TOKEN = "8257960571:AAGqlVkb_NYx5es_5Lm55XPEALng9RpYCD4"
CHAT_ID = "7198009222"

app = Flask(__name__)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, data=payload)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    if not data:
        return "no data"

    symbol = data.get("symbol", "")
    signal = data.get("signal", "")
    tf = data.get("tf", "")
    price = data.get("price", "")

    msg = f"📊 {symbol}\n⏱ {tf}\n📌 SİNYAL: {signal}\n💰 Fiyat: {price}"
    send_telegram(msg)

    return "ok"

@app.route("/")
def home():
    return "R-DESK BOT AKTIF"
