from bs4 import BeautifulSoup
import requests

def get_mails(name, proxy):
    url = f"https://www.yopmail.com/fr/wm"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Cookie": f"ywm={name}",
        "Cookie": f"yc=RZwZlZwV3AGD0ZQt1ZQZjAQR",
        "Cookie": f"yses=nT464mdLhKGXsXe/Tjz639oqxlfnPhAaRIDKqTilg4wMelbwJD27mPcivLyFqjIm",
        "Cookie": "compte=123456:lenorme:toto"
    }
    response = requests.get(url, proxies={'http': proxy}, headers=headers)
    if response.status_code != 200:
        print("Erreur lors de l'accès à la boîte de réception.")
        print(f"Code d'erreur : {response.status_code}")
        print(f"Contenu de la réponse : {response.text}")
        return

    # soup = BeautifulSoup(response.text, 'html.parser')
    
    # # Trouver les e-mails dans la page (les e-mails sont dans des éléments spécifiques)
    # emails = soup.select(".lm")  # Sélecteur CSS pour les lignes d'e-mails
    
    # if not emails:
    #     print("Aucun e-mail trouvé pour l'instant.")
    #     return
    
    print(f"E-mails reçus pour {name} :")
    print(response.text)
    # for email_item in emails:
    #     subject = email_item.text.strip()
    #     print(f"- Sujet : {subject}")
    # return emails