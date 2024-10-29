
def grid(lignes, colonnes, obstacles):
    """Création de la grille"""
    grille = np.array((lignes, colonnes))
    for (x,y) in obstacles :
        grille[x][y] = 1
    return grille