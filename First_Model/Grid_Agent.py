import random
import Agent

# talk about correlation length.
# copy of book, parallel
# see paralels to phase transitions.
class GridAgent(Agent):

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