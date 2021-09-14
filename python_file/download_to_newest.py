import requests
from bs4 import BeautifulSoup
import os


setting_dir = 'setting'

setting = dict()

with open(os.path.join(setting_dir, 'user_setting.txt'), 'r') as f:
    setting = eval(f.read());

username = setting['username']
password = setting['password']
save_path = setting['save_path']

with open(os.path.join(setting_dir, 'so_far.txt'), 'r') as f:
    so_far_num = int(f.read());

basic_url = 'http://li.nu/attrade/gachalist.php?gacha='
index_url = 'http://li.nu/attrade/gacha.php'
index_page = requests.get(index_url)
soup = BeautifulSoup(index_page.text, 'lxml')
newest_url = soup.find('div', class_='info').find('a').get('href')
newest_num = int(newest_url.split('=')[-1])

i = so_far_num + 1

rec = open(os.path.join(save_path,'record.txt'), 'w', encoding='UTF-8')

while i <= newest_num:
    print(str(i) + ' start!')
    url = basic_url + str(i)
    pic_page = requests.get(url)
    soup = BeautifulSoup(pic_page.text,'lxml')

    try:
        name = soup.find('div',id='info').find('h2').get_text()
    except:
        print('編號不存在')
        text = str(i) + " 編號不存在!" + "\n"
        rec.write(text)
        print(str(i) + ' None!')
        i += 1
        continue

    for j in ['\\', '/', ':', '*', '?', '"', '<', '>', '|','.']:
        position = 0
        while 1:
            position = name.find(j, position)
            if position == -1:
                break
            name = name.replace(j, "_", 1)

    name = str(i) + "_" + name

    while(name.endswith((" "))):
        name = name[0:-1]

    dir_path = os.path.join(save_path, name)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)

    try:
        images = soup.find('ul', class_='itemlist').find_all('li')
    except:
        print('沒有圖片')
        text = name + " 沒有圖片!" + "\n"
        rec.write(text)
        print(str(i) + ' None!')
        i += 1
        continue

    for img in images:
        img_url = img.find('div',class_='image').find('a',class_='zoom-img').get('href')


        if(img_url.endswith('swf')):
            img_url = 'http://li.nu/attrade/'+img_url

        file_name = img_url.split('/')[-1]

        pic = requests.get(img_url)
        if not os.path.exists(os.path.join(dir_path, file_name)):
            with open(os.path.join(dir_path, file_name), 'wb') as f:
                f.write(pic.content)



    try:
        origin_url = soup.find('a',text='@games内のページを確認').get('href')
    except:
        print('找不到官網')
        text = name + " 找不到官網!" + "\n"
        rec.write(text)
        print(str(i) + ' finish!')
        i += 1
        continue

    if(origin_url.startswith('http://www.atgames.jp/')):
        print('舊版官網,不存在')
        text = name + " 舊版官網問題!" + "\n"
        rec.write(text)
        print(str(i) + ' finish!')
        i += 1
        continue

    origin_site = requests.get(origin_url)
    soup = BeautifulSoup(origin_site.text, 'lxml')

    one_pic = 0
    mult_pic = 0

    URL = 'https://sp.atgames.jp/pocketland/access/login/complete'
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
    form_data = {'userId':username, 'password':password}

    try:
        soup.find('section',class_='loginFormSec')
        if(username=='' or password==''):
            text = name + " finish!" + "\n"
            rec.write(text)
            print(str(i) + ' finish!')
            i += 1
            continue
        else:
            session = requests.Session()
            session.post(url=URL, headers=header, data=form_data)
            origin_site = session.get(origin_url)
            soup = BeautifulSoup(origin_site.text, 'lxml')

    except:
        print('非登入頁面')

    try:
        header_url = soup.find('section',id='Header').find('img').get('src')
        one_pic = 1
    except:
        print('非特典頁面')

    try:
        img_list = soup.find('div',class_='mod_wysiwyg').find_all('img',limit=2)
        mult_pic = 1
    except:
        print('非活動主頁面')

    if one_pic == 1:
        file_name = header_url.split('/')[-1]
        pic = requests.get(header_url)
        if not os.path.exists(os.path.join(dir_path, file_name)):
            with open(os.path.join(dir_path, file_name), 'wb') as f:
                f.write(pic.content)

    elif mult_pic == 1:
        for img in img_list:
            img_url = img.get('src')
            file_name = img_url.split('/')[-1]
            pic = requests.get(img_url)
            if not os.path.exists(os.path.join(dir_path, file_name)):
                with open(os.path.join(dir_path, file_name), 'wb') as f:
                    f.write(pic.content)

    if(one_pic==1 or mult_pic==1):
        text = name + " finish!" + "\n"
    else:
        text = name + " error!" + "\n"

    rec.write(text)
    print(str(i) + ' finish!')
    i += 1

rec.close()
with open(os.path.join(setting_dir, 'so_far.txt'), 'w') as f:
    f.write(str(newest_num))

print('finish!')
os.system("pause")