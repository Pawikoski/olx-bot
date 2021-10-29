from tinydb import TinyDB, Query
from bs4 import BeautifulSoup
from date import format_date
import requests
import re


db = TinyDB('db.json')


def add_link():
    print("Enter anything but no link to exit")
    while True:
        link = input("Add link:")

        if "http" not in link and "olx.pl" not in link:
            break
        else:
            r = requests.get(link).content
            soup = BeautifulSoup(r, 'html.parser')

            date = soup.find("span", {"data-cy": "ad-posted-at"})

            if date is not None:
                date = date.text

                title = soup.find("h1", {"data-cy": "ad_title"}).text

                price_div = soup.find("div", {"data-testid": "ad-price-container"})
                price = int(''.join(re.findall(r'[0-9]', price_div.find("h3").text)))

                print(price)

                date = format_date(date)
                db.insert({'link': link,
                           'title': title,
                           'price': price,
                           'date': date})
                print(date)


def check_links():
    pass


if __name__ == "__main__":
    add_link()
