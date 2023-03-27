import numpy as np
from scipy.sparse import coo_matrix

# 원본 행렬 생성
row = [6,0,0,0,1,1,2,4,5]
col = [6,0,3,5,1,2,3,0,2]
value = [8,15,22,-15,11,3,-6,91,28]

# COO 형식의 희소행렬 생성
sparse_matrix = coo_matrix((value, (row,col)))

# COO 형식의 희소행렬을 CSC 형식으로 변환
csc_matrix = sparse_matrix.tocsc()

# CSC 형식의 희소행렬을 전치하여 COO 형식으로 변환

transposed_matrix = csc_matrix.transpose().tocoo()

print(transposed_matrix)