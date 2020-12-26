import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "693d1d5348bc088eec764d64b145eef0",
    "redirect_uri" : "https://localhost.com",
    "code"         : "7YXwfMkAbXWnHZd_48TpiKo7l9YLzhLKpN8KFuTvX0ja4oSAJyfL3K7qNLGYi-0-tYbBHQopyV8AAAF2W1tLlA"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)
