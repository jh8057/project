import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.btnUI()
    
    def initUI(self):
        self.setWindowTitle('ZZEMAL Bring ME HERE!') #set Title /QApp, Qwidget
        self.setWindowIcon(QIcon('c:/Users/JAEHYUN/Desktop/JH_Git/pyqt5/uzfun.png')) #change icon /Qicon
        #self.move(300,300)
        #self.resize(400,200) 
        self.setGeometry(300, 300, 400, 200) #(move + resize) func
        
        #self.show()

    def btnUI(self):
        btn = QPushButton('Quit',self) #create putton /QPushButton
        btn.move(125,50)
        btn.resize(btn.sizeHint())
        #btn.resize(100,100) #possible
        #btn.setGeometry(120, 50, 100, 100) #possible
        btn.clicked.connect(QCoreApplication.instance().quit)

        QToolTip.setFont(QFont('SansSerif', 10)) #set font /Qfont 
        self.setToolTip('This is a <b>QWidget</b> widget') #create tooltip /QToolTip 
        btn.setToolTip('This is a <b>QPushButton</b> widget')

        self.show()


if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())