# -*- coding: utf-8 -*-
#!/usrbin/env python
"""
Created on Jan 14 12:04 2021

@author: jaehyun
"""
import os
import time
import sys
import json
import requests
from bs4 import BeautifulSoup
#from time import sleep
from gtts import gTTS, gTTSError

import smtplib
from email.mime.text import MIMEText
import threading
 
def google_tts(stt_txt):
   file = "TTS_google_ko.mp3"
   try:
       tts= gTTS(text=stt_txt, lang='ko') # 읽고 싶은 문장과 언어를 넣는다.
   except (ValueError, AssertionError) as e:
       if('No text to speak' in str(e)):
           os.system("gst-play-1.0 No_text_to_speak.mp3")
   tts.save(file)
   os.system("gst-play-1.0 TTS_google_ko.mp3")
 
def analysis_word(stt_txt):
    textcontent = stt_txt
    analysis_list = textcontent.split()
    word_Index = 0
    for i in analysis_list:
        if i in analysis_dict:
            analysis_dict[i] = analysis_dict[i]+1
        else :
            analysis_dict[i] = 1
    answer_list = sorted(analysis_dict.items(),reverse =True, key = lambda x : x[1])
    print(answer_list)
    for word in answer_list:
        if "w" in word:
            print("Index : {}".format(answer_list.index(word)))
            word_Index = answer_list.index(word)
    #print(answer_list[1])
    #print(answer_list[0][1])
    #print(answer_list[0][0])
    path = os.getcwd()
    folder_name = "analysis_word"
    folder_path = path + '/' + folder_name + '/'
    if not os.path.isdir(folder_path):
        os.mkdir(folder_path)
    try:
        f = open(folder_path +"Analysis_word.txt",'w')
        f.write(str(analysis_dict))
        f.close()
    except:
        pass
    try:
        f = open(folder_path +"Analysis_word_sorted.txt",'w')
        f.write(str(answer_list))
        f.close()
    except:
        pass
    return answer_list
  
def send_mail(answer_list,title_list , link_list):
   smtp = smtplib.SMTP('smtp.gmail.com', 587)
   smtp.ehlo()      # say Hello
   smtp.starttls()  # TLS 사용시 필요
   smtp.login('luckysymbol13@gmail.com', 'nhnlkcfsirqdojji')
   msg = MIMEText('''    안녕하세요 김재현 연구원입니다.
   Test용 메일입니다!
   본 데모는 사내에 설치 되어있는 마이크를 통해 수집 된 데이터입니다.
   1위 : {} - {}번 말했어요!
   2위 : {} - {}번 말했어요!
   3위 : {} - {}번 말했어요!
   
   당신의 관심 상품은?!
   {}
   {}
   
   '''.format(answer_list[0][0],answer_list[0][1],answer_list[1][0],answer_list[1][1],answer_list[2][0],answer_list[2][1], title_list , link_list))
   msg['Subject'] = '[단어수집기_데모]가장 많이 당신이 쓴 말은?'
   msg['To'] = 'jh8057@kpvoice.com'
   smtp.sendmail('luckysymbol13@gmail.com', 'jh8057@kpvoice.com', msg.as_string())
   smtp.quit()
 
def startTimer(answer_list):
   print("Timer")
   timer = threading.Timer(7200, startTimer)
   count = 0
   if count == 0:
       print("pass")
   else :
       send_mail(answer_list)
   count = 1
   timer.start()
 
def load_analysis_txt():
    path = os.getcwd()
    folder_name = "Analysis_word"
    folder_path = path + '/' + folder_name + '/'
    try:
        f = open(folder_path +"Analysis_word.txt",'r')
        data = f.read()
        replace_data = data.replace("'",'"')
        analysis_dict = json.loads(replace_data)
        f.close()
    except:
        pass
    return analysis_dict

def analysis_tendency(analysis_dict,answer_list):
    if '키보드' in analysis_dict:
        if analysis_dict['키보드'] > 10:
            res = requests.get('https://search.shopping.naver.com/search/all?query=%ED%82%A4%EB%B3%B4%EB%93%9C&cat_id=&frm=NVSHATC') # url 정보를 res에 저장
            soup = BeautifulSoup(res.content,'html.parser') # html로 파싱하겠다.
            #result = soup.find_all(class_='basicList_link__1MaTN') # title을 찾아서 title1에 저장
            title_list =[]
            link_list = []
            for result in soup.find_all('a'):
                if '키보드' in str(result.get('title')):
                    title_list.append(result.get('title'))
                    link_list.append("Link : " + result.get('href'))
                elif '기계식' in str(result.get('title')):
                    title_list.append(result.get('title'))
                    link_list.append("Link : " + result.get('href'))
            send_mail(answer_list,title_list,link_list)


if __name__ == '__main__':
    analysis_dict = load_analysis_txt()
    answer_list = analysis_word("키보드 키보드 키보드 키보드 키보드")
    analysis_tendency(analysis_dict,answer_list)
    