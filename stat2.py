import numpy as np

from tabulate import tabulate

from stat2helper import curveType


digitAfterPoint = 5


def straightLineTableFormation(tableValuesForStat2):
    tableValuesForStat2.elementsXY = np.around(tableValuesForStat2.x * tableValuesForStat2.y,digitAfterPoint)
    tableValuesForStat2.n = len(tableValuesForStat2.x)
    tableValuesForStat2.elementsXSqr = np.around(np.square(tableValuesForStat2.x),digitAfterPoint)
    tableValuesForStat2.sumX = np.around(tableValuesForStat2.x.sum(), digitAfterPoint)
    tableValuesForStat2.sumY = np.around(tableValuesForStat2.y.sum(), digitAfterPoint)
    tableValuesForStat2.sumXY = np.around(tableValuesForStat2.elementsXY.sum(), digitAfterPoint)
    tableValuesForStat2.sumXSqr = np.around(tableValuesForStat2.elementsXSqr.sum(), digitAfterPoint)
    showTable({'X': tableValuesForStat2.x, 'Y': tableValuesForStat2.y, 'XY': tableValuesForStat2.elementsXY, 'X^2': tableValuesForStat2.elementsXSqr},
              {'SumX': [tableValuesForStat2.sumX], 'SumY': [tableValuesForStat2.sumY], 'SumXY': [tableValuesForStat2.sumXY],
               'SumX^2': [tableValuesForStat2.sumXSqr]})
    getLineFit(tableValuesForStat2,curveType.straightLineCurve)

def findingAndB(solution,constA,constB,constC):
    a = 1
    b = np.around(solution[2] / solution[1], digitAfterPoint)
    normalEqn1 = [constA * a, constB * b, constC]
    a = np.around((normalEqn1[2] + (-normalEqn1[1])) / normalEqn1[0], digitAfterPoint)
    return (a,b)
