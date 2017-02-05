'''
Created on Feb 5, 2017
quick and dirty json to csv converter
@author: doktorbrown
'''
import json
import csv


rawJson = 'markerbotreader-Checkups-export.json'
csvOutput = '3D_Print_Submissions.csv'


# opens json and splits it into list entries based on repetition of "{u'CheckData':   etc" string

def jsonParser(rawJson):
    with open(rawJson) as data_file:    
        data = json.load(data_file)    
        strData = str(data)
        splitStrData= strData.split(" u'")
        strSplitStrData = str(splitStrData)
        listSplitData= list(strSplitStrData.split("{u'CheckData': {u'Status':"))
        print len(listSplitData), "records will be converted"

        return listSplitData


# takes list entries and outputs to row in csv

def csvOut(csvOutput,inputData):
    for i in range(0,len(inputData)):
        strInputData= str(inputData[i])
        splitInputData= strInputData.split(',')
        listInputData = list(splitInputData)
        csvLogs = csv.writer(open(csvOutput, 'a'))
        csvLogs.writerow(listInputData)



csvOut(csvOutput,jsonParser(rawJson))
print "csv file has been exported"
