import numpy as np 

def G(A : np.array, C : np.array):
    n = A.shape[0]
    out = np.vstack([C @ np.linalg.matrix_power(A, i) for i in range(n)])
    return out

m = 1
k = 1
b = 1/2

A = np.array([[0, 1],
              [-k/m, -b/m]])
B = np.array([[0], 
              [1/m]])
C = np.array([1, 0])

if __name__ == '__main__':
    g = G(A, C)
    is_vis1 = np.linalg.matrix_rank(g) == A.shape[0]
    print(is_vis1)

#odp na podstawie macierzy G można stwierdzić że układ jest obserwowalny

