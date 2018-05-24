import json
print "run getDataFromTactic start"
publishConfigFile = '//mcd-one/database/assets/scripts/python2.7_alpha/publishToolConfig.json'

with open(publishConfigFile, 'r') as f:
    publishToolSettingData = json.load(f)

scripts_path = "//mcd-one/database/assets"
sys.path.append(scripts_path +  "/client")
sys.path.append(scripts_path + "/scripts/tactic_scripts/ui")

tacticHostName = publishToolSettingData['tacticHostName']
tacticHostIP = publishToolSettingData['tacticHostIP']
loginID = publishToolSettingData['tacticID']
loginPW = publishToolSettingData['tacticPW']
root = publishToolSettingData['root']
fileTypeFillet = publishToolSettingData['fileTypeFillet']

import getTacticDataD
reload(getTacticDataD)


tactic = getTacticDataD.connectToTactic(tacticHostName,tacticHostIP,loginID,loginPW)  # login tactic 

print len(tactic.getRowDataFromTactic('simpleslot/assets'))
print len(tactic.getRowDataFromTactic('simpleslot/shot'))
print len(tactic.getRowDataFromTactic('sthpw/task'))
tactic.getRowDataFromTactic('sthpw/task')[-1]
#print getTacticDataD.getRowDataFromTactic("qc_db")
tactic.testAssetInTactic()

