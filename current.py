from dotenv import load_dotenv
import os
import requests
load_dotenv()
os.system('cls')
weather_api = os.getenv("API_KEY")

print(f"Cheia API este: {weather_api}")