###--- LIBRARY IMPORTS ---###
from importlib import reload
import numpy as np
import matplotlib.pyplot as plt

import dataFuncs

#--- load data ---#
fileNames = ['24thNOGOTrainingBL32.txt','24thNOGOTrainingBR22.txt']
names = ['BL32','BR22'] # Animal IDs
dataList = dataFuncs.loadData(fileNames) # creates list of complete datasets | dataList[animal][row][col]

#--- get reward info per animal ---#
rewardCounts = dataFuncs.getRewardCounts(dataList,names) # returns / prints the percent performance | (number of trials with reward / total number of trials) * 100

#--- get Go performance ---#
goCorrect,goIncorrect = dataFuncs.dataStats(dataList,names,'Go')

#--- get No Go performance ---#
nogoCorrect,nogoIncorrect = dataFuncs.dataStats(dataList,names,'NoGo')

#--- Calculate pInhibition ---#
pInhibition = dataFuncs.pInhibition(dataList,names)
