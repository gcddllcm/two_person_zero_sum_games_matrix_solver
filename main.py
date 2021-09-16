import numpy as np;


def generateMatrix(): # to get the matrix from user, but for now, just set some matrix var
    # a = np.array([[1, 2, 3],
    #             [4, 5, 6],
    #             [7, 8, 9],
    #             [10, 11, 12]]);
    a = np.array([[3, 1],
                [-1, 2]]);
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
    
    
    

def test(): #for testing something whilst coding
    return 0;





if __name__ == '__main__':
    mat1 = generateMatrix();
    mat2 = generatePivotTable(mat1);
    piv = pickPivot(mat2[2]);
    print(piv);
