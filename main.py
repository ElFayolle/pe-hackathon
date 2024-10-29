import numpy as np
#import xcover 
import matplotlib.pyplot as plt

RAW_SHAPES = {
    "F": [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    "I": [[1, 1, 1, 1, 1]],
    "L": [[1, 0, 0, 0], [1, 1, 1, 1]],
    "N": [[1, 1, 0, 0], [0, 1, 1, 1]],
    "P": [[1, 1, 1], [1, 1, 0]],
    "T": [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    "U": [[1, 1, 1], [1, 0, 1]],
    "V": [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    "W": [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    "X": [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    "Y": [[0, 1, 0, 0], [1, 1, 1, 1]],
    "Z": [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
}

color_palette = [
    "red",
    "blue",
    "green",
    "yellow",
    "orange",
    "purple",
    "cyan",
    "magenta",
    "lime",
    "pink",
    "teal",
    "brown"
]

def grid(lignes, colonnes, obstacles):
    """Création de la grille"""
    grille = np.zeros((lignes, colonnes))
    for (x,y) in obstacles :
        grille[x][y] = 1
    return grille



def grid_layout(grid, pieces):
    l,w = len(grid), len(grid[0])
    grid_color = np.zeros((l,w,3))
    #On remplit les cases obstacles
    for i,ligne in enumerate(grid):
        for j,pixel in enumerate(ligne):
            if pixel == 1:
                grid_color[i,j] = [0,0,0]
            else:
                grid_color[i,j] = [255,255,255]
    #On remplit les cases occupées par des pièces 
    for i,piece in enumerate(pieces):
        piece_name = sum(piece[i]*i+1)

    plt.imshow(grid_color, interpolation='nearest')
    plt.show()

grid_layout(grid(5,5,[]),[])

