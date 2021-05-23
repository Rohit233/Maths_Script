import sys, getopt
import numpy as np
from stat2helper import curveType, tableValuesForStat2
from stat2 import straightLineTableFormation, parabolicCurveTableFormation, exponentialCurveTableFormation

print(str(sys.argv[1]))
x = []
y = []
singleValue = str()
for i in sys.argv[2]:
    if  i == ',':
        x.append(float(singleValue))
        singleValue = ''
    else:
        singleValue += i
# Taking Last Value
x.append(float(singleValue))
singleValue =''
for i in sys.argv[3]:
    if i == ',':
        y.append(float(singleValue))
        singleValue = ''
    else:
        singleValue+=i
# Taking Last Value
y.append(float(singleValue))
tableValuesForStat2 = tableValuesForStat2()
tableValuesForStat2.x = np.array(x)
tableValuesForStat2.y = np.array(y)
if sys.argv[1] == curveType.straightLineCurve:
    straightLineTableFormation(tableValuesForStat2)
elif sys.argv[1] == curveType.parabolicCurveType1:
    parabolicCurveTableFormation(tableValuesForStat2=tableValuesForStat2, type=curveType.parabolicCurveType1)
elif sys.argv[1] == curveType.parabolicCurveType2:
    parabolicCurveTableFormation(tableValuesForStat2=tableValuesForStat2, type= curveType.parabolicCurveType2)
elif sys.argv[1] == curveType.exponentialCurve:
    exponentialCurveTableFormation(tableValuesForStat2=tableValuesForStat2)