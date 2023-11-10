import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("http://quotes.toscrape.com/tag/humor/")
soup = BeautifulSoup(page.text, "html.parser")
quotes = soup.findAll("span", attrs={"class":"text"})
authors = soup.findAll("small", attrs={"class":"author"})

quotes_csv = open("quotes.csv", "w")
writer = csv.writer(quotes_csv)

writer.writerow(["Quote", "Author"])

for quote, author in zip(quotes,authors):
    print(f"{quote.text} - {author.text}")
    writer.writerow([quote.text, author.text])
quotes_csv.close()