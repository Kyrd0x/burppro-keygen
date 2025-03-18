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

PROXIES = [

]

def generate_mail():
    firstname = random.choice(FIRSTNAMES).lower()
    lastname = random.choice(LASTNAMES).lower()
    symbol = random.choice(SYMBOLS)
    number = random.randint(0, 99)
    domain = ""
    email = firstname + symbol + lastname + str(number) + '@' + domain

def main():
    for _ in range(LIMIT):
        starttime = time.time()
        mail = generate_mail()
        # attendre reception d'un mail, timeout 10min


if __name__ == '__main__':
    main()