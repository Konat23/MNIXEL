import numpy as np
B = np.load('model/B.npy')
W = np.load('model/W.npy')

def y_prob (W,B,X):

    # In this function you compute y_prob:

    # Please, don't use other names for your variables. Only use the names proposed by this function definition (Z, Zexp and Y_prob)

    # YOUR CODE STARTS HERE

    # Compute Z
    # Aqui hubiese usado mejor:

    # Z = np.matmul(W,X)+B[:,None]
    Z = np.matmul(W,X.T)+B[:,None]
    # Then, compute Zexp
    Zexp = np.exp(Z)
    # And finally, you compute the sum of elements in Zexp
    # Zexp_sum = np.sum(Zexp,0)
    Zexp_sum = np.sum(Zexp,0)


    # YOUR CODE ENDS HERE
    # Z = Zexp / Zexp_sum
    Y_prob = Zexp / Zexp_sum

    return Y_prob.T

def y_class (Y_prob):  # categorical

    #y_prob is all dataset i.e is a size of (m,1) or (1,m)

    # Please, don't use other names for your variables. Only use the names proposed by this function definition (Y_class)

    # YOUR CODE STARTS HERE

    # Hint:
    # Find the maximum value in Y_prob
    #Y_class=  Y_prob.index(max(Y_prob)) # Y_prob[1]= [0.2,0.7,0.1] so Y_class[1]=1
    #Y_class = Y_prob[(np.max(Y_prob,1)[:,None] == Y_prob)] # Esto saca el maximo, mas no el indice
    Y_class = np.argmax(Y_prob,1)
    # YOUR CODE ENDS HERE

    return Y_class

