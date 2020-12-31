# JH_project
김재현의 프로젝트들을 모아둔 Git 저장소이다.

<img src="./pyqt5/rainbowface.jpg" width="128px" height="128px" title="HI!" alt="rainbowface"></img><br/>

## kakao_msg
나에게 카카오 메시지를 보내는 프로젝트이다.  
카카오 메세지 API를 이용했다.
**webcrawling**을 이용해서 그날의 **미세먼지**,**코로나 확진자수**를 찾아 `리스트` 형태에 담아 메시지를 보냈다.
### 방법
* 카카오메시지 Rest API url을 통해 response를 받는다.
* webcrawling으로 naver검색 엔진에서 미세먼지 및 확진자 정보를 가져온다.
* 헤더, 설명, 버튼, 이미지, 링크등 채워넣는다.  
### 결과 
<img src ="./kakao_msg/kakao_msg_fi.JPG" title="result"></img>
___

## py_memo
`시작동기` : 여자친구가 가볍게 웃으면서 쓰는 일기장을 하나 만들어 보고 싶었다.
### 시나리오
1. exe파일을 실행하면 메모장이 뜬다.
2. 오늘의 하루 일기를 간단히 쓴다.
3. 마지막에 오늘의 색을 정하는 버튼이 있다.
4. 색에 따라 메시지 창이 다르게 반응!
5. 저장은 특정 경로에 저장 되게 한다.
저장 이름은 카운트에 따라 다르게 되게끔 한다.
(날짜를 받아와서 날짜로 저장되게 하자)
6. 룰렛 기능이나 랜덤을 통해 특정 주제(웃긴거 or 흥미유발)을 정하고 webcrawling을 통해 사진을 가져와서 띄운다.

### 동작 기능
1번 시나리오 : **pyqt5** 와 **pyinstaller** 를 이용하였다.  
>참고: pyinstaller 는 cross-compile이 안되기에, window에서 컴파일하면 window에서만 실행이가능하다.  

2번 시나리오 : pyqt5의 **QTextEdit** 기능을 이용하였다.  
5번 시나리오 : datetime 모듈을 통해 실시간 시간 정보를 가져오고, 이를 문자로 저장하였다.
이를 이용하여 저장 파일의 이름을 결정하였다.
```py
import datetime
        dt = datetime.datetime.today()
        today = str(dt)
        today1 = today.replace('-','')
        today2 = today1.replace(':','-')
        ...
        f = open("UZ in {}.txt".format(today2[:17]),'w')
```
### 결과 
Version1.0 : 시나리오의 1,2,5번 구현 완료. 색에 관한 이벤트를 추가해야된다.  
<img src ="./py_memo/result_v1.jpg" title="result_v1"></img>  *version1.0 결과 사진*

#### 아쉬웠던점
>21.01.01 기록 : version 1.0
 - pyinstaller가 cross-compile이 되지 않는점.
 - 코드 반복이 많았던 점
 - 다른 이름 저장을 할때 직접 .txt를 작성해줘야된다.
 - 이모티콘 작성이 불가능한 점

___

## pyqt5
qt란 C++ 코드를 GUI로 구현하는 프로그램이다.
pyqt로 확장되어 python을 GUI로 구현할 수 있게 되었다.

기본적인 **widget** 생성하여 **menu,button**등을 구성해보았고,**mouse** 및 **keyboard** 이벤트 발생을 이용해보았다.  
마무리로 pyinstaller 을 통해 exe파일로 만드는것 까지 해보았다.
```
pyinstaller -w -F "python파일"
```
### 결과
아이콘 변경, 타이틀 설정, 단축기 설정, 메뉴바 & 창태바 추가, 상태메시지, 중심 위치 설정  
<img src ="./pyqt5/pyqt5_main.JPG" title="result1" height="180px"></img>  
슬라이더 및 다이얼 설정, 둘의 연동, lcd에 숫자 표시, 리셋(default) 버튼  
<img src ="./pyqt5/lcd.JPG" title="result2" width="200px" height="200px"></img>  
___  

## startgit
이 폴더는 제일 처음 깃을 사용했을때 만들었던 폴더이다.  
~~그래서 나도 뭐가 들어있는지 모르겠다 ㅋㅋ~~

## study_c
C언어 공부를 위한 폴더이다. 
.vscode폴더 내에 vscode에서 c언어를 컴파일하고 디버깅하기 위한 세팅이 들어있다.
[dojang(도장)](https://dojang.io)을 보고 공부했다.
|Day|Work|
|:--:|:--|
|20.12.27| unit1 ~ unit4 : Setting IDE & Print|
|20.12.28| unit5 ~ unit6 : variable & Debug|
|20.12.29| unit7 : type of int|
## study_py
파이썬 공부를 위한 폴더이다. 파이썬 관련 파일들이 모여있다.

## SWTEST
SW test 기출문제들이다. 
## vscode_cmake
기본적인 cmake형식이다.

## webcrawling
web크롤링 파일이다. 
naver에서 타이틀을 가져오는것을 해보았다.

## webpage
css와 html을 이용한 webpage 구성이다.