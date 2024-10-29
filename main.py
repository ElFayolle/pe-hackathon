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

color_palette_rgb = [
    (255, 0, 0),      # Red
    (0, 0, 255),      # Blue
    (0, 255, 0),      # Green
    (255, 255, 0),    # Yellow
    (255, 165, 0),    # Orange
    (128, 0, 128),    # Purple
    (0, 255, 255),    # Cyan
    (255, 0, 255),    # Magenta
    (50, 205, 50),    # Lime
    (255, 192, 203),  # Pink
    (0, 128, 128),    # Teal
    (165, 42, 42)     # Brown
]

def grid(lignes, colonnes, obstacles):
    """Création de la grille"""
    grille = np.zeros((lignes, colonnes))
    for (x,y) in obstacles :
        grille[x][y] = 1
    return grille



def grid_layout(grid, piece_index, emplacement_piece):
    #grid = tableau rempli de 1 au niveau des cases obstacles et 0 ailleurs
    #pieces_index = renvoie l'index de la pièce : [0,1,0,0,0,0] pour la pièce n°2
    #emplacement_piece = oui
    l,w = len(grid), len(grid[0])
    grid_color = np.zeros((l,w,3))  
    counter = -1
    for i,ligne in enumerate(grid):
        for j,pixel in enumerate(ligne):
            if pixel == 1:
                grid_color[i,j] = [255,255,255]
            else:
                print(counter)
                counter +=1
                for k  in range(len(emplacement_piece)):
                    if emplacement_piece[k][counter] == 1:
                        piece_name = sum(piece_index[k][l]*k+1 for l in range(len(piece_index[k])))
                        grid_color[i,j] = color_palette_rgb[piece_name-1]

    plt.imshow(grid_color, interpolation='nearest')
    plt.show()

## Test 
grid_t = np.array([[1,0,1],[0,0,0],[1,0,0]])
pieces_index_t = [[1, 0], [0,1]]
pieces_emplacement_t = [[0,0,0,1,1,1],[1, 1, 1, 0, 0, 0]]
#grid_layout(grid_t,pieces_index_t, pieces_emplacement_t)

