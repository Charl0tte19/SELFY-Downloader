import requests
from bs4 import BeautifulSoup
import os

save_path = 'setting'

url = 'https://sp.atgames.jp/pocketland/information/list/index?placeId=38'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
form_data = {'placeId': 38, 'pageNo': 0}
news_page = requests.post(url='https://sp.atgames.jp/pocketland/information/list/show',headers=header,data=form_data)

#print(news_page.json()['parts'])

soup = BeautifulSoup(news_page.json()['parts'],'lxml')
tags = soup.find_all('ul',class_='transitionsUl')

for tag in tags:
    t = tag.find('a')
    if 'ガチャ' in t.get_text():
        newest_url = t.get('href')
        site = requests.get(newest_url)
        soup = BeautifulSoup(site.text,'lxml')
        pic_url = soup.find('div',class_='mod_wysiwyg').find('img').get('src')
        if 'header' in pic_url:
            pic = requests.get(pic_url)

        with open(os.path.join(save_path,'newest.png'),'wb') as f:
            f.write(pic.content)
        break

print('finish!')
