import json
import requests

url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"


#app_key= 693d1d5348bc088eec764d64b145eef0
#local_code = 9ltvFKZTTE7lwZR1LW6x_yGqm8-j6VsJ61iymNCPE0565YGkkHZuVWPkcQhIRkT_mPLKJgopyV8AAAF2W1CQJg
#access_token ="lQa-h8nnRHmlFlSS_-pSWjU7dYm2JU2-wuDg2go9dJgAAAF2W1vHnw"

# 사용자 토큰
headers = {
    "Authorization": "Bearer " + "NI51qRXOEFNXOiQ_eSqg6uA0_CyDrGWhO-rjBQorDNIAAAF2XLRVOg"
}


data = {
    "template_object" : json.dumps({ "object_type" : "text",
                                     "text" : "Hello, Daum!",
                                     "link" : {
                                                 "web_url" : "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%AF%B8%EC%84%B8%EB%A8%BC%EC%A7%80&oquery=rlawogus&tqi=U9hoZsprvTossa6pMcRssssstvd-482393"
                                              }
    })
}

response = requests.post(url, headers=headers, data=data)
print(response.status_code)
if response.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(response.json()))
  