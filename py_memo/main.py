import sys
import os
from PyQt5.QtWidgets import QApplication,QPushButton, QMainWindow, QAction, qApp, QWidget, QDesktopWidget, QVBoxLayout, QTextEdit, QFileDialog,QHBoxLayout,QColorDialog,QFrame
from PyQt5.QtGui import QIcon, QFont, QColor

import datetime

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.menubarUI()
        
    def initUI(self):
        self.statusBar().showMessage('Come on!') #create status bar
        self.setWindowTitle('ZZEMAL Bring ME HERE!') #set Title /QApp, Qwidget
        self.setWindowIcon(QIcon('./py_memo/rainbow.png')) #change icon /Qicon
        self.setGeometry(300, 600, 400, 200) #(move + resize) func
        self.fontSize = 10
        #self.show()

    
    def menubarUI(self):
        menubar =self.menuBar()
        menubar.setNativeMenuBar(False)
       
        #Filemenu create
        Filemenu = menubar.addMenu("파일")
        Filemenu1 = menubar.addMenu("글씨")
        Filemenu2 = menubar.addMenu("나가기")

        #Function create
        exitAction = QAction(QIcon('./py_memo/exit.png'),'GET OUT OF HERE! MOVE, MOVE!',self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit app')

        loadfile = QAction(QIcon('./py_memo/load.png'),'두두둥장~', self)
        savefile = QAction(QIcon('./py_memo/save.jpg'),'다른이름으로 저장!', self)
        savefile.setShortcut('Ctrl+Shift+S')
        savefile.setStatusTip('다른이름으로 저장하기!')
        
        fastsave = QAction(QIcon('./py_memo/capsul.jpg'),'타임캡슐에 묻기!', self)
        fastsave.setShortcut('Ctrl+S')
        fastsave.setStatusTip('기억저장하기!')

        fontup = QAction(QIcon('./py_memo/fontup.jpg'),'크게!', self)
        fontup.setShortcut('Ctrl++')
        fontup.setStatusTip('크게!')

        fontdown = QAction(QIcon('./py_memo/fontdown.jpg'),'작게!', self)
        fontdown.setShortcut('Ctrl+-')
        fontdown.setStatusTip('작게!')

        redcolor = QAction(QIcon('./py_memo/red.jpg'),'red!', self)
        redcolor.setStatusTip('너의 심장의 색깔은 BLACK..이 아닌red!')

        Blackcolor = QAction(QIcon('./py_memo/black.jpg'),'black!', self)
        Blackcolor.setStatusTip('너의 심장의 색깔은 BLACK!!!')

        selectcolor =QAction(QIcon('./py_memo/selectcolor.jpg'),'select color!', self)
        selectcolor.setStatusTip('너의 심장의 색깔은 ..!!!')

        analysis_txt =QAction(QIcon('./py_memo/word.jpg'),'Analysis Words!', self)
        analysis_txt.setStatusTip('삐립삐립.. 너의 단어는..!')
        analysis_txt.setShortcut('Ctrl+w')


        #triggered
        exitAction.triggered.connect(qApp.quit) # quit app
        loadfile.triggered.connect(self.add_open)
        savefile.triggered.connect(self.add_save)
        fastsave.triggered.connect(self.fast_save)
        fontup.triggered.connect(self.fontSizeUp)
        fontdown.triggered.connect(self.fontSizeDown)
        redcolor.triggered.connect(self.fontColorRed)
        Blackcolor.triggered.connect(self.fontColorBLACK)
        selectcolor.triggered.connect(self.selectcolor_onDialog)
        analysis_txt.triggered.connect(self.analysis_word)

        #Filemenu add
        Filemenu.addAction(loadfile)
        Filemenu.addAction(savefile)
        Filemenu.addAction(fastsave)
        Filemenu1.addAction(fontup)
        Filemenu1.addAction(fontdown)
        Filemenu1.addAction(redcolor)
        Filemenu1.addAction(Blackcolor)
        Filemenu1.addAction(selectcolor)
        Filemenu1.addAction(analysis_txt)
        Filemenu2.addAction(exitAction)
        
        #Toolbar 
        toolbar=self.addToolBar('TOOLBAR')
        toolbar.addAction(loadfile)
        toolbar.addAction(savefile)
        toolbar.addAction(fastsave)
        toolbar.addAction(fontup)
        toolbar.addAction(fontdown)
        toolbar.addAction(redcolor)
        toolbar.addAction(Blackcolor)
        toolbar.addAction(selectcolor)
        toolbar.addAction(analysis_txt)
        toolbar.addAction(exitAction)

        self.text1= QTextEdit(self) #testedit 열기
        self.text1.setAcceptRichText(True) #testedit 여는데 필요한거
        self.setCentralWidget(self.text1) #센터에 배치

        self.center()
        self.show()

    def center(self):
        qr =self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def add_open(self):
        FileOpen = QFileDialog.getOpenFileName(self, '나의 과거를 보여줘!', './')
        try : 
            f = open(FileOpen[0],'r')
            textcontenct = f.read()
            self.text1.setText(textcontenct)
            f.close()
        except:
            pass

    def add_save(self):
        FileSave = QFileDialog.getSaveFileName(self, '타임캡슐에 묻는중..', './')
 
        textcontent = self.text1.toPlainText()
        try : 
            f = open(FileSave[0], 'w')
            f.write(textcontent)
            f.close()
        except:
            pass
    def fast_save(self):
        dt = datetime.datetime.today()
        today = str(dt)
        today1 = today.replace('-','')
        today2 = today1.replace(':','-')
        
        path = os.getcwd()
        folder_name = "UZ MEMORY"
        folder_path = path + '/' + folder_name + '/'
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)

        textcontent = self.text1.toPlainText()
        try:
            f = open(folder_path +"UZ in {}.txt".format(today2[:17]),'w')
            f.write(textcontent)
            f.close()
        except:
            pass
    def fontColorRed(self) :
        colorvar = QColor(255,0,0)
        self.text1.setTextColor(colorvar)
    def fontColorBLACK(self) :
        colorvar = QColor(0,0,0)
        self.text1.setTextColor(colorvar)
    def fontSizeUp(self) :
        self.fontSize = self.fontSize + 1
        self.text1.setFontPointSize(self.fontSize)
    def fontSizeDown(self) :
        self.fontSize = self.fontSize - 1
        self.text1.setFontPointSize(self.fontSize)
    def selectcolor_onDialog(self):
        col = QColorDialog.getColor()
        if col.isValid():
            colorvar = QColor(col.red(),col.green(),col.blue())
            self.text1.setTextColor(colorvar)
    def analysis_word(self):
        textcontent = self.text1.toPlainText()
        analysis_list = textcontent.split()
        analysis_dict = {}
        for i in analysis_list:
            if i in analysis_dict:
                analysis_dict[i] = analysis_dict[i]+1
            else :
                analysis_dict[i] = 1
        dt = datetime.datetime.today()
        today = str(dt)
        today1 = today.replace('-','')
        today2 = today1.replace(':','-')
        
        path = os.getcwd()
        folder_name = "UZ Analysis"
        folder_path = path + '/' + folder_name + '/'
        if not os.path.isdir(folder_path):
            os.mkdir(folder_path)
        try:
            f = open(folder_path +"Analysis UZ in {}.txt".format(today2[:17]),'w')
            f.write(str(analysis_dict))
            f.close()
        except:
            pass
    

if __name__=='__main__':
    app=QApplication(sys.argv)
    ex=MyApp()
    sys.exit(app.exec_())