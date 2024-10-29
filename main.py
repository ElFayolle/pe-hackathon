import numpy as np
import xcover 
import matplotlib.pyplot as plt

RAW_SHAPES = {
    0: [[1, 1, 0], [0, 1, 1], [0, 1, 0]],
    1: [[1, 1, 1, 1, 1]],
    2: [[1, 0, 0, 0], [1, 1, 1, 1]],
    3: [[1, 1, 0, 0], [0, 1, 1, 1]],
    4: [[1, 1, 1], [1, 1, 0]],
    5: [[1, 1, 1], [0, 1, 0], [0, 1, 0]],
    6: [[1, 1, 1], [1, 0, 1]],
    7: [[1, 1, 1], [1, 0, 0], [1, 0, 0]],
    8: [[1, 0, 0], [1, 1, 0], [0, 1, 1]],
    9: [[0, 1, 0], [1, 1, 1], [0, 1, 0]],
    10: [[0, 1, 0, 0], [1, 1, 1, 1]],
    11: [[1, 1, 0], [0, 1, 0], [0, 1, 1]],
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

def result_into_matrix(L):
    piece_index = L[:,0:12]
    piece_emplacement = L[:,13:]
    return piece_index, piece_emplacement


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


def grid_layout(grid, liste_sol):
    #grid = tableau rempli de 1 au niveau des cases obstacles et 0 ailleurs
    piece_index, emplacement_piece = result_into_matrix(liste_sol)
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

def dégage_doublons (liste):
    indices = []
    i = 0
    while i < len(liste) :
        indices = []
        for j in range(i+1, len(liste)):
            if np.array_equal(liste[i],liste[j]):
                indices.append(j)
        print(indices)
        for k in sorted(indices, reverse = True) :
            liste.pop(j)
        i += 1
    return(liste)


def rotations_et_symetries(forme_géométrique):
    forme = np.array(forme_géométrique)
    
    rot_et_sym = []
    for j in range (2):
        
        
        for i in range(4):
            forme = np.rot90(forme)
            rot_et_sym.append(forme)
        np.flip(forme, axis = j)
    return(rot_et_sym)
    


def solve(grille,shape,n):
    matrix=[]
    for ind,(key,value) in enumerate(shape.items()):
        Rot_sym=(rotations_et_symetries(value))
        L=[0 for i in range(n)]
        L[key]=1
        for form in Rot_sym:
            possib=possibilites(grille,form)
            for pos in possib:
                matrix.append(L+pos)
    res=list(xcover.covers_bool(np.array(matrix,dtype=bool)))[0]
    print(res)
    SOLUTION=[]
    for x in res:
        SOLUTION.append(matrix[x])
        grid_layout(grille,np.array(SOLUTION))
    return np.array(SOLUTION)




## Test 
grid_t = np.array([[1,0,1],[0,0,0],[1,0,0]])
pieces_index_t = {0:np.array([[1, 0],[1,1]]),1:np.array([[1, 0],[1,1]])}
pieces_emplacement_t = [[0,0,0,1,1,1],[1, 1, 1, 0, 0, 0]]


#print(solve(grid_t,pieces_index_t,2))
solve(grid(6,10,[]),RAW_SHAPES,12)
