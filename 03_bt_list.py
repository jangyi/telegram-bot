import urllib.request
from bs4 import BeautifulSoup
import os
import time

import telegram

bot = telegram.Bot(token='729021332:AAHM6EhXiWyZOpilp12RQGX8x6Idfjy3TIw')
chat_id = bot.getUpdates()[-1].message.chat.id

# 파일의 위치
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

URL = 'http://battlerite.nexon.com/community/free/list'

while True:
    source_code_from_URL = urllib.request.urlopen(URL)
    soup = BeautifulSoup(source_code_from_URL, 'lxml', from_encoding='utf-8')
    text = ''
    for item in soup.find_all('span', {"class":"txt"}):
        text = text + str(item.find_all(text=True))

    with open(os.path.join(BASE_DIR, 'bt_list.txt'), 'r+', encoding='utf-8') as f_read:
        before = f_read.readline()

        if before != text:
            bot.sendMessage(chat_id=chat_id, text='배틀라이트 새 글이 올라왔어요!')

        else:
            bot.sendMessage(chat_id=chat_id, text='새 글이 없어요 ㅠㅠ')

        f_read.close()

    with open(os.path.join(BASE_DIR, 'bt_list.txt'), 'w+', encoding='utf-8') as f_write:
        f_write.write(text)
        f_write.close()

    time.sleep(60)  # 60초(1분)을 쉬어줍니
