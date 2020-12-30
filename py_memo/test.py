import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp, QFileDialog, QTextEdit,QHBoxLayout ,QVBoxLayout
 
 
 
class QtGUI(QMainWindow):
 
    def __init__(self):
 
        super().__init__()
        self.resize(400, 400)
        self.setWindowTitle("UZ's Diary!")
        menubar = self.menuBar()
 
        Filemenu = menubar.addMenu("파일")
        Filemenu1 = menubar.addMenu("편집")
        Filemenu2 = menubar.addMenu("서식")
 
        loadfile = QAction('laod File ...', self)
        savefile = QAction('save File ...', self)
        exit = QAction('Exit',self)
 
        loadfile.triggered.connect(self.add_open)
        savefile.triggered.connect(self.add_save)
        exit.triggered.connect(qApp.quit)
 
        Filemenu.addAction(loadfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(exit)
 
        self.text1= QTextEdit(self) #testedit 열기
        self.text1.setAcceptRichText(True) #testedit 여는데 필요한거
        self.setCentralWidget(self.text1) #센터에 배치
 
        self.show()
 
 
    def add_open(self):
 
        FileOpen = QFileDialog.getOpenFileName(self, 'Open file', './')
 
        f = open(FileOpen[0],'r')
        textcontenct = f.read()
        self.text1.setText(textcontenct)
        f.close()
 
 
    def add_save(self):
 
        FileSave = QFileDialog.getSaveFileName(self, 'Save file', './')
 
        textcontent = self.text1.toPlainText()
 
        f = open(FileSave[0], 'w')
 
        f.write(textcontent)
 
        f.close()
 
 
 
if __name__ == '__main__':
 
    app = QApplication(sys.argv)
 
    ex = QtGUI()
 
    app.exec_()