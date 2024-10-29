import numpy as np
import xcover 
import matplotlib.pyplot as plt

SHAPE = {'F':np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,1,0,0],[1,1,0,0,0],[0,1,0,0,0]]),
'I':np.array([[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0]]),
'L':np.array([[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0]]),
'N':np.array([[0,0,0,0,0],[0,1,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]),
'P':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[1,1,0,0,0],[1,0,0,0,0]]),
'T':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,1,0,0],[0,1,0,0,0],[0,1,0,0,0]]),
'U':np.array([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,1,0,0],[1,1,1,0,0]]),
'V':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,0,0,0,0],[1,1,1,0,0]]),
'W':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,0,0],[0,1,1,0,0]]),
'X':np.array([[0,0,0,0,0],[0,0,0,0,0],[0,1,0,0,0],[1,1,1,0,0],[0,1,0,0,0]]),
'Y':np.array([[0,0,0,0,0],[0,1,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,0,0,0]]),
'Z':np.array([[0,0,0,0,0],[0,0,0,0,0],[1,1,0,0,0],[0,1,0,0,0],[0,1,1,0,0]])
}

def grid(lignes, colonnes, obstacles):
    """Création de la grille"""
    grille = np.array((lignes, colonnes))
    for (x,y) in obstacles :
        grille[x][y] = 1
    return grille



def grid(l,c):
    return np.zeroes((l,c))













def grid_layout(grid, pieces):
    l,w = grid.shape
    grid_color = np.zeroes((l,w,3))
    for i,ligne in enumerate(grid):
        for j,pixel in enumerate(ligne):
            if pixel == 1:
                grid_color[i,j] == [0,0,0]
    plt.imshow(grid_color, interpolation='nearest')
    
