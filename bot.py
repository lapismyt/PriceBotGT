import os
from geckoterminal_api import GeckoTerminalAPI
import time
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import threading

gt = GeckoTerminalAPI()

TG_TOKEN = os.getenv("PRICEBOT_TOKEN")
# POOL = os.getenv("PRICEBOT_POOL")
POOL = "EQA7xusA4i7BBlj65FiswpLbbhkiRFmQGyuhf4zpObzY09Ir" # TODO
CHAT = "-1002088821264"

INTERVAL = 3600

bot = telebot.TeleBot(TG_TOKEN)

GT_URL = "https://www.geckoterminal.com/ru/ton/pools/EQA7xusA4i7BBlj65FiswpLbbhkiRFmQGyuhf4zpObzY09Ir" # TODO
STONFI_URL = "https://app.ston.fi/swap?chartVisible=false&chartInterval=1w&ft=DFC&tt=EQDilWQKhM1wtm_us4PYvqU4bI2ljri5tfK0-01C7xdB938M&fa=370" # TODO

def main():
    while True:
        info = gt.network_pool_address("ton", POOL)
        info = info["data"]["attributes"]
        price_usd = float(info["base_token_price_usd"])
        price_quote = float(info["base_token_price_quote_token"])
        price_change_percentage_h1 = float(info["price_change_percentage"]["h1"])
        price_change_percentage_h24 = float(info["price_change_percentage"]["h24"])
        volume_h1 = float(info["volume_usd"]["h1"])
        volume_h24 = float(info["volume_usd"]["h24"])

        resp = f"Pool: {info['name']}\n"
        resp += f"Price: {round(price_quote, 4)} (${round(price_usd, 4)})\n\n"

        resp += f"Price changes:\n"
        resp += f"1H: {round(price_change_percentage_h1, 2)}\n"
        resp += f"24H: {round(price_change_percentage_h24, 2)}\n\n"

        resp += f"Volumes:\n"
        resp += f"1H: ${round(volume_h1, 2)}\n"
        resp += f"24H: ${round(volume_h24, 2)}\n"

        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("Geckoterminal", url=GT_URL)) # TODO
        markup.add(InlineKeyboardButton("STON.fi", url=STONFI_URL)) # TODO

        bot.send_message(CHAT, resp, reply_markup=markup)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
