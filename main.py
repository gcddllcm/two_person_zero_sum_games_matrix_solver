import numpy as np;


def generateMatrix(): # to get the matrix from user, but for now, just set some matrix var
    a = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
                [10, 11, 12]]);
    # a = np.array([[3, 1],
    #             [-1, 2]]);
    return a;

    
    

def generatePivotTable(matrix):
    minimumVal = 2 * abs(np.min(matrix));
    rowIndex = [];
    colIndex = [];
    
    for i in range(0, matrix.shape[0], 1):
        rowIndex.append(f"x{i}");
    for j in range(0, matrix.shape[1], 1):
        colIndex.append(f"y{j}");
        
    # add all entries by the double of the absolute value of the minimum number in matrix
    # and will take out later (to make sure that all entries are not negative value) 
    matrix = np.add(matrix, np.full(matrix.shape, minimumVal));
    
    # horizontal stack
    stackHorizontal = np.hstack(
        (matrix, np.full((matrix.shape[0], 1), 1))
        );
    
    # vertical stack
    stackVertical = np.vstack(
        (stackHorizontal, np.full((1, stackHorizontal.shape[1]), -1))
        );
    
    # set the bottom right to be 0
    stackVertical[-1][-1] = 0;
    augmentedMatrix = stackVertical;
    
    return [rowIndex, colIndex, augmentedMatrix, minimumVal];




def pickPivot(augMatrix):
    veryLargeNumber = 2 * abs(np.max(augMatrix));
    trueRow = augMatrix.shape[0] - 1;
    trueCol = augMatrix.shape[1] - 1;
    
    pivot = (augMatrix[0][0], veryLargeNumber, (0, 0));
    
    for column in range(0, trueCol, 1):
        if augMatrix[trueRow][column] < 0:
            for row in range(0, trueRow, 1):
                ongoingCell = (augMatrix[row][column], 
                               augMatrix[row][trueCol]/augMatrix[row][column],
                               (row, column));
                if augMatrix[row, column] >= 0 and 0 <= ongoingCell[1] < pivot[1]:
                    pivot = ongoingCell;
            break;
    return pivot;
    
    
    

def detectPivotTable(rowIndex, colIndex, augMatrix):
    agent = pickPivot(augMatrix);
    pivAnswer = agent[0];
    rowPiv, colPiv = agent[2];
    
    trueRow = augMatrix.shape[0] - 1;
    trueCol = augMatrix.shape[1] - 1;
    
    augMatrix_latest = np.ones(augMatrix.shape);
    
    
    for i in range(0, trueRow+1, 1):
        for j in range(0, trueCol+1, 1):
            if i != rowPiv and j != colPiv:
                augMatrix_latest[i, j] = augMatrix[i, j] - augMatrix[rowPiv, j] * augMatrix[i, colPiv] / augMatrix[rowPiv, colPiv];
    
    
    for column in range(0, trueCol+1, 1):
        if column != colPiv:
            augMatrix_latest[rowPiv, column] = augMatrix[rowPiv][column] / pivAnswer;


    for row in range(0, trueRow+1, 1):
        if row != rowPiv:
            augMatrix_latest[row, colPiv] = -augMatrix[row, colPiv] / pivAnswer;
    
    
    augMatrix_latest[rowPiv, colPiv] = 1 / pivAnswer;
    
    
    reset = rowIndex[rowPiv];
    rowIndex[rowPiv] = colIndex[colPiv];
    colIndex[colPiv] = reset;
    
    return rowIndex, colIndex, augMatrix_latest;




def ultimateSolver(matrix):
    pivotTable = generatePivotTable(matrix);
    minimumVal = pivotTable[3];
    pivotTable = detectPivotTable(pivotTable[0], pivotTable[1], pivotTable[2]);
    
    bottomRow = list(
        pivotTable[2][pivotTable[2].shape[0]-1, :]
    );
    btwPop = bottomRow.pop();
    
    
    while any(entry < 0 for entry in bottomRow):
        pivotTable = detectPivotTable(pivotTable[0], pivotTable[1], pivotTable[2]);
        bottomRow = list(
            pivotTable[2][pivotTable[2].shape[0]-1, :]
        );
        btwPop = bottomRow.pop();
        
    
    left = pivotTable[0];
    top = pivotTable[1];
    xStrategies = {};
    yStrategies = {};
    
    
    for tag in range(0, len(top), 1):
        if "x" in top[tag]:
            index = int(top[tag].split("x")[1]) + 1;
            xStrategies[f"row {index}"] = round(pivotTable[2][pivotTable[2].shape[0]-1, tag] / btwPop, 5);

        else:
            index = int(top[tag].split("y")[1]) + 1;
            yStrategies[f"column {index}"] = 0;
    
    
    for tag in range(0, len(left), 1):
        if "y" in left[tag]:
            index = int(left[tag].split("y")[1]) + 1;
            yStrategies[f"column {index}"] = round(pivotTable[2][tag, pivotTable[2].shape[1]-1] / btwPop, 5);
            
        else:
            index = int(left[tag].split("x")[1]) + 1;
            xStrategies[f"row {index}"] = 0;
            
    
    xStrategies = np.array([value for (key, value) in sorted(xStrategies.items())]).tolist();
    yStrategies = np.array([value for (key, value) in sorted(yStrategies.items())]).tolist();
    valueOfTheGame = 1/btwPop - minimumVal;
    
    return xStrategies, yStrategies, valueOfTheGame;




if __name__ == '__main__':
    test = np.array([
        [3, 3, 2, 2, 1, 1], 
        [3, 2, 2, 1, 1, 0], 
        [2, 2, 1, 1, 0, 0],
        [2, 1, 1, 0, 0, 1],
        [1, 1, 0, 0, 1, 2],
        [1, 0, 0, 1, 2, 3]
        ]);
    play = ultimateSolver(test)
    print(test)
    print(f"\nX strategy:\n{play[0]}")
    print(f"\nY strategy:\n{play[1]}")
    print(f"\nV: {play[2]}")