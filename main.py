import requests
from flask import Flask, request

BOT_TOKEN = "BURAYA_BOT_TOKEN"
CHAT_ID = "BURAYA_CHAT_ID"

app = Flask(__name__)

def send_telegram(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": text}
    requests.post(url, data=data)

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    symbol = data.get("symbol","")
    signal = data.get("signal","")
    tf = data.get("tf","")
    price = data.get("price","")
    send_telegram(f"{symbol} {tf} {signal} {price}")
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return "R-DESK OK"
