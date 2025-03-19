import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

NAME = "john.doe654"

def get_query(name):
    return f"Hi, I'd like to request a trial of Burpsuite Pro. My name is {name}. Please answer only these few sentences as I will copy and paste them. Thanks."

def get_response(name):
    return model.generate_content(get_query(name)).text