def getLineFit(tableValuesForStat2,typeOfCurve):
    a = 1
    b = 1
    normalEqn1 = []
    normalEqn2 = []
    if typeOfCurve == curveType.straightLineCurve:
     normalEqn1 = [tableValuesForStat2.n * a, tableValuesForStat2.sumX * b, tableValuesForStat2.sumY]
     normalEqn2 = [tableValuesForStat2.sumX * a, tableValuesForStat2.sumXSqr * b, tableValuesForStat2.sumXY]

    #PARABOLIC CURVE FOR y=a+bx^2
    elif typeOfCurve == curveType.parabolicCurveType1:
        normalEqn1 = [tableValuesForStat2.n,tableValuesForStat2.sumXSqr,tableValuesForStat2.sumY]
        normalEqn2 = [tableValuesForStat2.sumXSqr,tableValuesForStat2.sumXToPowerFour,tableValuesForStat2.sumXSqrY]

    #PARABOLIC CURVE FOR y =ax_bx^2
    elif typeOfCurve == curveType.parabolicCurveType2:
       normalEqn1 = [tableValuesForStat2.sumXSqr,tableValuesForStat2.sumXcube,tableValuesForStat2.sumXY]
       normalEqn2 = [tableValuesForStat2.sumXcube,tableValuesForStat2.sumXToPowerFour,tableValuesForStat2.sumXSqrY]
    #EXPONENTIAL CURVE FOR y=ae^bx
    elif typeOfCurve == curveType.exponentialCurve:
        normalEqn1 = [tableValuesForStat2.n,tableValuesForStat2.sumX,tableValuesForStat2.sumY]
        normalEqn2 = [tableValuesForStat2.sumX,tableValuesForStat2.sumXSqr,tableValuesForStat2.sumXY]

    # MULTIPLYING NORMALEQN EQUATION
    if typeOfCurve == curveType.straightLineCurve:
      normalEqn1 = np.array(normalEqn1) * tableValuesForStat2.sumX
      normalEqn2 = np.array(normalEqn2) * tableValuesForStat2.n
    elif typeOfCurve == curveType.parabolicCurveType1:
        normalEqn1 = np.array(normalEqn1) * tableValuesForStat2.sumXSqr
        normalEqn2 = np.array(normalEqn2) * tableValuesForStat2.n
    elif typeOfCurve == curveType.parabolicCurveType2:
        normalEqn1 = np.array(normalEqn1) * tableValuesForStat2.sumXcube
        normalEqn2 = np.array(normalEqn2) * tableValuesForStat2.sumXSqr
    elif typeOfCurve == curveType.exponentialCurve:
        normalEqn1 = np.array(normalEqn1) * tableValuesForStat2.sumX
        normalEqn2 = np.array(normalEqn2) * tableValuesForStat2.n

    solution = normalEqn1 - normalEqn2
    if typeOfCurve == curveType.straightLineCurve :
      valueOfAndB = findingAndB(solution=solution, constA=tableValuesForStat2.n, constB=tableValuesForStat2.sumX,constC=tableValuesForStat2.sumY)
      b = valueOfAndB[1]
      a = valueOfAndB[0]
      if b < 0:
        print('y=' + str(a) + str(b) + 'x')
      else:
        print('y=' + str(a) + '+' + str(b) + 'x')
    elif typeOfCurve == curveType.parabolicCurveType1:
        valueOfAndB = findingAndB(solution=solution, constA=tableValuesForStat2.n, constB=tableValuesForStat2.sumXSqr,constC=tableValuesForStat2.sumY)
        b = valueOfAndB[1]
        a = valueOfAndB[0]
        if b < 0 :
            print('y=' + str(a) + str(b) + 'x^2')
        else:
            print('y=' + str(a) + '+' + str(b) + 'x^2')
    elif typeOfCurve == curveType.parabolicCurveType2:
        valueOfAndB = findingAndB(solution=solution, constA=tableValuesForStat2.sumXSqr, constB=tableValuesForStat2.sumXcube,
                    constC=tableValuesForStat2.sumXY)
        b  = valueOfAndB[1]
        a = valueOfAndB[0]
        if b < 0 :
            print('y=' + str(a) + "x" + str(b) + 'x^2')
        else:
            print('y=' + str(a) + "x" + '+' + str(b) + 'x^2')
    elif typeOfCurve == curveType.exponentialCurve:
        valueOfAndB = findingAndB(solution= solution, constA= tableValuesForStat2.n,constB= tableValuesForStat2.sumX,constC=tableValuesForStat2.sumY)
        b = np.around(valueOfAndB[1]/0.4343,digitAfterPoint)
        a = np.around(10**valueOfAndB[0],digitAfterPoint)
        print('y='+str(a)+' e^'+str(b)+'x')

