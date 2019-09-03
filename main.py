import requests
import PyQt5

##### QWidget With GridLayout
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTextBrowser
from PyQt5.QtGui import QIcon

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
    def set_search_keyword(self):
        self.search_keyword = self.korea_addr
        print('set_search_keyword 함수 진입')
        print(self.search_keyword)

    def search_btn_clicked(self, search_keyword):
        #clear addr_result first
        self.addr_result.clear()

        print('search_btn_clicked 함수 진입')
        if(search_keyword != ''):
            try:
                URL = 'http://www.juso.go.kr/addrlink/addrLinkApi.do'
                APIKey = '자신의 API키 (도로명주소 API)'
                params = {'confmKey' : APIKey, 'currentPage' : '1', 'currentPerPage' : 10, 'keyword' : search_keyword, 'resultType' : 'json'}
                res = requests.post(URL, params=params)
                resJson = res.json()
                print(resJson)
                print(resJson['results']['juso'][0])
                response_list = resJson['results']['juso']

                self.addr_result.append('===검색결과===')
                index = 1
                for i in response_list:
                    self.addr_result.append(str(index) + ':')
                    self.addr_result.append(str(i['engAddr']))
                    self.addr_result.append('')
                    index += 1

            except:
                return self.addr_result.append('결과가 없거나 오류가 발생하였습니다.')

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)


        grid.addWidget( QLabel('한글주소: ') , 0,0)
        grid.addWidget(QLabel('API Key(선택): '), 1, 0)

        self.korea_addr = QLineEdit()
        self.korea_addr.setText('입력')

        self.api_key = QLineEdit()
        grid.addWidget(self.korea_addr, 0, 1)
        grid.addWidget(self.api_key, 1, 1)

        self.addr_result = QTextBrowser()
        grid.addWidget(self.addr_result, 2,0)

        self.search_btn = QPushButton('&Search')
        grid.addWidget(self.search_btn , 3,0)

        # search button pressed
        self.search_keyword = ''
        self.search_btn.pressed.connect(lambda:self.set_search_keyword())
        self.search_btn.pressed.connect(lambda:self.search_btn_clicked(self.search_keyword.text()))


        self.setWindowTitle('English Road Address Searching Program')
        self.setWindowIcon(QIcon('src/img/favicons.png'))

        self.setGeometry(300,300,800,600) # x,y,row size, column size
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())