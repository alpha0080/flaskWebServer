#coding=utf-8

import sys

# add alpha python env path
sys.path.append('//mcd-one/database/assets/scripts/python_alpheEnv/Lib')
sys.path.append('//mcd-one/database/assets/scripts/python_alpheEnv/Lib/site-packages')

# call postgreSQL python module
import psycopg2

class callPostgre:

    def __init__(self,dbName,userID,userPW,hostIP,hostPort):

       # print 'int 01'
        #print dbName,userID,userPW,hostIP,hostPort

        self.conn = psycopg2.connect(database=dbName, user= userID, password= userPW, host= hostIP, port= hostPort)
        self.cursor = self.conn.cursor()
        #return self.cursor
    def close(self):
        print 'cursor close'
        self.conn.close()
        self.cursor.close()



    def getSelectTableQuery(self,tableName):  # select table, set query

        #print "SELECT * FROM %s"%tableName
        query = self.cursor.execute("SELECT * FROM %s"%tableName)

        #return query
        return self.cursor.description


    def createTabeIntoDatabase(self,tableName,columnList):
        '''create table, from input, and create column,
            arg* database, assign the database name without already existed
            arg* columnList , assign all column data form postgreSQL description
        '''



        command = 'CREATE TABLE %s ('%tableName + columnList +')'
        print command
        self.cursor.execute(command)

        self.conn.commit()



    def deleteSelectTable(self,tableName):
        #print ' delete %s'%tableName
        command = 'DROP TABLE %s '%tableName
        print command




        #self.cursor.execute("DROP TABLE %s"%tableName)
        self.cursor.execute(command)

        self.conn.commit()

        #self.conn.close()
        #self.cursor.close()

    def deleteAllDataInTable(self,tableName):
        command = 'DELETE FROM %s'%tableName
        self.cursor.execute(command)
        #self.cursor.execute("DELETE from usersDB")
        self.conn.commit()



    def getRowDataFromTable(self,tableName):
        self.cursor.execute("SELECT * FROM %s"%tableName)
        rows = self.cursor.fetchall()
        totalColumnCount = len(rows)

        return rows


    def getRowSelectDataFromTable(self,tableName,searchKeyWord):
        command = "SELECT %s FROM %s"%(searchKeyWord,tableName)
        print command
        self.cursor.execute(command)
        return self.cursor.fetchall() # return data from selected name
        #print self.cursor.execute("SELECT %s FROM %s"%(searchKeyWord,tableName))
        #for row in rows:
        #    print('name=' + str(row[0]) + ' address=' + str(row[1]) +
        #' age=' + str(row[2]) + ' date=' + str(row[3]))

    def getRowSelectDataFromTableDetial(self,tableName,columnName,searchColumn,searchKey):
        #command = "SELECT %s FROM %s WHERE %s = %s"%(columnName,tableName,searchColumn,searchKey)
        command = "SELECT %s FROM %s WHERE %s = %s"%(columnName,tableName,searchColumn,searchKey)

        #print command
        self.cursor.execute(command)
        return self.cursor.fetchall()

    def addColumnToTable(self,tableName,columnName,dataType,isNotNull): #add column to select table
        '''addColumnToTable(tableName,columnName,dataType,isNotNull) ,
            dataType: integer,
                     varchar(n) :variable-length with limit
                     char(n) :fixed-length, blank padded
                     text:variable unlimited length
                     data :date (no time of day)
                    time [ (p)] :[ without time zone ]
                    boolean:state of true or false
                    path:Closed path :(similar to polygon),[(x1,y1),...]
                                                        ,((x1,y1),...)
                    polygon:Polygon (similar to closed path),((x1,y1),...)
                    circle:Circle ,<(x,y),r> (center yiibai and radius)
                    json:array_to_json('{{1,5},{99,100}}'::int[]) -->[[1,5],[99,100]]
                        row_to_json(row(1,'foo')) -->{"f1":1,"f2":"foo"}
                    xml
                    UUID
                    macaddr:	MAC addresses
                    inet :IPv4 and IPv6 hosts and networks
        '''





        self.cursor.execute('ALTER TABLE %s ADD COLUMN %s %s %s'%(tableName,columnName,dataType,isNotNull))
        self.conn.commit()


    def dropColumnFromTable(self,tableName,columnName):#drop column from select table

        self.cursor.execute('ALTER TABLE %s DROP COLUMN %s'%(tableName,columnName))
        self.conn.commit()


    def insertStringDataIntoTableColumn(self,tableName,columnName,value):

        #if type(value) == 'str'
        #print  type(value)
        command = 'INSERT INTO %s '%tableName + '(%s)'%columnName +' VALUES '+'('+'\''+ value +'\'' +')'
    #    print command
       # self.cursor.execute('INSERT INTO %s '%tableName + '(%s )'%columnName +'VALUES '+'('+ value +')')
        self.cursor.execute(command)


        #self.conn.commit()



    def insertAllDataIntoTableColumn(self,tableName,dataList):
        #print tableName
        ''' insert all data from selected list '''
        #print str(dataList)[1:-1]
        #print len(dataList)
        command = 'INSERT INTO %s'%tableName +' VALUES ('+ str(dataList)[1:-1] +')'
        #print command
        self.cursor.execute(command)


        self.conn.commit()



    def updateDataToTable(self,tableName,whereKey,whereData,columnName,columnNameValue):
        '''update value from select key id'''


        command = 'UPDATE %s SET %s ='%(tableName,columnName) + '\'' +'%s'%columnNameValue + '\''+ ' WHERE %s ='%whereKey +'\''+ whereData +'\''
        #print command
        # UPDATE COMPANY SET SALARY = 15000 WHERE ID = 6;
        try:
            self.cursor.execute(command)
        except:
            pass
            #print 'none'

        self.conn.commit()

        #"UPDATE Employee SET age=12 WHERE name='Gopher'"



    def testRun():
        dbName = 'mydb'
        userID = 'postgres'
        userPW = '5j/u.42017'
        hostIP = '192.168.161.47'
        hostPort = '5432'
        print connectPostgreSQL(dbName,userID,userPW,hostIP,hostPort)


#testRun()
