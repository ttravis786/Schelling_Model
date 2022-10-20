import Grid
import matplotlib.pyplot as plt
import importlib
importlib.reload(Grid)
colours = c = {'b':[0.495, 0.5, 0.2], 'g':0.495, 'o':0.01}
occupied_proportion = 0.98
width=1000
new_Grid = Grid.Grid(width, occupied_proportion, colours)
for i in range(0, 5):
    if i%1 == 0:
        colour_coords = new_Grid.get_cell_colour_coords()
        fig, ax = plt.subplots()
        for colour in colour_coords:
            coords = colour_coords[colour]
            if colour == 'o':
                colour = 'r'
            ax.plot(coords[:,0], coords[:,1], f'{colour}s', linewidth=2)
        fig.show()
    print(f'iteration:{i}!!')
    new_Grid.preform_iteration()
