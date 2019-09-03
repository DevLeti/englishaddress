English Road Address Searching Program (working title) (영문 도로명 주소 검색 프로그램)
=============

# 1. 설명
English Road Address by using OpenApi (<http://juso.go.kr/>)  
영문 도로명 주소 검색 프로그램입니다. 원하는 키워드를 통해 자신의 주소가 영어로 어떻게 되어있는지 확인할 수 있습니다.

# 2. 요구되는 프로그램 및 모듈
1. Python(Language, 3.7.x) - I made this with Python 3.7.3. That's the reason.
2. PyQt5(Module) - For GUI.
3. requests(Module) - For Requesting English Address to <http://juso.go.kr/>
4. will be added when other dependancies are required.

# 3. 사용법
현재 APIKey(선택)폼은 작동하지 않습니다.  
main.py파일의 search_btn_clicked함수에 APIKey 변수의 값에 직접 API값을 넣으셔야 합니다. 추후 필수값으로 지정할 계획입니다.  
APIKEY(선택)form is not working now.d
you should set your APIKey value to variable - 'APIKey' - in search_btn_clicked function (main.py file). I will make APIKey form value required value.
