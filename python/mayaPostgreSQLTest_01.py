
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
fileData = getSthpwDB.getRowDataFromTable('file')

projectRows =getTacticDB.getRowDataFromTable('game')
projectRows = list(reversed(projectRows))
projectRows[0][8] #gameName
projectRows[0][10] #gameName

filesCount = len(fileData)
userCount = len(userProcessData)
for i in range(0,userCount):
    print userProcessData[i][1]
    print userProcessData[i][7]
    
taskData[-1][32]

shotCount =  len(shotRows)
fileData[-1][20]
for i in range(0,shotCount):
    if shotRows[i][10] == "GAME00803":  #define the qc project, that name is qc_db,game code is "GAME00803"
        print shotRows[i]

for i in range(0,filesCount):
    if fileData[i][20] == "GAME00803":
        print fileData[i]
        
        
    
    