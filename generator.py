from bs4 import BeautifulSoup
import configparser
import requests
import yopmail
import random
import string
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
    letters = string.ascii_lowercase + string.digits
    salt_size = random.randint(2, 6)
    salt = ''.join(random.choice(letters) for _ in range(salt_size))
    domain = "yopmail.com"  #to change 
    email = firstname + symbol + lastname + salt + '@' + domain
    return email

def check_emails(email):
    url = f"http://www.yopmail.com/fr/inbox.php?login={email}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Erreur lors de l'accès à la boîte de réception.")
        print(f"Code d'erreur : {response.status_code}")
        print(f"Contenu de la réponse : {response.text}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Trouver les e-mails dans la page (les e-mails sont dans des éléments spécifiques)
    emails = soup.select(".lm")  # Sélecteur CSS pour les lignes d'e-mails
    
    if not emails:
        print("Aucun e-mail trouvé pour l'instant.")
        return
    
    print(f"E-mails reçus pour {email} :")
    for email_item in emails:
        subject = email_item.text.strip()
        print(f"- Sujet : {subject}")

def main():
    for _ in range(EMAILS_AMOUNT):
        start_time = time.time()
        proxy = get_proxy()
        mail = generate_mail()
        print(f"Using proxy: {proxy} and {mail}")

        yopmail.get_mails(mail, proxy)
        print(f"Temps écoulé : {time.time() - start_time:.2f}s\n")
        # attendre reception d'un mail, timeout 10min
        time.sleep(1)


if __name__ == '__main__':
    main()