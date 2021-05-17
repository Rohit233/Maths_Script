from decimal import Decimal

import numpy as np
from tabulate import tabulate

x = np.array([2, 4, 6, 8, 10])
y = np.array([3.07569486489466668, 12.85, 31.47, 57.38, 91.29])
digitAfterPoint = 5


def straightLineTableFormation():
    elementsXY = x * y
    elementsXSqr = np.square(x)
    showTable({'X': x, 'Y': y, 'XY': elementsXY, 'X^2': elementsXSqr},
              {'SumX': [x.sum()], 'SumY': [y.sum()], 'SumXY': [elementsXY.sum()], 'SumX^2:': [elementsXSqr.sum()]})


def parabolicCurveTableFormation(type):
    elementsXSqr = np.around(np.square(x), digitAfterPoint)
    elementsXCube = np.around(np.power(x, 3), digitAfterPoint)
    elementsXToPowerFour = np.around(np.power(x, 4), digitAfterPoint)
    elementsXY = np.around(x * y, digitAfterPoint)
    elementsXSqrY = np.around(elementsXSqr * y, digitAfterPoint)
    if type == 'a+bx^2':
        showTable({'X': x, 'Y': y, 'X^2': elementsXSqr, 'X^4': elementsXToPowerFour, 'X^2Y': elementsXSqrY},
                  {'SumX': [np.around(x.sum(), digitAfterPoint)], 'SumY': [np.around(y.sum(), digitAfterPoint)],
                   'SumX^2': [np.around(elementsXSqr.sum(), digitAfterPoint)],
                   'SumX^4': [np.around(elementsXToPowerFour.sum(), digitAfterPoint)],
                   'SumX^2Y': [np.around(elementsXSqrY.sum(), digitAfterPoint)], })
    elif type == 'ax+bx^2':
        showTable({'X': x, 'Y': y, 'X^2': elementsXSqr, 'X^3': elementsXCube, 'X^4': elementsXToPowerFour,
                   'X^2Y': elementsXSqrY, 'XY': elementsXY},
                  {'SumX': [np.around(x.sum(),digitAfterPoint)], 'SumY': [np.around(y.sum(),digitAfterPoint)], 'SumX^2': [np.around(elementsXSqr.sum(),digitAfterPoint)],
                   'SumX^3': [np.around(elementsXCube.sum(),digitAfterPoint)], 'SumX^4': [np.around(elementsXToPowerFour.sum(),digitAfterPoint)],
                   'SumX^2Y': [np.around(elementsXSqrY.sum(),digitAfterPoint)], 'SumXY': [np.around(elementsXY.sum(), digitAfterPoint)]})


def showTable(elements, sums):
    print(tabulate(elements, headers='keys', tablefmt='fancy_grid'))
    print(tabulate(sums, headers='keys', tablefmt='fancy_grid'))


# straightLineTableFormation()
parabolicCurveTableFormation('ax+bx^2')
