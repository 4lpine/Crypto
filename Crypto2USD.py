import requests
import json
import os
import match

coin_urls = {
    "BTC" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bitcoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "ETH" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=ethereum&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "BNB" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bnb&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "DOGE" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=dogecoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "SHIB" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=shiba-inu&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "XMR" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=monero&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "LTC" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=litecoin&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true",
    "BTT" : "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug=bittorrent-new&start=1&limit=1&category=spot&centerType=all&sort=cmc_rank_advanced&direction=desc&spotUntracked=true"
}

os.system("cls")

x = input("Enter the amount : ")
os.system("cls")
y = match.better_input("Enter the coin type -> ", ["BTC", "ETH", "BNB", "DOGE", "SHIB", "XMR", "LTC", "BTT", "btc", "eth", "bnb", "doge", "shib", "xmr", "ltc", "btt"])

os.system("cls")

def price(coin, amount):
    r = requests.get(coin_urls[coin])
    crypto = json.loads(r.content)
    return crypto['data']['marketPairs'][0]['price'] * amount

print(f"{float(x.upper())} {y.upper()} = {round(price(y.upper(), float(x.upper())), 2)}$ usd")


