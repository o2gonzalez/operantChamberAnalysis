###--- LIBRARY IMPORTS ---###
import numpy as np
import matplotlib.pyplot as plt

#--- Helper functions ---#
def loadData(fileNames):
    data = []
    with open(fileNames) as f:
        contents = f.readlines()
        for lines in contents:
            data.append(lines.split())
    return data