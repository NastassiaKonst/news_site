import requests
from bs4 import BeautifulSoup

url = 'https://habr.com/ru/news/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'}
page_number = 10
page_list = ['page1/', 'page2/', 'page3/', 'page4/', 'page5/', 'page6/', 'page7/', 'page8/', 'page9/', 'page10/']


def get_html(url, parameters=None):
    r = requests.get(url, headers=HEADERS, params=parameters)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='tm-article-snippet')
    news = []
    for el in items:
        image = ''
        if len(el.find_all('img')) > 1:
            image = el.find_all('img')[-1].get('src')
        url = 'https://habr.com' + el.find('a', class_='tm-article-snippet__title-link').get('href')
        news_dictionary = {
            'header': el.find('h2', class_='tm-article-snippet__title tm-article-snippet__title_h2').get_text(),
            'news_url': url,
            'annotation': el.find('div', class_='tm-article-body tm-article-snippet__lead').get_text(
                strip=True).replace('Читать дальше →', '').replace('Читать далее', ''),
            'image': image,
        }
        html = requests.get(url, headers=HEADERS, params=None)
        soup = BeautifulSoup(html.text, 'html.parser')
        items = soup.find_all('article', class_='tm-article-presenter__content')
        for el in items:
            news_dictionary['full_text'] = el.find('div', class_='article-formatted-body').get_text(strip=True)
        news.append(news_dictionary)
    return news


def parsing():
    html = get_html(url + page_list[0])
    if html.status_code == 200:
        return get_content(html.text)
    else:
        return 'error'
    #i = 0
    #while i < page_number:
    #    html = get_html(url + page_list[i])
    #    if html.status_code == 200:
    #        print(get_content(html.text))
    #    else:
    #        print('error')
    #    i = i + 1

