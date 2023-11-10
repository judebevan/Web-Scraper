import pandas as pd
import requests
from bs4 import BeautifulSoup


def get_crypto_table():
    url = "https://finance.yahoo.com/crypto/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find_all('table')[0]
    df = pd.read_html(str(table))[0]
    return df


crypto_df = get_crypto_table()
print(crypto_df)