from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from cv2 import rotate

class Clock(QMainWindow):

    def __init__(self):
        
        super().__init__()
        #create timer obj
        timer= QTimer(self)
        #update the whole code
        timer.timeout.connect(self.update)
        #setting 1000ms timer
        timer.start(1000)
        #window title
        self.setWindowTitle('Clock')
        self.setGeometry(200,200,300,300)
        self.setStyleSheet("background : black;")
        #creating hands
        self.hPointer = QtGui.QPolygon([QPoint(6,7),
                                        QPoint(-6,7),
                                        QPoint(0,-50),])
        self.mPointer = QtGui.QPolygon([QPoint(6,7),
                                        QPoint(-6,7),
                                        QPoint(0,-70),])
        self.sPointer = QtGui.QPolygon([QPoint(1,1),
                                        QPoint(-1,1),
                                        QPoint(0,-90),])
        #the color of minute and hour hands
        self.bColor = Qt.green
        #the color of second hand
        self.sColor =Qt.red

    def paintEvent(self,event):
        #getting minimum of width and height
        #so that clock remain square
        rec = min(self.width(),self.height())
        #getting current time
        tik=QTime.currentTime()
        #creating a painter obj
        painter = QPainter(self)
        #method to draw the hands
        def drawPointer(color,rotation,pointer):
            painter.setBrush(QBrush(color))
            painter.save()
            painter.rotate(rotation)
            painter.drawConvexPolygon(pointer)
            painter.restore()
        
        painter.setRenderHint(QPainter.Antialiasing)
        painter.translate(self.width() / 2,self.height() / 2)
        painter.scale(rec / 200,rec / 200)
        #set current pen as no pen
        painter.setPen(QtCore.Qt.NoPen)
        #draw each hand
        drawPointer(self.bColor, (30 * (tik.hour() + tik.minute() / 60)), self.hPointer)
        drawPointer(self.bColor, (6 * (tik.minute() + tik.second() / 60)), self.mPointer)
        drawPointer(self.sColor, (6 * tik.second()),self.sPointer)
        #drawing background
        painter.setPen(QPen(self.bColor))

        for i in range(0,60):
            #drawing background lines
            if (i % 5) == 0:
                painter.drawLine(87,0,97,0)

            painter.rotate(6)
        #ending the painter
        painter.end()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Clock()
    win.show()
    exit(app.exec_())