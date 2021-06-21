import pyupbit
import requests
access = ""          # 본인 값으로 변경
secret = ""          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)


print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회


def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0

def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

krw = get_balance("KRW")
if 5000<krw<50000:
    print("YR")
elif 50000<krw <110000:
    print("NO")
btc = get_balance("GAS")
print(btc)

myToken = "" # slack token

#post_message(myToken,"#message", "Today KRW : " +str(krw))

