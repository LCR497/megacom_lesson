import requests
from bs4 import BeautifulSoup
import csv

def get_data():
    url = 'https://www.sulpak.kg/f/smartfoniy'
    r = requests.get(url, verify=False)    # def get_data()
    soup = BeautifulSoup(r.content, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    return items

# fa fa-star active

def parse_data():
    result = []
    for item in get_data():
        if type(item.find('div', class_='old-price')) == type(None):
            result.append({
                'title': item.find('h3', class_='title').get_text().strip().replace('\n', ''),
                'price': item.find('div', class_='price').get_text().strip().replace('\n', ''),
                # 'old_price': item.find('div', class_='old-price').get_text().strip().replace('\n', ''),
                'img': item.find('img')['src'],
                'old-price' : 'Нет старой цены',
                'star': item.find('a', class_='rating-container starts-to-comments').get_text().strip().replace('\n','')
            })
        else:
            result.append({
                'title' : item.find('h3', class_='title').get_text().strip().replace('\n', ''),
                'price' : item.find('div', class_='price').get_text().strip().replace('\n', ''),
                # 'old_price': item.find('div', class_='old-price').get_text().strip().replace('\n', ''),
                'img' : item.find('img')['src'],
                'old-price' : item.find('div', class_='old-price').get_text().strip().replace('\n', ''),
                'star' : item.find('a', class_='rating-container starts-to-comments').get_text().strip().replace('\n', ''),
            })
    return result


def save_data():
    with open('result.csv', 'w') as f:   # def save_data()
        writer = csv.DictWriter(f, fieldnames=['title', 'price', 'old-price', 'star', 'img'])
        writer.writeheader()
        writer.writerows(parse_data())

def main():
    save_data()

if __name__ == '__main__':
    main()

# import requests
# from bs4 import BeautifulSoup
# from pprint import pprint
# import csv
#
#
# r = requests.get('https://www.sulpak.kg/f/smartfoniy', verify=False)    # def get_data()
# soup = BeautifulSoup(r.content, 'html.parser')
# items = soup.findAll('div', class_='goods-tiles')
#
# result = []
# for item in items:
#     result.append({
#         'title' : item.find('h3', class_='title').get_text().strip().replace('\n', ''),
#         'price' : item.find('div', class_='price').get_text().strip().replace('\n', ''),
#     })    # def parse_data()
#
# with open('result.csv', 'w') as f:   # def save_data()
#     writer = csv.DictWriter(f, fieldnames=['title', 'price'])
#     writer.writeheader()
#     writer.writerows(result)