from enum import Enum

State = Enum('agentState', [("IDLE", 1), ("HUNGRY", 2), ("RUNNING_BACK", 3), ("LOOKING", 4)])

class Agent():

    def __init__(self, x, y, color,color_base_position, name):
        self.name = name
        self.x = x
        self.y = y
        self.base_position = (x,y)
        self.color_base_position = color_base_position
        self.color = color
        self.state = State.IDLE
        self.speed = 40

    def update(self, environment, dt):
        pass

    def move(self, dx, dy, grid_size):
        self.x = max(0, min(grid_size - 1, self.x + dx))
        self.y = max(0, min(grid_size - 1, self.y + dy))

    def moveToPosition(self, x, y,grid_size):
        dx, dy = 0, 0
        if self.x < x:
            dx = 1
        elif self.x > x:
            dx = -1
        # Change this in "if" if you want diagonal movement
        elif self.y < y:
            dy = 1
        elif self.y > y:
            dy = -1
        self.move(dx, dy, grid_size)


    def change_state(self, new_state):
        if new_state in State:
            self.state = new_state