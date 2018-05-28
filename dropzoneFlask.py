import os
import json
import sys



from flask import Flask, render_template, request
from flask_dropzone import Dropzone
from flask import jsonify


## initial
sys.path.append("c:/webServer/python")

##alpha script
import postgreSQLCall
reload(postgreSQLCall)

print "postgreSQLCall",postgreSQLCall
sysPath = sys.path


class callTactic():

    def __init__(self, name):
        self.name = name    




#basedir = os.path.abspath(os.path.dirname(__file__))
uploadFileList = []
app = Flask(__name__)

app.config.update(
    UPLOADED_PATH= 'static/uploads',
	DROPZONE_ALLOWED_FILE_CUSTOM  = True,
	DROPZONE_ALLOWED_FILE_TYPE='image/*, .json , .png, .jpg , .atlas' ,
    DROPZONE_MAX_FILE_SIZE=2048,
    DROPZONE_MAX_FILES=99999,
    DROPZONE_DEFAULT_MESSAGE = 'Drop Spine Files, atlas, json, png',
)
 #   DROPZONE_REDIRECT_VIEW='completed'

dropzone = Dropzone(app)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files.get('file')
        f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
      #  print f.filename
        uploadFileList.append(f.filename)
    return render_template('upload.html')





@app.route('/projectMain')
def projectMain():
    
   # return "project Main"
    return render_template('main.html')





@app.route('/completed')
def completed():
   # print uploadFileList
   # eventFiles = uploadFileList
    uploadFileList = []


@app.route('/hello/')
def hello():
    return render_template('hello.html')

@app.route('/pixiSpine')
def pixiSpine():
    print "uploadFileList",uploadFileList
    bgList = ["bg.png","BG.png","Bg.png","bg.jpg","BG.jpg","Bg.jpg"]
    if len(uploadFileList) == 0:
        pass
    else:
        bgImage = "none"
        for i in uploadFileList:
            if i.split(".")[1] == "json":
                spineJson = i
            elif i.split(".")[1] == "png":
                spineSpriteImage = i
            elif i.split(".")[1] == "atlas":
                spineSpriteAtlas = i
            elif i in bgList:
                bgImage = i

           # data = "test test test"
        effectName = getEffectName(spineJson)
        
        return render_template('pixiSpine.html',uploadFileList= uploadFileList, effectName = effectName,spineJson=spineJson,bgImage = bgImage )
    
    

@app.route('/toFlask', methods=['GET', 'POST'])
def toFlask(x=None, y=None):
    
    print "asdadasd"
    
    return render_template('toFlask.html')
    # do something to send email
  #  pass

@app.route('/cleanReq/',methods=['POST','GET'])
def cleanReq():
    
    uploadFileList = []
    print "asdsad"
    name=request.form.get('name')
   # age=int(request.form.get('age'))
   # print name,age
   # if name=='kikay' and age==18:
    print uploadFileList
    return name
  #  else:
    #    return jsonify({'result':'error'})
   # 



##AJAX test  Start####    
@app.route('/jqTest',methods=['POST','GET'])
def jqTest():
    
    return render_template('jqTestImport.html')



@app.route('/mystring')
def mystring():
    return 'my string'



@app.route('/mydict', methods=['GET', 'POST'])
def mydict():
    d = {'name': 'xmr', 'age': 18}
    #getDB = postgreSQLCall.callPostgre('3D_db','postgres','5j/u.42017','192.168.161.47','5432')  
    #getTacticDB = postgreSQLCall.callPostgre('simpleslot','postgres','','192.168.163.60','5432')  
    getSthpwDB = postgreSQLCall.callPostgre('sthpw','postgres','','192.168.163.60','5432')   
  #  projectRows = self.getTacticDB.getRowDataFromTable('game')
   # assetRows = getTacticDB.getRowDataFromTable('assets')
    userProcessData =  getSthpwDB.getRowDataFromTable('login')
    #print "getTacticDB",getTacticDB
    #print "getSthpwDB",getSthpwDB
   # print "projectRows",projectRows
   # print "userProcessData",userProcessData
    print "userProcessData",userProcessData[0][1]
    return jsonify(userProcessData)
    
@app.route('/mylist')
def mylist():
    l = ['xmr', 18]
    print('mylist')
    return json.dumps(l)  



@app.route('/name', methods=['POST'])
def getname():
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    d = {'name': firstname + ' ' + lastname, 'age': 18}
    print(d)
    return jsonify(d)




@app.route('/mytable')
def mytable():
    table = [('id', 'name', 'age', 'score'),
        ('1', 'xiemanrui', '18', '100'),
        ('2', 'yxx', '18', '100'),
        ('3', 'yaoming', '37', '88')]

    print('mytable')
    data = json.dumps(table)
    print(data)
    return data


@app.route("/testtest",methods=['POST','GET'])
def testtest():
    return "i'm test"










##KPI indexPage start




@app.route("/indexPage",methods=['POST','GET'])
def indexPage():
   # return "i'm test"
    app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'
    print "path",app.config['UPLOADED_PATH']
    return render_template('indexPageTest.html')






##KPI indexPage End


##dropzone upload test

@app.route('/dropzoneUploadTest', methods=['GET', 'POST'])
def upload_file():
    
    #import os
    app.config['UPLOADED_PATH'] ="c:/webServer/uploads"
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    #return "upload test"
    return render_template('dropzoneUploadTest.html')





@app.route('/qclist', methods=['GET', 'POST'])
def qclist():
    
   # return "QC List Test v 0.01"
    app.config['UPLOADED_PHOTOS_DEST']="//mcd-one/3d_project/temp"
    files_list = os.listdir(app.config['UPLOADED_PHOTOS_DEST'])
   # return render_template('manage.html', files_list=files_list)
    return render_template('qclist.html', files_list=files_list)






##AJAX test####    
















    
        
def getEffectName(jsonFile):
    path = 'c:/webServer/static/uploads/'
    fileName = path + jsonFile
    #print fileName

    with open(fileName) as data_file:    
        data = json.load(data_file)
   # print len(data.keys())
    return data["animations"].keys()[0]

if __name__ == '__main__':
    app.run(host='192.168.161.46',debug=True)