def parabolicCurveTableFormation(type,tableValuesForStat2):
   tableValuesForStat2.n = len(tableValuesForStat2.x)
   tableValuesForStat2.elementsXSqr = np.around(np.square(tableValuesForStat2.x), digitAfterPoint)
   tableValuesForStat2. elementsXCube = np.around(np.power(tableValuesForStat2.x, 3), digitAfterPoint)
   tableValuesForStat2.elementsXToPowerFour = np.around(np.power(tableValuesForStat2.x, 4), digitAfterPoint)
   tableValuesForStat2. elementsXY = np.around(tableValuesForStat2.x * tableValuesForStat2.y, digitAfterPoint)
   tableValuesForStat2. elementsXSqrY = np.around(tableValuesForStat2.elementsXSqr * tableValuesForStat2.y, digitAfterPoint)
   tableValuesForStat2.sumX = np.around(tableValuesForStat2.x.sum(), digitAfterPoint)
   tableValuesForStat2.sumY = np.around(tableValuesForStat2.y.sum(), digitAfterPoint)
   tableValuesForStat2.sumXSqr =np.around(tableValuesForStat2.elementsXSqr.sum(), digitAfterPoint)
   tableValuesForStat2.sumXToPowerFour = np.around(tableValuesForStat2.elementsXToPowerFour.sum(), digitAfterPoint)
   tableValuesForStat2.sumXSqrY = np.around(tableValuesForStat2.elementsXSqrY.sum(), digitAfterPoint)
   tableValuesForStat2.sumXY = np.around(tableValuesForStat2.elementsXY.sum(), digitAfterPoint)
   tableValuesForStat2.sumXcube = np.around(tableValuesForStat2.elementsXCube.sum(), digitAfterPoint)
   if type == curveType.parabolicCurveType1:
      showTable({'X': tableValuesForStat2.x, 'Y': tableValuesForStat2.y, 'X^2': tableValuesForStat2.elementsXSqr, 'X^4': tableValuesForStat2.elementsXToPowerFour,
                   'X^2Y': tableValuesForStat2.elementsXSqrY},
                  {'SumX': [tableValuesForStat2.sumX],
                   'SumY': [tableValuesForStat2.sumY],
                   'SumX^2': [tableValuesForStat2.sumXSqr],
                   'SumX^4': [tableValuesForStat2.sumXToPowerFour],
                   'SumX^2Y': [tableValuesForStat2.sumXSqrY], })
      getLineFit(tableValuesForStat2,curveType.parabolicCurveType1)
   elif type == curveType.parabolicCurveType2:
        showTable({'X': tableValuesForStat2.x, 'Y': tableValuesForStat2.y, 'X^2': tableValuesForStat2.elementsXSqr, 'X^3': tableValuesForStat2.elementsXCube,
                   'X^4': tableValuesForStat2.elementsXToPowerFour,
                   'X^2Y': tableValuesForStat2.elementsXSqrY, 'XY': tableValuesForStat2.elementsXY},
                  {'SumX': [tableValuesForStat2.x.sum()],
                   'SumY': [tableValuesForStat2.y.sum()],
                   'SumX^2': [tableValuesForStat2.sumXSqr],
                   'SumX^3': [tableValuesForStat2.sumXcube],
                   'SumX^4': [tableValuesForStat2.sumXToPowerFour],
                   'SumX^2Y': [tableValuesForStat2.sumXSqrY],
                   'SumXY': [tableValuesForStat2.sumXY]})
        getLineFit(tableValuesForStat2,curveType.parabolicCurveType2)

def exponentialCurveTableFormation(tableValuesForStat2):
    tableValuesForStat2.n = len(tableValuesForStat2.x)
    tableValuesForStat2.elementsXSqr = np.around(np.square(tableValuesForStat2.x), digitAfterPoint)
    tableValuesForStat2.elementlogY = np.around(np.log10(tableValuesForStat2.y), digitAfterPoint)
    tableValuesForStat2.elementsXY = np.around(tableValuesForStat2.x * tableValuesForStat2.elementlogY, digitAfterPoint)
    tableValuesForStat2.sumXSqr = np.around(tableValuesForStat2.elementsXSqr.sum(), digitAfterPoint)
    tableValuesForStat2.sumY =  np.around(tableValuesForStat2.elementlogY.sum(), digitAfterPoint)
    tableValuesForStat2.sumy = np.around(tableValuesForStat2.y.sum(), digitAfterPoint)
    tableValuesForStat2.sumX = np.around(tableValuesForStat2.x.sum(), digitAfterPoint)
    tableValuesForStat2.sumXY = np.around(tableValuesForStat2.elementsXY.sum(), digitAfterPoint)
    showTable({'x': tableValuesForStat2.x, 'y': tableValuesForStat2.y, 'Y': tableValuesForStat2.elementlogY, 'x^2': tableValuesForStat2.elementsXSqr, 'xY': tableValuesForStat2.elementsXY},
              {'Sumx': [tableValuesForStat2.sumX],
               'Sumy': [tableValuesForStat2.sumy],
               'SumY': [tableValuesForStat2.sumY],
               'Sumx^2': [tableValuesForStat2.sumXSqr],
               'Sumx*Y': [tableValuesForStat2.sumXY]
               })
    getLineFit(tableValuesForStat2,curveType.exponentialCurve)

def showTable(elements, sums):
    print(tabulate(elements, headers='keys', tablefmt='fancy_grid'))
    print(tabulate(sums, headers='keys', tablefmt='fancy_grid'))

