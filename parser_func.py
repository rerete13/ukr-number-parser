from bs4 import BeautifulSoup as bs
import requests as rq
from pprint import pprint as pp
from numba import njit




def parser_num(num: str):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://baza-gai.com.ua/nomer/{num}'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'lxml')

    return html


def parser_regions():    
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    url = f'https://baza-gai.com.ua/regions'
    r = rq.get(url, headers=headers)
    html = bs(r.content, 'lxml')

    return html


    
def parser(link:str):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    r = rq.get(link, headers=headers)
    html = bs(r.content, 'lxml')

    return html


def get_regions_index_choose(index:int):
    arr = []
    main_object = parser_regions()
    region = main_object.find_all('tbody')
    region = region[0].find_all('tr')
    region = region[index]
    region = region.find_all('td')
    region = region[1:]
    for i in region[:2]:
        arr.append(i.text)
    
    region = region[-1].text
    
    for i in region.split(','):
        arr.append(i.strip())


    return arr

    
    
    