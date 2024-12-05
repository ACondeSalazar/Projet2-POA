from time import sleep

from Agent import Agent
from Agent import State
import random

class ChildAgent(Agent):

    def __init__(self, x, y, color,color_base_position, name):
        Agent.__init__(self, x, y, color,color_base_position, name)
        self.hungry_timer = random.randint(3, 10)
        self.candyEat = 0

    def update(self, environment, dt):
        if self.state == State.IDLE:
            self.hungry_timer -= dt
            if self.hungry_timer <= 0:
                print("i am hungry!")
                self.change_state(State.HUNGRY)
                self.hungry_timer = random.randint(5, 20)

        elif self.state == State.HUNGRY:
            self.searchCandy(environment["grid_size"], environment["candy_pos"])
            if environment["candy_pos"][0] == self.x and environment["candy_pos"][1] == self.y:
                print("hmmm nice candy")
                self.candyEat+= 1
                self.change_state(State.RUNNING_BACK)
            else:
                print("Searching ")

        elif self.state == State.RUNNING_BACK:
            if self.x == self.base_position[0] and self.y == self.base_position[1]:
                print("i m sitting again")
                self.change_state(State.IDLE)
            else:
                self.backToSpawn(environment["grid_size"])


    def searchCandy(self,grid_size, candy_pos):
        candy_x, candy_y = candy_pos
        self.moveToPosition(candy_x, candy_y, grid_size)

    def backToSpawn(self,grid_size):
        self.moveToPosition(self.base_position[0], self.base_position[1], grid_size)

    def teacherCaughtYou(self):
        self.change_state(State.RUNNING_BACK)

    def eat(self):
        print(f"{self.name} is eating.")
        self.change_state(State.IDLE)

    def run_back(self):
        print(f"{self.name} is running back.")