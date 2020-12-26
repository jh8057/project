import json
import requests
from bs4 import BeautifulSoup


res = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80') 
soup = BeautifulSoup(res.content,'html.parser')

title1 = soup.find(class_='tb_scroll') # title을 찾아서 title1에 저장
title1_str = title1.get_text()

list1 = title1_str.split()
index1 = list1.index("서울")

print(list1[index1])
print("현재 :",list1[index1+1])
print("오전예보 :",list1[index1+2])
print("오후예보 :",list1[index1+3])


res2 =  requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9D%BC%EC%9D%BC%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&tqi=U9h25sp0JXossFNwbFossssstZG-213683')
soup2 = BeautifulSoup(res2.content,'html.parser')

title2 = soup2.find(class_='status_today')
title2_str = title2.get_text()

list2 = title2_str.split()

print("국내발생 {}명, 해외유입{}명!".format(list2[2],list2[4]))

