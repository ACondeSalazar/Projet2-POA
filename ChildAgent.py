from Agent import Agent
from Agent import State
from pygame import Vector2
import random

class ChildAgent(Agent):
    
    def __init__(self):
        super().__init__()
        self.hungry_timer = random.randint(3,10)
        
        
    def update(self,environement,dt):
        
        if self.state == State.IDLE:
            self.hungry_timer -= dt
            if self.hungry_timer <= 0:
                print("i am hungry!")
                self.change_state(State.HUNGRY)
                self.hungry_timer = random.randint(5, 20)

        
        if self.state == State.HUNGRY:
            direction = (environement["candy_pos"] - self.position)
            if direction.length() < 0.5:
                print("hmmm nice candy")
                self.change_state(State.RUNNING_BACK)
            else:
                direction = direction.normalize()
                self.move(direction, dt)
                
        if self.state == State.RUNNING_BACK:
            direction = (self.base_position - self.position)
            if direction.length() < 0.5:
                print("i m sitting again")
                self.change_state(State.IDLE)
            else:
                direction = direction.normalize()
                self.move(direction, dt)
    
    def eat(self):
        print(f"{self.name} is eating.")
        self.change_state(State.IDLE)

    def run_back(self):
        print(f"{self.name} is running back.")
        self.velocity = Vector2(-self.speed, 0)