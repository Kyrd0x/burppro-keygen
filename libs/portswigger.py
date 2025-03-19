import requests

URL = "https://portswigger.net/burp/pro/trial"

def init():
    try:
        response = requests.get(URL)
        session_id = response.cookies["SessionId"]
        csrf_token = response.text.split('name="RequestVerificationToken"')[1].split('value=')[1].split(">")[0]
        return session_id, csrf_token
    except Exception as e:
        print(f"Error while initializing session: {e}")
        return None
        
def fill_mail(mail, token):
    try:
        response = requests.post(URL, data={"Email": mail, "RequestVerificationToken": token})
        print(response.text)
    except Exception as e:
        print(f"Error while filling email: {e}")
        return None

def request_trial(mail, message):
    name, domain = mail.split('@')
    session_id, token = init()
    if not session_id:
        return
    
    fill_mail(mail, token)
    
