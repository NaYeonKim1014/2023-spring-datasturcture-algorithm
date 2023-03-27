import numpy as np
from scipy.sparse import coo_matrix

# create original matrix
row = [6,0,0,0,1,1,2,4,5]
col = [6,0,3,5,1,2,3,0,2]
value = [8,15,22,-15,11,3,-6,91,28]

# create a sparse matrix in the form of COO
sparse_matrix = coo_matrix((value, (row,col)))

# transform COO format to CSC format
csc_matrix = sparse_matrix.tocsc()

# transpose CSC format to COO format

transposed_matrix = csc_matrix.transpose().tocoo()

print(transposed_matrix)