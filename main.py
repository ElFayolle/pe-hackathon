import numpy
import xcover 
import matplotlib.pyplot as plt



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
    
