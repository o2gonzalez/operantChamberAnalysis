###--- LIBRARY IMPORTS ---###
import numpy as np
import matplotlib.pyplot as plt

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
