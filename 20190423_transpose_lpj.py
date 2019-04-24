import numpy as np

def transpose(list) :
    matrix1=np.array(list)

    b=len(matrix1[0])
    matrix2 = []
    for shape in range(b) :
        matrix2.append(matrix1[:, shape])
    matrix2=np.array(matrix2)
    return matrix2
    
# assert transpose([[1,2,5,7],[3,4,1,9],[5,6,8,7]]) == np.array([[1,2,5,7],[3,4,1,9],[5,6,8,7]]).T ,'fall'
