import pandas as pd
import numpy as np

irisdata = pd.read_csv('iris.data', sep=",", names=['sepalLength', 'sepalWidth', 'petalLength', 'petalWidth', 'class'])
winedata = pd.read_csv('wine.data', sep=",", names=['Alcohol','Malic acid','Ash','Alcalinity of ash','Magnesium','Total phenols','Flavanoids','Nonflavanoid phenols','Proanthocyanins','Color intensity','Hue','OD280/OD315 of diluted wines','Proline'  ])

def continuous_to_discrete():
    for column in irisdata:
        columnSeriesObj = irisdata[column]
        temp = pd.cut(columnSeriesObj.values, bins=5)
        irisdata.insert(1, column = columnSeriesObj.name, value = temp)
    
continuous_to_discrete()
print(irisdata)