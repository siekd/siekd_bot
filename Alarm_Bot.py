import os, time
import telegram
import urllib.request
from bs4 import BeautifulSoup

API_KEY = os.environ["BOT_TOKEN"]
bot = telegram.Bot(token=API_KEY)

chat_id = '814915551'

Book_mark = ['명탐정 코난', '액터쥬(act-age)', '아무튼 귀여워']

while True:
    URL = 'https://manamoa12.net/bbs/board.php?bo_table=manga'
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    bs = BeautifulSoup(html.read(), 'html.parser')

    nameList = bs.findAll('a', {'style': 'font-size:16px'})
    New_list = []
    Fix_list = []
    Upload_list = []

    for name in nameList:
    New_list.append(name.get_text())
    for i in New_list:
    remove = i.rfind('화')
    if remove == -1:
        remove = i.rfind('편')
    Fix_list.append(i[5:remove+1])

    f = open('Log.txt', 'r+', encoding='UTF8')
    save = f.readlines()
    revise = []

    for i in range(len(save)):
        temp = save[i].replace('\n', '')
        revise.append(temp)

    if Fix_list != revise:
    for i in range(len(Fix_list)):
        for j in range(len(Book_mark)):
            if Book_mark[j] in Fix_list[i]:
                message = Fix_list[i] + ' 업데이트 되었습니다.'
                bot.sendMessage(chat_id=chat_id, text=message)
    f.close()
    for i in range(len(Fix_list)):
        temp = Fix_list[i] + '\n'
        Upload_list.append(temp)

    with open('Log.txt', 'w', encoding='UTF8') as file:
        file.writelines(Upload_list)

    f.close()
    time.sleep(60)
