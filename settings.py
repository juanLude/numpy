import numpy as np
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1])
# to access the third column (column index 2), 
# we can iterate through each row and access the element at index 2:
column = [row[2] for row in matrix] 
print(column)