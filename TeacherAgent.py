from Agent import Agent
from Agent import State
from pygame import Vector2


class TeacherAgent(Agent):
    
    def update(self):
        pass
    
    def look(self):
        print(f"{self.name} is looking.")

    def run_back(self):
        print(f"{self.name} is running back.")
        self.velocity = Vector2(-self.speed, 0)