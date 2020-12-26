import requests
from bs4 import BeautifulSoup

print("Let's start webcrawling!")

res = requests.get('https://www.naver.com/') # url 정보를 res에 저장
#print(res.content) # content로 res 내에 내용을 볼 수 있음
soup = BeautifulSoup(res.content,'html.parser') # html로 파싱하겠다.
# 파싱이란 , 어떤 페이지에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출해 가공하는 것을 말한다.
title1 = soup.find('title') # title을 찾아서 title1에 저장
print(title1.get_text()) 