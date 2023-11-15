from requests_html import HTML

with open ('requests-html/htmlscraper.html') as html_file:
    source = html_file.read()
    html = HTML(html=source)

# Using title index method
title = html.find("title")
print(title[0].text)

# Using first keyword to get the first title in the iteration
title1 = html.find("title", first=True)
print(title1.text)

# Getting the first heading using id name
heading = html.find("#title", first=True)
print(heading.text)

# Getting the information within the first div tag
articles = html.find("div.article")
for article in articles:
    header = article.find('h2', first=True).text
    summary = article.find('p', first=True).text
    print(header)
    print(summary)
    print()

