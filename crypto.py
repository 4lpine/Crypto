import requests
import json
import os
import match
import sys
from colorama import Fore

coin_urls = {
    "BTC" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bitcoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "ETH" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=ethereum&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "BNB" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bnb&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "DOGE" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=dogecoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "SHIB" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=shiba-inu&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "XMR" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=monero&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "LTC" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=litecoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "BTT" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bittorrent-new&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "USD" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=tether&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
}

os.system("cls")

def price(coin, amount):
    r = requests.get(coin_urls[coin.upper()])
    crypto = json.loads(r.content)
    return crypto['data']['marketPairs'][0]['price'] * amount

amount = sys.argv[1]
coin1 = sys.argv[2]
coin2 = sys.argv[3]

print(f"Converting {Fore.WHITE}{amount} {Fore.LIGHTBLACK_EX}{coin1}{Fore.WHITE} to {Fore.LIGHTBLACK_EX}{coin2}...{Fore.RESET}")

x = price(coin1, int(amount))
y = price(coin2, 1)

print(f"{Fore.WHITE}{amount} {Fore.LIGHTBLACK_EX}{coin1} = {Fore.MAGENTA}{round(x / y, 8)} {Fore.LIGHTBLACK_EX}{coin2}{Fore.RESET}")



