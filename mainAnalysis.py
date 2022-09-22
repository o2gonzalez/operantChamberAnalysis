###--- LIBRARY IMPORTS ---###
from importlib import reload
import numpy as np
import matplotlib.pyplot as plt

import dataFuncs

#--- load data ---#
fileNames = ['3rdDayRewardHabBL32.txt','3rdDayRewardHabBR22.txt','3rdDayRewardHabTL31.txt','3rdDayRewardHabTR24.txt']
names = ['BL32','BR22','TL31','TR24'] # Animal IDs
dataList = dataFuncs.loadData(fileNames) # creates list of complete datasets | dataList[animal][row][col]

#--- get reward info per animal ---#
rewardCounts = dataFuncs.getRewardCounts(dataList,names) # returns / prints the percent performance | (number of trials with reward / total number of trials) * 100


