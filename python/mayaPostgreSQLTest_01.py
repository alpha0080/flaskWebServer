
from PySide2 import QtCore, QtGui, QtWidgets

import buildUI
reload(buildUI)

import random 
import postgreSQLCall

#getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  
getTacticDB = postgreSQLCall.callPostgre('simpleslot','postgres','','192.168.163.60','5432')  
getSthpwDB = postgreSQLCall.callPostgre('sthpw','postgres','','192.168.163.60','5432')   
  #  projectRows = self.getTacticDB.getRowDataFromTable('game')
assetRows = getTacticDB.getRowDataFromTable('assets')
shotRows = getTacticDB.getRowDataFromTable('shot')

userProcessData =  getSthpwDB.getRowDataFromTable('login')
taskData =  getSthpwDB.getRowDataFromTable('task')

userCount = len(userProcessData)
for i in range(0,userCount):
    print userProcessData[i][1]
    print userProcessData[i][7]
    
taskData[-1][32]

shotCount =  len(shotRows)

for i in range(0,shotCount):
    if shotRows[i][10] == "GAME00803":  #define the qc project, that name is qc_db,game code is "GAME00803"
        print shotRows[i]

   # print userProcessData[i][19]

#print userProcessData[0]