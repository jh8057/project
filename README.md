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
___

## study_c
C언어 공부를 위한 폴더이다. 
참고 .vscode폴더 내에 vscode에서 c언어를 컴파일하고 디버깅하기 위한 세팅이 들어있다.
[dojang(도장)](https://dojang.io)을 보고 공부했다.
|Day|Work|
|:--:|:--|
|20.12.27| unit1 ~ unit4 : Setting IDE & Print|
|20.12.28| unit5 ~ unit6 : variable & Debug|
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