from tinydb import TinyDB, Query, where
from bs4 import BeautifulSoup
from date import format_date
import requests
import re


db = TinyDB('db.json')


def add_link():
    print("Enter anything but no link to exit")
    while True:
        link = input("Add link: ")

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

                date = format_date(date)

                # views = soup.find("span", {"data-testid": "page-view-text"}).text
                # print(views)

                auction_data = {
                    'link': link,
                    'title': title,
                    'price': price,
                    'date': date
                }

                does_exist(auction_data)


def update_db(auction_data, search_result):
    old_title = search_result[0]['title']
    old_price = search_result[0]['price']
    old_date = search_result[0]['date']

    new_title = auction_data['title']
    new_price = auction_data['price']
    new_date = auction_data['date']
    link = auction_data['link']

    new_auction_data = dict()
    new_auction_data['link'] = link

    if old_title != new_title:
        print("Title has been changed.")
        new_auction_data['title'] = new_title

    if old_price != new_price:
        print("Price has been changed.")
        new_auction_data['price'] = new_price

    if old_date != new_date:
        print("Auction has been refreshed")
        new_auction_data['date'] = new_date

    if len(new_auction_data) > 1:
        user_choice = input("Some data in auction has been changed. Do you want to update database? (Y/N)")
        while True:
            if user_choice.lower() == "n":
                print("Database won't be updated")
                break
            elif user_choice.lower() == "y":
                print("Database will be updated")
                db.update({'title': new_title, 'price': new_price, 'date': new_date}, where('link') == link)
                break


def does_exist(auction_data: dict):
    q = Query()
    link = str(auction_data['link'])
    search_result = db.search(q.link == link)
    if len(search_result) > 0:
        print("Already exists in database!")

        update_db(auction_data, search_result)

    else:
        db.insert(auction_data)


def check_links():
    for record in db.all():
        r = requests.get(record['link'])


if __name__ == "__main__":
    while True:
        start = int(input("1 - add link\n2 - check all links"))
        match start:
            case 1:
                add_link()
            case 2:
                check_links()
