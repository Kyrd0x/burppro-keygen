from bs4 import BeautifulSoup
import configparser
import requests
import random
import time
import os

config = configparser.RawConfigParser()
config.read(".conf")

EMAILS_AMOUNT = config.getint('General', 'emails')
TIMEOUT = config.getint('General', 'timeout')

PROXIES_API = config.get('Proxy', 'url')
PROXY_TIMEOUT = config.getint('Proxy', 'timeout')

SYMBOLS = ['.', '-', '_']

with open('wordlists/firstnames.txt', 'r') as f:
    FIRSTNAMES = f.read().splitlines()

with open('wordlists/lastnames.txt', 'r') as f:
    LASTNAMES = f.read().splitlines()

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
    for _ in range(EMAILS_AMOUNT):
        start_time = time.time()
        proxy = get_proxy()
        print(f"Using proxy: {proxy} (valid={is_valid_proxy(proxy)})")
        mail = generate_mail()
        # attendre reception d'un mail, timeout 10min

        time.sleep(1)


if __name__ == '__main__':
    main()