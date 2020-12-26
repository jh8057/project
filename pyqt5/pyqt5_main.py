import sys
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow, QAction, qApp, QWidget, QDesktopWidget, QVBoxLayout
from PyQt5.QtGui import QIcon, QFont

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.exitUI()
        
    def initUI(self):
        self.statusBar().showMessage('Come on!') #create status bar
        self.setWindowTitle('ZZEMAL Bring ME HERE!') #set Title /QApp, Qwidget
        self.setWindowIcon(QIcon('rainbow.png')) #change icon /Qicon
        self.setGeometry(300, 600, 400, 200) #(move + resize) func
        #self.show()

    
    def exitUI(self):
        exitAction = QAction(QIcon('exit.png'),'GET OUT OF HERE! MOVEMOVE!',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')
        exitAction.triggered.connect(qApp.quit) # quit app

        self.statusBar()

        menubar =self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        #&File'의 앰퍼샌드 (ampersand, &)는 간편하게 단축키를 설정하도록 해줍니다.
        #'F' 앞에 앰퍼샌드가 있으므로 'Alt+F'가 File 메뉴의 단축키가 됩니다. 만약 'i'의 앞에 앰퍼샌드를 넣으면 'Alt+I'가 단축키가 됩니다.
        filemenu.addAction(exitAction)
        
        toolbar=self.addToolBar('exit')
        toolbar.addAction(exitAction)

        self.center()
        self.show()

    def center(self):
        qr =self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())