import sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from config import finbee_password, finbee_username
import requests
from bs4 import BeautifulSoup


def login(user_name, password):
    with requests.session() as s:
        soup = BeautifulSoup(s.get('https://p2p.finbee.lt/prisijungti').content, 'html.parser')
        token = soup.find("meta", {"name":"csrf-token"})['content']
        print(print(token))

if __name__ == "__main__":
    login(finbee_username, finbee_password)

