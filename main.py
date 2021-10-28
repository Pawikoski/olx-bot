from tinydb import TinyDB, Query
from bs4 import BeautifulSoup
from date import format_date
import requests


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
            date = soup.find("span", {"data-cy": "ad-posted-at"}).text
            date = format_date(date)
            # db.insert({'link': link})
            print(date)

def check_links():
    pass


if __name__ == "__main__":
    add_link()
