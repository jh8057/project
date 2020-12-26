import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout,QPushButton,QSlider
from PyQt5.QtCore import Qt

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        lcd = QLCDNumber(self)
        self.dial = QDial(self)
        self.dial.setRange(0, 50)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(self.dial)
        self.setLayout(vbox)

        btn = QPushButton('Default', self)
        btn.move(5, 260)
        btn.clicked.connect(self.button_clicked)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)

        self.dial.valueChanged.connect(lcd.display)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())