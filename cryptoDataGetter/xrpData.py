from requests_html import HTML, HTMLSession

session = HTMLSession()
response = session.get("https://coinmarketcap.com/currencies/xrp/historical-data/")

main_div = response.html.find("#__next", first=True)
div1 = main_div.html.find()