###--- LIBRARY IMPORTS ---###
import re
from this import d
import numpy as np
import matplotlib.pyplot as plt

import dataFuncs

#--- load data ---#
fileNames = ['3rdDayRewardHabBL32.txt','3rdDayRewardHabBR22.txt','3rdDayRewardHabTL31.txt','3rdDayRewardHabTR24.txt']
names = ['BL32','BR22','TL31','TR24']


data = dataFuncs.loadData(fileNames)
rewardCounts = dataFuncs.getRewardCounts(data)


for fileID in range(len(fileNames)):
    with open(fileNames[fileID]) as f:
        data = []
        contents = f.readlines()
        for lines in contents:
            data.append(lines.split())

    numTrials = int(float(data[36][1]))
    rewardNosePokes = []
    dArrayStart = 39
    rewardNosePokePosition = 9
    for ii in range(dArrayStart,dArrayStart+numTrials):
        rewardNosePokes.append(float(data[ii][rewardNosePokePosition]))
    rewardNosePokes = np.array(rewardNosePokes)

    nonPokes = np.where(rewardNosePokes==0)[0]
    percentPokes = ((numTrials-nonPokes.shape[0])/numTrials)*100
    print("Animal ID: ",names[fileID],"| Percent of Trials with Nose Pokes: ",percentPokes,"%\n")
