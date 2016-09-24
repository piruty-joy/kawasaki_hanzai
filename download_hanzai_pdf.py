# coding: utf-8

import urllib.request
from bs4 import BeautifulSoup


def download_pdf(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    kiji_atag = soup.findAll('div', class_='main_naka_kiji')[0].findAll('a')

    for atag in kiji_atag:
        href = atag.get('href')
        with urllib.request.urlopen('http://www.city.kawasaki.jp/250' + href[1:]) as pdf:
            with open('pdf/' + href.split('/')[-1], 'wb') as local:
                local.write(pdf.read())

url_list = [
    'http://www.city.kawasaki.jp/250/page/0000055800.html',
    'http://www.city.kawasaki.jp/250/page/0000058168.html',
    'http://www.city.kawasaki.jp/250/page/0000066485.html'
]

for url in url_list:
    download_pdf(url)
