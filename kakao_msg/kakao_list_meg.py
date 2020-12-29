import json
import requests
from bs4 import BeautifulSoup

#topic1 : 미세먼지
res = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&query=%EC%A0%84%EA%B5%AD%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80') 
soup = BeautifulSoup(res.content,'html.parser')

title1 = soup.find(class_='tb_scroll') # title을 찾아서 title1에 저장
title1_str = title1.get_text()

list1 = title1_str.split()
index1 = list1.index("서울")


#topic2 : 코로나
res2 =  requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9D%BC%EC%9D%BC%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&tqi=U9h25sp0JXossFNwbFossssstZG-213683')
soup2 = BeautifulSoup(res2.content,'html.parser')

title2 = soup2.find(class_='status_today')
title2_str = title2.get_text()

list2 = title2_str.split()


url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "EfDpZqJHpRwj2Zw-zbcJI23qwpeS8-lhPz0nSAorDKcAAAF2r2SMVQ"
}

template = {
    "object_type" : "list",
    "header_title" : "째말의 아침 뉴~으스!",
    "header_link" : {
        "web_url" : "www.naver.com",
        "mobile_web_url" : "www.naver.com"
    },
    "contents" : [
        {
            "title" : "미세먼지는?!",
            "description" : "{}의 미세먼지는 {}으로 {}!".format(list1[index1],list1[index1+1],list1[index1+2]),
            "image_url" : "http://ojsfile.ohmynews.com/STD_IMG_FILE/2017/0103/IE002079730_STD.jpg",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=rlawogus&tqi=U9hoZsprvTossa6pMcRssssstvd-482393",
                "mobile_web_url" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=rlawogus&tqi=U9hoZsprvTossa6pMcRssssstvd-482393"
            }
        },
        {
            "title" : "코로나 일일 확진자는?",
            "description" : "국내발생 {}명, 해외유입{}명!".format(list2[2],list2[4]),
            "image_url" : "https://postfiles.pstatic.net/MjAyMDA0MjhfMjkz/MDAxNTg4MDgyMjE4MjUy.5SYQs_iJSwIs-kw0eyW0nB58ndN2Fw0OSi9TwYdLJO8g.OsFlm1eLHc2fKjJQxe8F6_ttBEDdB8GrHXeeDnGQDYUg.JPEG.geauil/%EC%97%B0%ED%95%84%EC%98%A4%EB%A6%84_%EB%A7%88%EC%8A%A4%ED%81%AC_%EC%95%88%EB%82%B4%EB%AC%B8_%EB%8C%80%EC%A7%80_1.jpg?type=w773",
            "image_width" : 50, "image_height" : 50,
            "link" : {
                "web_url" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9D%BC%EC%9D%BC%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&tqi=U9h25sp0JXossFNwbFossssstZG-213683",
                "mobile_web_url" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%BD%94%EB%A1%9C%EB%82%98+%EC%9D%BC%EC%9D%BC%ED%99%95%EC%A7%84%EC%9E%90&oquery=%EC%BD%94%EB%A1%9C%EB%82%98+%ED%99%95%EC%A7%84%EC%9E%90&tqi=U9h25sp0JXossFNwbFossssstZG-213683"
            }
        }
        
    ],
    "buttons" : [
        {
            "title" : "네이버로 GO!",
            "link" : {
                "web_url" : "www.naver.com",
                "mobile_web_url" : "www.naver.com"
            }
        }
    ]
    
}

data = {
    "template_object" : json.dumps(template)
}

response = requests.post(url, data=data, headers=headers)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))