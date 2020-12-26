import requests

# 커스텀 템플릿 주소 : https://kapi.kakao.com/v2/api/talk/memo/send
talk_url = "https://kapi.kakao.com/v2/api/talk/memo/send"

# 사용자 토큰
token = '693d1d5348bc088eec764d64b145eef0'
header = {
    "Authorization": "Bearer NI51qRXOEFNXOiQ_eSqg6uA0_CyDrGWhO-rjBQorDNIAAAF2XLRVOg".format(
        token=token
    )
}

# 메시지 template id와 정의했던 ${name}을 JSON 형식으로 값으로 입력
payload = {
    'template_id' : {42494},
    'template_args' : '{"topic1": "미세먼지는?"}'
}

# 카카오톡 메시지 전송
res = requests.post(talk_url, data=payload, headers=header)

if res.json().get('result_code') == 0:
    print('메시지를 성공적으로 보냈습니다.')
else:
    print('메시지를 성공적으로 보내지 못했습니다. 오류메시지 : ' + str(res.json()))