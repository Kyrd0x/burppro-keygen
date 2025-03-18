from bs4 import BeautifulSoup
import requests
import random
import json
import time

LIMIT = 10

# 10 minutes
TIMEOUT = 10*60

SYMBOLS = ['.', '-', '_']

with open('wordlists/firstnames.txt', 'r') as f:
    FIRSTNAMES = f.read().splitlines()

with open('wordlists/lastnames.txt', 'r') as f:
    LASTNAMES = f.read().splitlines()

PROXIES_API = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
PROXY_TIMEOUT = 30

def get_proxy():
    start_time = time.time()
    while True:
        response = requests.get(PROXIES_API)
        proxies = response.text.splitlines()
        proxy = random.choice(proxies)
        if is_valid_proxy(proxy):
            return proxy
        if time.time() - start_time > PROXY_TIMEOUT:
            raise Exception("[TIMEOUT] No valid proxy found")
        

def is_valid_proxy(proxy):
    try:
        _response = requests.get('https://api.ipify.org', proxies={'http': proxy}, timeout=3)
        return True
    except:
        return False

def generate_mail():
    firstname = random.choice(FIRSTNAMES).lower()
    lastname = random.choice(LASTNAMES).lower()
    symbol = random.choice(SYMBOLS)
    number = random.randint(0, 99)
    domain = ""
    email = firstname + symbol + lastname + str(number) + '@' + domain

def main():
    for _ in range(LIMIT):
        start_time = time.time()
        proxy = get_proxy()
        print(f"Using proxy: {proxy} (valid={is_valid_proxy(proxy)})")
        mail = generate_mail()
        # attendre reception d'un mail, timeout 10min
        time.sleep(1)


if __name__ == '__main__':
    main()