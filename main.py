import numpy as np;


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
    mainMatrix = stackVertical;
    
    return [rowIndex, colIndex, mainMatrix, minimumVal];
    
    
    



def test():
    a = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9],
                  [10, 11, 12]]);
    
    return a;







if __name__ == '__main__':
    mat = test();
    generatePivotTable(mat);
