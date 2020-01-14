import requests # module to make http/https requests
import html5lib # a small parser package for html-5
from bs4 import BeautifulSoup

amazon_link = "https://www.amazon.com/HP-Touchscreen-Computer-Quard-Core-802-11ac/dp/B082PZVZB7/ref=sr_1_2_sspa?keywords=laptop&qid=1579030386&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExMVdJU0dVOUJaSUtOJmVuY3J5cHRlZElkPUExMDQ0MDk5MjM2Q0pUMlFFNEZJMiZlbmNyeXB0ZWRBZElkPUEwNTAwMTAwMUZDMlpGTDNJVjM4TSZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"

agent_header = {
		"User-Agent" : agent
}

amazon_page = requests.get(amazon_link, headers = agent_header)

#print(type(amazon_page))
soup = BeautifulSoup(amazon_page.content, "html5lib")

price_span = str(soup.find(id = "priceblock_ourprice"))
print(price_span)


price = ""
for char in price_span:
	if char.isdigit() is True:
		price += char
	if char == ".":
		price += char

print(price)
price = float(price)
max_price = 800
if price <= max_price:
	print("yo you can buy it now")













