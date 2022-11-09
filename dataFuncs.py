###--- LIBRARY IMPORTS ---###
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

#--- Helper functions ---#
# load data #
def loadData(fileNames):
    dataList = []
    for fileID in fileNames:
        with open(fileID) as f:
            data = []
            contents = f.readlines()
            for lines in contents:
                data.append(lines.split())
        dataList.append(data)
    return dataList

# get percent GO correct #
def getStats(dataList,names,correctPos,totalPos,incorrectPos=None):
    percentCorrect = np.zeros(shape=len(names))
    percentIncorrect = np.zeros(shape=len(names))
    for ii in range(len(names)):
        # correct trials
        totalTrials = int(float(dataList[ii][35][totalPos]))
        correct = int(float(dataList[ii][35][correctPos]))
        percentCorrect[ii] = correct/totalTrials
        # incorrect trials
        if(incorrectPos != None):
            incorrect = int(float(dataList[ii][35][incorrectPos]))
            percentIncorrect[ii] = incorrect/totalTrials
    return percentCorrect,percentIncorrect
        

#--- data functions ---# 
# get reward info #
def getRewardCounts(dataList,names,dArrayStart=39,rewardNosePokePosition=9):
    performance = np.zeros(shape=len(names))
    for ii in range(len(names)):
        numTrials = int(float(dataList[ii][36][1]))
        rewardNosePokes = []
        for jj in range(dArrayStart,dArrayStart+numTrials):
            rewardNosePokes.append(float(dataList[ii][jj][rewardNosePokePosition]))
        rewardNosePokes = np.array(rewardNosePokes)
        nonPokes = np.where(rewardNosePokes==0)[0]
        percentPokes = ((numTrials-nonPokes.shape[0])/numTrials)*100
        print("Animal ID: ",names[ii],"| Percent of Trials with Nose Pokes: ",percentPokes,"%\n")
        performance[ii] = percentPokes
    return performance

def dataStats(dataList,names,statType):
    if(statType=='Go'):
        correctPos = 7
        totalPos = 4
        incorrectPos = 8
    elif(statType=='NoGo'):
        correctPos = 10
        totalPos = 5
        incorrectPos = 9
    elif(statType=='PreCue'):
        correctPos = 6
        totalPos = 1
        incorrectPos = None
    percentCorrect,percentIncorrect = getStats(dataList,names,correctPos,totalPos,incorrectPos)
    return percentCorrect,percentIncorrect

# Inhibition control (P_inhibition) #
def pInhibition(dataList,names):
    pNoGo,tmp = dataStats(dataList,names,'NoGo')
    tmp,pOmission = dataStats(dataList,names,'Go')
    pInhibit = (pNoGo-pOmission)/(1-pOmission)
    return pInhibit

# Response Bias #
def RI(dataList,names):
    pGo,tmp = dataStats(dataList,names,'Go')
    tmp,pNoGoi = dataStats(dataList,names,'NoGo')
    ri = -(1/2)*(stats.zscore(pGo))





