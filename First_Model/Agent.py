import random

# talk about correlation length.
# copy of book, parallel
# see paralels to phase transitions.
class Agent():
    # f_a - min tolerance
    # m - probability of relocation even if satisfied
    # W - number of cells to check for better satisfaction.
    # n_size = size to check neighbourhood
    #

    def __init__(self, cell, colour, f_a=0.3, m=0.01, w=30, n_size=5):
        self.cell = cell
        self.grid = cell.grid
        self.colour = colour
        self.f_a = f_a
        self.m = m
        self.w = w
        self.n_size = n_size
        self.current_satisfaction = None

    # returns satisfaction, 0 <= u_a <= 1
    def get_satisfaction(self):
        u_a = self.cell.get_satisfaction(
            self.colour, self.n_size, self.f_a)

        self.current_satisfaction = u_a
        return u_a

    def attempt_relocate(self):
        u_a = self.get_satisfaction()
        # probability of random reallocation even if u_a = 1
        p = random.uniform(0, 1)
        if ((u_a == 1) and
            (p >= self.m)):
            return self.cell,9
        # take a random sample of empty cells if size W.
        potential_cells = self.grid.get_empty_cells()
        if len(potential_cells) > 30:
            potential_cells = random.sample(
                list(potential_cells), self.w)

        suitable_cells = []
        suitable_cells_u = u_a
        for cell in potential_cells:
            u_c = cell.get_satisfaction(
            self.colour, self.n_size, self.f_a)

            if u_c == suitable_cells_u:
                suitable_cells.append(cell)
            elif u_c > suitable_cells_u:
                suitable_cells_u = u_c
                suitable_cells = [cell]

        if ((u_a == 1 and suitable_cells) or
                (suitable_cells_u > u_a)):
            chosen_cell = random.choice(suitable_cells)
            # relocates cell.
            self.grid.relocate_agent(self.cell, chosen_cell, self)
            return self.cell, chosen_cell
        else:
            return self.cell, 8















