import time, os
import telegram
import urllib.request
from bs4 import BeautifulSoup

last_file = os.environ.get('new_file')

API_KEY = '914333031:AAEobLa1UpdCokJu5MzNpG8S6eALbl2Tu6M'
bot = telegram.Bot(token=API_KEY)

chat_id = '814915551'

Book_mark = ['데스러버', '액터쥬(act-age)', '나의 히어로 아카데미아',\
             '원펀맨 리메이크', '전생현자의 이세계 라이프',\
             '호리미야 리메이크', '여친, 빌리겠습니다', '남고생을 기르고 싶은',\
             '5분 후의 세계', '고2로 타임슬립한 내가', '5등분의 신부',\
             '유라기장', '이삿짐 정리가 끝나지 않아', '여친 가챠',\
             '카구야님은 고백 받고 싶어', '도게자해서 부탁해봤다',\
             '도서관의 대마술사', '암살자인 내 스테이더스가 용사보다',\
             '현자의 제자를 자칭하는 현자', '싫은 얼굴을 하면서',\
             '어서오세요 실력지상주의 교실에', '거미입니다만',\
             '누이 되는 자', '블랙 클로버']
while True:
    URL = 'https://manamoa12.net/bbs/board.php?bo_table=manga'
    req = urllib.request.Request(URL, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req)
    bs = BeautifulSoup(html.read(), 'html.parser')
    
    new = bs.find('a', {'style': 'font-size:16px'})
    new = new.get_text()
    remove = new.rfind('화')
    if remove == -1:
        remove = new.rfind('편')
    new = new[5:remove+1]
    
    if last_file != new:
        for i in range(len(Book_mark)):
            if Book_mark[i] in new:
                message = new + '가 업데이트 되었습니다.'
                bot.sendMessage(chat_id=chat_id, text=message)
        os.environ['new_file'] = new
    time.sleep(10)
