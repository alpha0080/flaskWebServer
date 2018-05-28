import os
import json
import sys

sys.path.append("C:/Python27/Lib")
sys.path.append("C:/Python27/Lib/site-packages")

from flask import Flask, render_template, request

app = Flask(__name__)

#from flask_dropzone import Dropzone


class flaskApp():
    def __init__(self):
       # self.app = Flask(__name__)
       self.doc ="flask Test"


#@app.route('/flaskMaya',methods=['POST','GET'])
@app.route('/flaskMaya/')
def flaskMaya():
   # return "my flask test"
    return render_template('flaskMayaH5.html')

@app.route('/flaskRunA/')
def flaskRunA():
    print "flaskRunA"



def main():
    #app = flaskApp
    #app = Flask(__name__)
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
