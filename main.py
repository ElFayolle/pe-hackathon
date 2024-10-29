import numpy as np
import xcover 
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

def possibilites(grille,piece):
    '''Renvoie toutes les possibilités de position de la pièce dans la grille avec UNE orientation particulière'''
    possib = []
    n_vide = np.sum(grille == 0)
    indice_vide = np.argwhere(grille == 0) # C'est un tableau numpy donc pas pratique pour la suite mais bon
    n_piece = np.sum(piece == 1)
    indice_piece = np.argwhere(piece == 1)
    indice_piece_1 = indice_piece[0]
    for i_vide in indice_vide:
        test = [(i_vide[0],i_vide[1])]
        flag = True
        k = 1
        while flag and k < len(indice_piece):
            i_piece = indice_piece[k]
            indice = i_vide + i_piece - indice_piece_1
            if indice[0] >= len(grille) or indice[1] >= len(grille[0]):
                flag = False
            elif grille[indice[0],indice[1]] == 1: # Si la case où l'un des bouts de la pièce doit se mettre est déjà remplie
                flag = False
            else:
                test.append((indice[0],indice[1]))
            k += 1
        
        if flag:
            pos = []
            for indice in indice_vide:
                if (indice[0],indice[1]) in test:
                    pos.append(1)
                else:
                    pos.append(0)
            possib.append(pos)
    return possib
# TEST #
grille = np.array([[1,0,1],[0,0,0],[0,0,1]])
piece = np.array([[1,1],[1,1]])
print(possibilites(grille,piece))
# FIN DU TEST #

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

