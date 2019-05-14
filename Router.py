#!/usr/bin/python
import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
  
  def __init__(self):
	super(Window, self).__init__()
	self.setGeometry(50,50,1200,600)
	self.setWindowTitle("Router Debug")
	self.home()

  def home(self): #stuff specific to app
	self.textbox()
	btn = QtGui.QPushButton("Fetch",self)	
	btn.clicked.connect(self.readfile)
	btn.resize(75,25)
	btn.move(1000,100)
	btn2 = QtGui.QPushButton("Quit",self)	
	btn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
	btn2.resize(75,25)
	btn2.move(1000,300)
	self.show()

  def textbox(self):
	self.text = QtGui.QTextEdit(self)
	self.text.move(20, 20)
	self.text.resize(900,500)
	

  def readfile(self):
	f = open('data.txt','r')
	self.text.setText("Hi")
	with f:
	  lines = f.read()
	  self.text.setText(lines)
	f.close()	
	

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
