import os
import json
import sys

from flask import Flask, render_template, request
from flask_dropzone import Dropzone


## initial
sys.path.append("c:/webServer/python")

sysPath = sys.path



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





@app.route('/uitest/')
def uitest():
    return render_template('uitest.html')





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