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

##########################
####### PyQT5 Part #######
##########################


###########
#TODO LIST#
###########
# TODO PYQT5로 GUI 만들기.
# TODO 필수 변수 : 도로명 키워드.
# TODO GUI Main 요소 : 도로명 키워드 input, Search Button, API KEY(옵션), Result.
# TODO GUI UpSide 요소 : Menu ( Quit, Setting ), etc ( Help, Credit )
# TODO GUI DownSide 요소 : Status Bar ( Ready, Searching..., Ready, Error(404, 500), etc.. )

# TODO 도로명 키워드를 받아서 SearchEngAdd()로 보내고 얻은 영문 주소를 TextBrowser로 보내기
# TODO Search Button을 누르면 먼저 TB 안의 내용을 Clear 시키고 Search 하게 만들기.
# TODO StatusBar로 성공/실패 알려주기
# TODO API KEY == ''면 자체 API KEY로 돌리기. API KEY != ''면 가지고 있는 API 키로 돌리기.

# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QToolTip, QMainWindow, qApp, QAction # Button, etc.
# from PyQt5.QtGui import QIcon, QFont #for insert favicon
# from PyQt5.QtCore import QCoreApplication
# class MyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()
#
#     def initUI(self):
#
#         ###QToolTip Section
#         QToolTip.setFont(QFont('SansSerif', 10)) # ToolTip (when mouse is hovering at a button)
#         self.setToolTip('This is a <b>QWidget</b> widget')
#
#         ###set exitAction at Menu
#         exitAction = QAction(QIcon('src/img/exit.png'), 'Exit', self)
#         # QAction(QIcon('Directory'), Displayed Words, inherited widget)
#         exitAction.setShortcut('Ctrl+Q') # object.setShortcut('Shortcut')
#         exitAction.setStatusTip('Exit application') #object.setStatusTip('send this to status bar')
#         exitAction.triggered.connect(qApp.quit) #quit app when exitAction is triggered
#
#         ###menuBar Section
#         menubar = self.menuBar() #Initialize menubar
#         menubar.setNativeMenuBar(False) # ?
#         fileMenu = menubar.addMenu('&File') #Make open File menu when (Alt+'F')ile
#         fileMenu.addAction(exitAction)
#
#         ###statusBar Section
#         self.statusBar().showMessage('Ready')
#         self.setGeometry(300,300,200,200)
#
#         ###QPushButton Section
#         btn = QPushButton('Quit', self) # QPushButton('Button's text', parent widget)
#         btn.setToolTip('This is a <b>QPushButton</b> widget')
#         btn.move(50,50)  # move Button
#         btn.resize(btn.sizeHint())  # ?
#         btn.clicked.connect(QCoreApplication.instance().quit)
#         # When button is clicked, "clicked" Signal is created. Clicked Signal is going to Applicaion's quit() method.
#
#         ###QTitle, Icon, move, resize, show Section
#         self.setWindowTitle('English Address Search Program')
#         self.setWindowIcon(QIcon('src/img/favicons.png'))
#         self.move(300,300)
#         self.resize(400,400)
#         self.show()
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = MyApp()
#     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, QToolTip, QMainWindow, qApp, QAction # Button, etc.
# from PyQt5.QtGui import QIcon, QFont #for insert favicon
# from PyQt5.QtCore import QCoreApplication
# class MyApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.initUI()