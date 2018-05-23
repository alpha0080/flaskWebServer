
from PySide2 import QtCore, QtGui, QtWidgets

import buildUI
reload(buildUI)

import random 
import postgreSQLCall

    #getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  
    #getTacticDB = postgreSQLCall.callPostgre('simpleslot','postgres','','192.168.163.60','5432')  
getSthpwDB = postgreSQLCall.callPostgre('sthpw','postgres','','192.168.163.60','5432')   
  #  projectRows = self.getTacticDB.getRowDataFromTable('game')
   # assetRows = getTacticDB.getRowDataFromTable('assets')
userProcessData =  getSthpwDB.getRowDataFromTable('login')

userCount = len(userProcessData)
for i in range(0,userCount):
    print userProcessData[i][1]
    print userProcessData[i][7]

   # print userProcessData[i][19]

#print userProcessData[0]