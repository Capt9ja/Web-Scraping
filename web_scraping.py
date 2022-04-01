from bs4 import BeautifulSoup
import requests

website_link = "https://books.toscrape.com/catalogue/page-2.html"
request = requests.get(website_link)
html = request.content
scraped = BeautifulSoup (html, 'html.parser')

result = []
scraping = scraped.find_all("article", class_= "product_pod")
print(scraping)
for scraping in scraping:
  title = scraping.h3.a["title"]
  price = scraping.find("p", class_="price_color")
  real_price = float(price.text.lstrip("£"))
  availability = scraping.find("p", class_="instock availability")
  result.append({title: real_price})
print(result)
