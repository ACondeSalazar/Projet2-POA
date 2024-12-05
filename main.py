from time import sleep
import pygame
import random
from Agent import Agent, State
from ChildAgent import ChildAgent
from TeacherAgent import TeacherAgent

GRID_SIZE = 10
TILE_SIZE = 50

pygame.init()

SCREEN_WIDTH = GRID_SIZE * TILE_SIZE
SCREEN_HEIGHT = GRID_SIZE * TILE_SIZE

BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (130, 123, 40)
GREEN = (0, 255, 0)
BACKGROUND_COLOR = (52, 50, 62)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
font = pygame.font.SysFont(None, 25)
pygame.display.set_caption("Classroom")





# Classe pour le jeu
class Game:
    def __init__(self):
        self.teacher = TeacherAgent(GRID_SIZE/2, GRID_SIZE-1, BLUE,GREEN, "Teacher")
        self.child_agents = [ChildAgent(i,0,RED,YELLOW,f"Child {i}") for i in range(0,GRID_SIZE,2)]
        self.candy_pos = (random.randint(0, GRID_SIZE - 1), random.randint(1, GRID_SIZE - 1))
        self.running = True

    def draw_grid(self):
        for x in range(0, SCREEN_WIDTH, TILE_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, SCREEN_HEIGHT))
        for y in range(0, SCREEN_HEIGHT, TILE_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (SCREEN_WIDTH, y))

    def draw_candy(self):
            pygame.draw.circle(screen, GREEN, (self.candy_pos[0] * TILE_SIZE + TILE_SIZE // 2, self.candy_pos[1]* TILE_SIZE + TILE_SIZE // 2), TILE_SIZE // 4)

    def update_students(self, environment, dt):
        myEnv = environment
        for child in self.child_agents:
            child.update(myEnv, dt)
            # If a child modify our environment, we need to update
            if self.check_collisions():
                myEnv = {
                    "candy_pos": self.candy_pos,
                    "grid_size": GRID_SIZE,
                    "child": [child for child in self.child_agents]
                }



    def check_collisions(self):
        environmentModify = False
        for student in self.child_agents:
            if student.x == self.candy_pos[0] and student.y == self.candy_pos[1]:
                # Ramasse un bonbon
                environmentModify = True
                self.candy_pos = (random.randint(0, GRID_SIZE - 1), random.randint(1, GRID_SIZE - 1))
            if student.x == self.teacher.x and student.y == self.teacher.y:
                student.teacherCaughtYou()
                environmentModify = True
                print("Child caught !")

        return environmentModify

    def show_text(self,msg, color, x, y):
        global screen, font
        text = font.render(msg, True, color)
        screen.blit(text, (x, y))


    def drawAgent(self, surface, agent):
        # DRAW CHAIR
        pygame.draw.rect(surface, agent.color_base_position,
                         (agent.base_position[0] * TILE_SIZE, agent.base_position[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        # DRAW CHILD
        pygame.draw.rect(surface, agent.color, (agent.x * TILE_SIZE, agent.y * TILE_SIZE, TILE_SIZE, TILE_SIZE))


    def run(self):
        dt = 0
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            environment = {
                "candy_pos": self.candy_pos,
                "grid_size" : GRID_SIZE,
                "child": [child for child in self.child_agents]
            }
            sleep(0.03)
            self.update_students(environment,dt)
            self.teacher.update(environment, dt)


            # RENDER
            screen.fill(BACKGROUND_COLOR)
            self.draw_grid()
            self.drawAgent(screen, self.teacher)
            for child in self.child_agents:
                self.drawAgent(screen, child)
                self.show_text(str(round(child.hungry_timer, 1)), BLACK, child.x* TILE_SIZE, child.y* TILE_SIZE)
            self.draw_candy()

            pygame.display.flip()

            dt = clock.tick(60) / 1000

# Lancer le jeu
game = Game()
game.run()
pygame.quit()
