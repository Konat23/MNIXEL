import numpy as np
import scipy.signal as ssig

def greduce(g0,n):
    # %Reduce color image
    # %Sintax:
    # %	g1 = greduce(g0, a)
    # % g0 -> H * W * 3
    # % n -> numero de veces a divir en 2
    # %Edit here %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # Flitro gaussiano
    a = 0.4
    k = np.array([[0.25 - 0.5*a],
                   [0.25],
                   [a],
                   [0.25],
                   [0.25 - 0.5*a]])
    H = np.matmul(k,np.transpose(k))
    B = np.zeros_like(g0)
    B = ssig.convolve2d(g0,H,'same')

    
    # Reduccion
    H, W = g0.shape
    if H%2 == 0: # si es par
        M = int(H/2)
    else:
        M = int((H+1)/2)
    if W%2 == 0: # si es par
        N = int(W/2)
    else:
        N = int((W+1)/2)
    g1 = np.zeros((M,N))
    
    for j in range(M): # M filas N columnas
        for i in range(N): # fila j columna i 
            g1[j,i]=B[2*j, 2*i]
    n = n-1
    # repetimos la operacion si hace falta
    #print(n)
    if n>0:
        g1 = greduce(g1,n)

    return g1

if __name__ == '__main__':
    matriz = np.random.rand(8,8)
    print(greduce(matriz,2))