import requests
import PyQt5

#Todo
#ui 만들기

# URL = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
# params = {'confmKey' : '발급받은 API키', 'currentPage' : '1', 'currentPerPage' : 10, 'keyword' : '갈매중앙로', 'resultType' : 'json'}
# res = requests.post(URL, params=params)
# resJson = res.json()
# print(resJson)
# print(resJson['results']['juso'][0])
# response_list = resJson['results']['juso']
#
# count = 1
# for i in response_list:
#     print("목록 {0}".format(count))
#
#     if(i['bdNm'] != ""):
#         print("아파트 주소 이름 : {0}".format(i['bdNm']))
#     else:
#         print("아파트 주소 이름 : None")
#
#     if(i['detBdNmList'] == ""):
#         print("동 정보 없음")
#     else:
#         print(i['detBdNmList'])
#     print("영어 주소 : {0}".format(i['engAddr']))
#     print("")
#     count += 1

# print(resJson['results']['juso'][0]['engAddr'])

"""
기본 GUI 화면
"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication


class ExWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Main Window')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ExWindow()
    sys.exit(app.exec_())