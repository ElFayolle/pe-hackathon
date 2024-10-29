
def grid(lignes, colonnes, obstacles):
    """Création de la grille"""
    grille = np.array((lignes, colonnes))
    for (x,y) in obstacles :
        grille[x][y] = 1
    return grille
import numpy
import xcover 
import matplotlib.pyplot as plt



def grid(l,c):
    return np.zeroes((l,c))













def grid_layout(grid, pieces):

