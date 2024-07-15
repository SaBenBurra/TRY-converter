from enum import Enum
import requests
from lxml import etree

DATA_URL = "https://api.genelpara.com/iframe/?symbol=para-birimleri&pb=USD,EUR"

USD_XPATH = "/html/body/div/div/div/ul[1]/li[3]/span"
EUR_XPATH = "/html/body/div/div/div/ul[2]/li[3]/span"

class Currency(Enum):
    USD = "USD"
    EUR = "EUR"

def get_data():
    response = requests.get(DATA_URL)
    return response.text

def scrape(data: str, curency: Currency):
    tree = etree.HTML(data)
    value = tree.xpath(globals()[curency.value + "_XPATH"])[0]
    return value.text

def convert(amount: float, from_try: bool, currency: Currency):
    data = get_data()
    value = float(scrape(data, currency).replace(",", "."))
    return amount / value if from_try else value * amount

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 4:
        print("argument error")
        sys.exit(1)

    amount = float(sys.argv[1])
    from_try = True if sys.argv[2] == "1" else False
    currency = Currency(sys.argv[3].upper())

    result = convert(amount, from_try, currency)
    result = float(f"{result:.2f}")
    print(str(result) + " " + (currency.value if from_try else "TRY"))
