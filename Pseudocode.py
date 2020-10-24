import multiprocessing
import numpy as np
from numba import jit
rng = np.random.default_rng()

def will(parent, child):
    parent_copy = np.array([])
    for c in child:
        if c[1] != None:
            parent_copy = np.append(parent_copy, parent[np.where(parent[:,0] == c[1])])
            parent = np.delete(parent, np.argwhere(parent[:,0] == c[1]), 0)
    return np.reshape(np.append(parent_copy, parent), (-1, 2))

'''Init conditions'''
A_main = np.array([[k, None] for k in range(1, 6)], dtype='f')
B_main = np.array([[k, None] for k in range(1, 5)], dtype='f')
C_main = np.array([[k, None] for k in range(1, 4)], dtype='f')
D_main = np.array([[k, None] for k in range(1, 3)], dtype='f')
a_top = A_main.shape[0]
b_top = B_main.shape[0]
c_top = C_main.shape[0]
d_top = D_main.shape[0]

while True:
    ''' A list '''
    np.random.shuffle(A_main)
    # A work signal --->
    # A list <--------
    ''' B list '''
    B_main = will (B_main, A_main)
    ''' C list '''
    C_main = will(C_main, B_main)
    ''' D list '''
    D_main = will(D_main, C_main)
    print('A', A_main, '\n',  'B', B_main,'\n', 'C',  C_main,'\n',  'D',  D_main)
    ''' Shuffle '''
    D_main = rng.choice(D_main, size=D_main.shape[0], replace=False, p=[0.68, 0.32], axis=0, shuffle=False)
    C_main = rng.choice(C_main, size=C_main.shape[0], replace=False, p=[0.68, 0.16, 0.16], axis=0, shuffle = False)
    B_main = rng.choice(B_main, size=B_main.shape[0], replace=False, p=[0.68, 0.2176, 0.0512, 0.0512], axis=0, shuffle=False)
    """ Deleting weaks"""
    A_main = A_main[:-2]
    B_main = B_main[:-2]
    C_main = C_main[:-1]
    D_main = D_main[:-1]
    """ Born """
    # Born signal ----->
    # finishing signal <-----
    A_main = np.append(A_main, [[a_top + 1, B_main[0][0]], [a_top +2, B_main[1][0]]], axis=0)
    a_top += 2
    B_main = np.append(B_main, [[b_top + 1, C_main[0][0]], [b_top +2, C_main[1][0]]], axis=0)
    b_top += 2
    C_main = np.append(C_main, [[c_top + 1, D_main[0][0]]], axis=0)
    c_top += 1
    D_main = np.append(D_main, [[d_top + 1, B_main[0][0]]], axis=0)
    d_top += 1
    print('A', A_main, '\n',  'B', B_main,'\n', 'C',  C_main,'\n',  'D',  D_main)
    input()