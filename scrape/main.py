import requests as r
from bs4 import BeautifulSoup

pagina = r.get("https://quotes.toscrape.com/")
texto = BeautifulSoup(pagina.text, 'html.parser')

frases = texto.find_all("span", itemprop="text")

for div in frases:
    print(div.text.strip())