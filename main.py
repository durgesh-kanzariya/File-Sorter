import sys
from interface import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WidgetAttribute.WA_TranslucentBackground)

        self.setWindowIcon(QtGui.QIcon(u":/icons/icons/twitter.svg"))
        self.setWindowTitle("File Organizer  by-Durgesh Kanzariya")

        QtWidgets.QSizeGrip(self.ui.label_5)

        self.ui.pushButton_2.clicked.connect(lambda: self.showMinimized())
        self.ui.pushButton.clicked.connect(lambda: self.close())
        self.ui.pushButton_5.clicked.connect(lambda: self.close())

        self.ui.pushButton_3.clicked.connect(lambda: self.restore_or_maximize_window())

        self.draggable = False
        self.oldPos = None
        self.ui.frame_3.mousePressEvent = self.mousePressEvent_frame_3
        self.ui.frame_3.mouseMoveEvent = self.mouseMoveEvent_frame_3
        self.ui.frame_3.mouseReleaseEvent = self.mouseReleaseEvent_frame_3

        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slide())

        self.show()

    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.pushButton_3.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            self.ui.pushButton_3.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

    def mousePressEvent_frame_3(self, event):
        if event.buttons() == Qt.LeftButton:
            self.draggable = True
            self.oldPos = event.globalPos()

    def mouseMoveEvent_frame_3(self, event):
        if self.draggable and event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseReleaseEvent_frame_3(self, event):
        if event.button() == Qt.LeftButton:
            self.draggable = False

    def slide(self):
        width = self.ui.slide_menu_container.width()
        if width == 0:
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-right.svg"))
        else:
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/help-circle.svg"))
        self.animation = QtCore.QPropertyAnimation(self.ui.slide_menu_container, b"maximumWidth")
        self.animation.setDuration(400)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
