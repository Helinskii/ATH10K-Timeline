#!/usr/bin/python
import sys
import subprocess
from PyQt4 import QtGui, QtCore


class Window(QtGui.QMainWindow):
  
  def __init__(self):
	super(Window, self).__init__()
	self.setGeometry(50,50,200,100)
	self.setWindowTitle("Router Debug")
	self.home()

  def home(self): #stuff specific to app
	btn = QtGui.QPushButton("Fetch",self)	
	btn.clicked.connect(self.display)
	btn.resize(50,20)
	btn.move(75,20)
	btn2 = QtGui.QPushButton("Quit",self)	
	btn2.clicked.connect(QtCore.QCoreApplication.instance().quit)
	btn2.resize(50,20)
	btn2.move(75,60)
	self.show()

  def display(self):
	subprocess.call(['./Router.sh'])
	

def run():
	app = QtGui.QApplication(sys.argv)
	GUI = Window()
	sys.exit(app.exec_())

run()
