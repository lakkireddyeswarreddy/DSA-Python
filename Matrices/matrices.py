
"""
In programming, Matrix is a two-dimensional array or a array of arrays. Where each row of the matrix is an array and all the rows are stored in a single array.
Matrices are used to represent data in a structured way, and they are widely used in various fields such as computer graphics, machine learning, scientific computing, etc.
Matrices can be represented in python using nested lists or using numpy library.
We can create a matrix using nested lists as shown below:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
We can access the elements of the matrix using the row and column indices as shown below:
print(matrix[0][0]) # prints 1

We can also create a matrix using numpy library as shown below:
import numpy as np
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
Shape of the matrix is represented as no.of.rows * no.of.columns. 

We can perform various operations on matrices such as addition, subtraction, multiplication, etc. using numpy library.
import numpy as np
matrix1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
matrix2 = np.array([
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
])
matrix_sum = matrix1 + matrix2
print(matrix_sum) # prints [[10 10 10] [10 10 10] [10 10 10]]
matrix_product = np.dot(matrix1, matrix2)
print(matrix_product) # prints [[ 30  24  18] [ 84  69  54] [138 114  90]]

We can also perform various operations on matrices using nested loops.

Transpose of a matrix is obtained by swapping the rows and columns of the matrix.
For example, the transpose of the matrix [[1, 2, 3], [4, 5, 6], [7, 8, 9]] is [[1, 4, 7], [2, 5, 8], [3, 6, 9]]. Rows will become columns and columns will become rows.

There are two types of matrices:
1. Square matrix: A matrix with same number of rows and columns.
2. Rectangular matrix: A matrix with different number of rows and columns.  
3. Special types of square matrices:
   a. Diagonal matrix: A square matrix in which all the elements outside the main diagonal are zero.
   b. Identity matrix: A square matrix in which all the elements of the main diagonal are one and all other elements are zero.
   c. Symmetric matrix: A square matrix that is equal to its transpose.
   d. Skew-symmetric matrix: A square matrix that is equal to the negative of its transpose.
   e. Upper triangular matrix: A square matrix in which all the elements below the main diagonal are zero.
   f. Lower triangular matrix: A square matrix in which all the elements above the main diagonal are zero.
   
There are different ways to represent a matrix in memory:
1. Row-major order: In this representation, the elements of the matrix are stored row by row in a single array.
2. Column-major order: In this representation, the elements of the matrix are stored column by column in a single array.

Sparse matrix is a matrix in which most of the elements are zero. It is more memory efficient to store only the non-zero elements of the sparse matrix along with their row and column indices.


"""

matrix1= [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

#Traversal by row

def traversal_by_row(matrix):
    result=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result.append(matrix[i][j])
    return result

# print(traversal_by_row(matrix1))

def traversal_by_column(matrix):
    result=[]
    for j in range(len(matrix[0])):
        for i in range(len(matrix)):
            result.append(matrix[i][j])
    return result

# print(traversal_by_column(matrix1))

def traversal_by_diagonal(matrix):
    result=[]
    for i in range(len(matrix)):
        result.append(matrix[i][i])
    return result

# print(traversal_by_diagonal(matrix1))

def traversal_by_anti_diagonal(matrix):
    result=[]
    for i in range(len(matrix)):
        result.append(matrix[i][len(matrix[0])-1-i])
    return result

# print(traversal_by_anti_diagonal(matrix1))

def snake_traversal(matrix):
    result=[]
    for i in range(len(matrix)):
        if i%2==0:
            result.extend(matrix[i])
        else:
            result.extend(matrix[i][::-1])
    return result

# print(snake_traversal(matrix1))

def spiral_traversal(matrix):
    
    result=[]
    
    left, right = 0, len(matrix[0])-1
    top, bottom = 0, len(matrix)-1
    
    while left<=right and top<=bottom:
    
        for i in range(left,right+1,1):
            result.append(matrix[top][i])
        
        top+=1
        
        for i in range(top, bottom+1,1):
            result.append(matrix[i][right])
            
        right-=1
        
        # if left<right:
        
        for i in range(right,left-1,-1):
            result.append(matrix[bottom][i])
            
        bottom-=1
        
        # if top<bottom:
        for i in range(bottom,top-1,-1):
            result.append(matrix[i][left])
            
        left+=1
    return result

print(spiral_traversal(matrix1))
        
    

