import os
import json
import sys

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

app = Flask(__name__)



class flaskApp():
    def __init__(self):



def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()

    ##app.run(host='192.168.161.46',debug=True)



'''


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")



class mod_MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent= QtWidgets.QApplication.activeWindow()):
        super(mod_MainWindow, self).__init__(parent)
        #self.QTITEM.ACTION.connect(self.MODDEF)
        self.setupUi(self)


def main():
    global ui
    app = QtWidgets.QApplication.instance()
    if app == None: app = QtWidgets.QApplication(sys.argv)
    try:
        ui.close()
        ui.deleteLater()
    except: pass
    ui = mod_MainWindow()
    ui.show()

if __name__ == '__main__':
    main()


'''
