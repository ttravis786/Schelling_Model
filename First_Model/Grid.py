# top right issues, they used surface of 3D shape.
# colours will be dict in form c = {'b':0.4, 'g':0.6} where the number is the proportion
import Cell
#import Grid_Agent
import Agent
import random
import numpy as np

class Grid():
    def __init__(self, cell_width, occupied_proportion, colours):
        self.cell_width = cell_width
        self.occupied_proportion = occupied_proportion
        self.colours = colours
        self.generate_index()
        self.generate_cells()
        self.generate_agents()
        self.find_unoccupied_cells()

    def generate_index(self):
        indexes = []
        for i in range(0,self.cell_width):
            for j in range(0, self.cell_width):
                indexes.append((i,j))
        self.indexes = indexes

    def generate_cells(self):
        self.cells = {}
        for index in self.indexes:
            self.cells[index] = Cell.Cell(index[0], index[1], self)

    def generate_agents(self):
        n_of_cells = len(self.indexes)
        for colour in self.colours:
            proportion = self.colours[colour]
            n_of_colour = int(proportion *
                              n_of_cells *
                              self.occupied_proportion)
            cell_sample = random.sample(self.find_unoccupied_cells(), n_of_colour)
            for cell in cell_sample:
                cell.agent = Agent.Agent(cell, colour, f_a=0.35)

    def find_unoccupied_cells(self):
        unoccupied_cells = []
        for cell in self.cells.values():
            if not cell.is_occupied():
                unoccupied_cells.append(cell)
        self.unoccupied_cells = unoccupied_cells
        return unoccupied_cells

    def find_occupied_cells(self):
        occupied_cells = []
        for cell in self.cells.values():
            if cell.is_occupied():
                occupied_cells.append(cell)
        return occupied_cells

    def get_empty_cells(self):
        return self.unoccupied_cells

    def relocate_agent(self, original_cell, new_cell, agent):
        self.unoccupied_cells.remove(new_cell)
        self.unoccupied_cells.append(original_cell)
        original_cell.agent = None
        new_cell.agent = agent
        agent.cell = new_cell

    def preform_iteration(self):
        ab = self.find_occupied_cells()
        for cell in ab:
            if cell.agent is None:
                print(1)
                continue
            old, new = cell.agent.attempt_relocate()

    def get_cell(self, x, y):
        return self.cells[x,y]

    def get_cell_colour_coords(self):
        colour_coords = {}
        for colour in self.colours:
            colour_coords[colour] = []
        for cell in self.find_occupied_cells():
            agent = cell.agent
            colour_coords[agent.colour].append([agent.cell.x, agent.cell.y])

        for colour in self.colours:
            colour_coords[colour] = np.array(colour_coords[colour])

        return colour_coords

