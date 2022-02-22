import requests
import json

from bs4 import BeautifulSoup
from Product import Product

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
    "accept": "application/json",
}

data = {

}

x = requests.get(
    "https://www.willhaben.at/iad/kaufen-und-verkaufen/marktplatz/grafikkarten-5882?sfId=9ac621c3-f17d-4ee4-a942-6fd0ed535911&isNavigation=true",
    headers=headers)

soup = BeautifulSoup(x.content, "html.parser")
y = soup.find("script", {"id": "__NEXT_DATA__"}).getText()
all_products = json.loads(y)["props"]["pageProps"]["searchResult"]["advertSummaryList"]["advertSummary"]

parsed_products = []

for product in all_products:
    try:
        id = product["id"]
        name = product["description"]
        description = [x for x in product["attributes"]["attribute"] if x["name"] == "BODY_DYN"][0]["values"][0]

        if product["advertImageList"]["advertImage"]:
            image_url = product["advertImageList"]["advertImage"][0]["mainImageUrl"]
        else:
            image_url = "https://media0.giphy.com/media/9J7tdYltWyXIY/giphy.gif?cid=ecf05e476gmuk8659qslcu092vo7y6yi7pdoq2vzm936vnft&rid=giphy.gif&ct=g"

        price = [x for x in product["attributes"]["attribute"] if x["name"] == "PRICE/AMOUNT"][0]["values"][0]
        url = "https://www.willhaben.at/iad/" + \
              [x for x in product["attributes"]["attribute"] if x["name"] == "SEO_URL"][0]["values"][0]
        location = [x for x in product["attributes"]["attribute"] if x["name"] == "LOCATION"][0]["values"][0]
        uploaded_at = [x for x in product["attributes"]["attribute"] if x["name"] == "PUBLISHED_String"][0]["values"][
            0].replace("T", " ").replace("Z", "")
        pay_livery = [x for x in product["attributes"]["attribute"] if x["name"] == "p2penabled"][0]["values"][0]

        pr = Product(id=id, name=name, description=description, image_url=image_url, price=price, location=location,
                     url=url, uploaded_at=uploaded_at, pay_livery=pay_livery)
        parsed_products.append(pr)

    except Exception as e:
        print(e)
        print(product)

print(parsed_products)
