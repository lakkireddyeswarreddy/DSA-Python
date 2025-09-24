
def setZeroes(matrix: list[list[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zero_column_index= set()
    for i in range(len(matrix)):
        is_zero_in_row=False
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                is_zero_in_row=True
                zero_column_index.add(j)
            elif (j in zero_column_index) or (is_zero_in_row):
                matrix[i][j]=0
                
    print(matrix)

matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
setZeroes(matrix)