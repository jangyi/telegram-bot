# HTTP API = 729021332:AAHM6EhXiWyZOpilp12RQGX8x6Idfjy3TIw

import requests
from bs4 import BeautifulSoup
import os
import time

import telegram

bot = telegram.Bot(token='729021332:AAHM6EhXiWyZOpilp12RQGX8x6Idfjy3TIw')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

while True:
    req = requests.get('http://heroes.nexon.com/community/userbbs/list')
    req.encoding = 'utf-8'

    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    posts = soup.find("span", {"class": "tx"}).text
    #latest = posts[0].text

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'r+', encoding='utf-8') as f_read:
        before = f_read.readlines()
        if before != posts:
            bot.sendMessage(chat_id=chat_id, text='새 글이 올라왔어요!')

        else:
            bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')

        f_read.close()

    with open(os.path.join(BASE_DIR, 'latest.txt'), 'w+', encoding='utf-8') as f_write:
        f_write.write(posts)
        f_write.close()

    time.sleep(30) # 60초(1분)을 쉬어줍니다.

