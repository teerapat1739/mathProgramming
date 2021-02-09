import numpy as np


lastIndexRowEchelon = 0
def is_row_echelon(matrix):
    isRowEchelon = False
    # Create an array to store the position of pivot.
    arrSavePosition = []
    # for loop matrix
    for rIdx, row in enumerate(matrix):
        # The sum of val before pivot each row.
        sumEachRow = 0
        IsPivotexists = 1 in row
        # There must be at least one 1 in each row.
        if IsPivotexists == False:
            isRowEchelon = False
            return isRowEchelon
        for cIdx, col in enumerate(row):
            sumEachRow = sumEachRow + col
            if col == 1:
                # sum each row before 1 must be equal 0
                if (sumEachRow - col) != 0:
                    return False
                if(len(arrSavePosition) > 0):
                    # In this case, it only occurs if the pivot number has exited 
                    if rIdx > arrSavePosition[0][0] and cIdx > arrSavePosition[0][1]: # Stair step condition
                        arrSavePosition[0][0] = rIdx
                        arrSavePosition[0][1] = cIdx
                    else:
                        isRowEchelon = False
                        return isRowEchelon
                else:
                    # In this case, it only occurs if the pivot number hasn't exited 
                    arrSavePosition.append([rIdx, cIdx])
                continue
    return True
            




A = np.array([[1, 7, 3, 8],
              [0, 1, 8, 7],
              [0, 0, 1, 3],
              [1, 0, 0, 1],
              ])


print(is_row_echelon(A))