from Agent import Agent
from Agent import State

class TeacherAgent(Agent):

    def __init__(self,x,y,color,color_base_position,name):
        super().__init__(x,y,color,color_base_position,name)
        self.target = None

    def update(self, environment,dt):
        grid_size = environment["grid_size"]
        if self.target is None or self.target.state != State.HUNGRY:
            for i in range(len(environment["child"])):
                if environment["child"][i].state == State.HUNGRY:
                    self.target = environment["child"][i]

            if self.target is None or self.target.state != State.HUNGRY:
                self.backToSpawn(grid_size)
        else:
            self.searchChild(grid_size)

    def backToSpawn(self,grid_size):
        print(f"{self.name} is running back.")
        self.moveToPosition(self.base_position[0], self.base_position[1], grid_size)

    def searchChild(self,grid_size):
        child_x, child_y = self.target.x, self.target.y
        self.moveToPosition(child_x, child_y, grid_size)
