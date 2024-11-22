from pygame import Vector2

from enum import Enum

State = Enum('agentState', [("IDLE",1),("HUNGRY",2),("RUNNING_BACK",3),("LOOKING",4)])

class Agent():
    
    def __init__(self):
        self.name = "Agent"
        self.velocity = Vector2(0,0)
        self.state = State.IDLE
        self.speed = 40
        self.position = Vector2(0,0)
        self.base_position = Vector2(0,0)
        
        
    def update(self, dt):
        pass
    
    def move(self, direction,dt):
        self.position += direction * self.speed * dt

    def change_state(self, new_state):
        if new_state in State:
            self.state = new_state