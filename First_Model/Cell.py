class Cell():
    def __init__(self, x, y, grid, agent=None):
        self.x = x
        self.y = y
        self.grid = grid
        self.agent = agent

    def is_occupied(self):
        if self.agent is None:
            return False
        else:
            return True

    def get_satisfaction(self, colour, n_size, f_a):
        x, y = self.x, self.y
        width = int((n_size - 1) / 2)
        total_near_agents = 0
        similar_near_agents = 0
        for i in range(x - width, x + width + 1):
            for j in range(y - width, y + width + 1):
                if i == x and j == y:
                    continue
                try:
                    near_cell = self.grid.get_cell(i, j)
                except:
                    continue
                if near_cell.is_occupied():
                    total_near_agents += 1
                    near_agent = near_cell.agent
                    if near_agent.colour == colour:
                        similar_near_agents += 1

        f_a_c = similar_near_agents / total_near_agents
        u_a = min([f_a_c, f_a]) / f_a
        return u_a