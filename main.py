import numpy as np
import xcover 
import matplotlib.pyplot as plt



def grid(l,c):
    return np.zeroes((l,c))

def possibilites(grille,piece):
    '''Renvoie toutes les possibilités de position de la pièce dans la grille avec UNE orientation particulière'''
    possib = []
    n_vide = np.sum(grille == 0)
    indice_vide = np.argwhere(grille == 0)
    print(indice_vide)
    n_piece = np.sum(piece == 1)
    indice_piece = np.argwhere(piece == 1)
    indice_piece_1 = indice_piece[0]
    for i_vide in indice_vide:
        test = [(i_vide[0],i_vide[1])]
        flag = True
        for i_piece in indice_piece[1:]:
            indice = i_vide + i_piece - indice_piece_1
            if indice[0] >= len(grille) or indice[1] >= len(grille[0]):
                flag = False
            elif grille[indice[0],indice[1]] == 1: # Si la case où l'un des bouts de la pièce doit se mettre est déjà remplie
                flag = False
            else:
                test.append((indice[0],indice[1]))
        if flag:
            pos = []
            for indice in indice_vide:
                if (indice[0],indice[1]) in test:
                    pos.append(1)
                else:
                    pos.append(0)
            possib.append(pos)
    return possib