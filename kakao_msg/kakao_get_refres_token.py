import json
import requests



url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "refresh_token",
    "client_id"  : "693d1d5348bc088eec764d64b145eef0",
    "refresh_token" : "nnlK_2qlHrrMT1VZX3h05fm3YF6XXpG3OX-3Xgo9dJgAAAF2W1vHnQ"
}
response = requests.post(url, data=data)

print(response.json())

'''
POST /oauth/token HTTP/1.1
Host: kauth.kakao.com
Content-type: application/x-www-form-urlencoded;charset=utf-8

Parameter
Name	      Type	    Description	Required
grant_type	  String	refresh_token으로 고정	O
client_id	  String	앱 생성 시 발급 받은 REST API	O
refresh_token String	토큰 발급 시 응답으로 받은 refresh_token Access Token을 갱신하기 위해 사용	O
'''