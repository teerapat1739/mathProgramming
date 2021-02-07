import numpy as np


lastIndexRowEchelon = 0
def is_row_echelon(matrix):
    # Create an array to store the position of pivot
    isRowEchelon = False
    arrSavePosition = []
    for rIdex, row in enumerate(matrix):
        # The sum of val before pivot each row
        sumEachRow = 0
        IsPivotexists = 1 in row
        if IsPivotexists == False:
            isRowEchelon = False
            return isRowEchelon
        for cIdx, col in enumerate(row):
            sumEachRow = sumEachRow + col
            if col == 1:
                if (sumEachRow - col) != 0:
                    return False
                if(len(arrSavePosition) > 0):
                    if rIdex > arrSavePosition[0][0] and cIdx > arrSavePosition[0][1]:
                        arrSavePosition[0][0] = rIdex
                        arrSavePosition[0][1] = cIdx
                    else:
                        isRowEchelon = False
                        return isRowEchelon
                else:
                    arrSavePosition.append([rIdex, cIdx])
                continue
    return True
            




A = np.array([[1, 7, 3, 8],
              [0, 1, 8, 7],
              [0, 0, 1, 3],
              [1, 0, 0, 1],
              ])


print(is_row_echelon(A))