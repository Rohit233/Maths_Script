import numpy as np


class tableValuesForStat2:
    x = np.array([])
    y = np.array([])
    elementsXSqr = np.array([])
    elementsXy = np.array([])
    elementsXY = np.array([])
    elementsXCube = np.array([])
    elementsXToPowerFour = np.array([])
    elementsXSqrY = np.array([])
    elementlogY = np.array([])
    sumX = int()
    sumY = int()
    sumXY = int()
    sumXSqr= int()
    sumXToPowerFour = int()
    sumXSqrY = int()
    sumXcube = int()
    sumy = int()
    n = int()

class curveType :
    straightLineCurve = 'straightLineCurve'
    parabolicCurveType1 = 'parabolicCurveType1'
    parabolicCurveType2 = 'parabolicCurveType2'
    exponentialCurve = 'exponentialCurve'