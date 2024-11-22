import pygame
import random
from Agent import Agent, State
from ChildAgent import ChildAgent
from TeacherAgent import TeacherAgent


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



BLUE = (0, 0, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0,0,0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("maitresse")

dt = 0

teacher = TeacherAgent()
teacher.name = "Teacher"
teacher_pos = pygame.Vector2(700, 300)

child_agents = []
for i in range(5):
    child = ChildAgent()
    child.name = f"Child {i+1}"
    child.position = pygame.Vector2(100 + i * 100, 500)
    child.base_position = pygame.Vector2(100 + i * 100, 500)
    child_agents.append(child)

candy_pos = pygame.Vector2(400, 100)

running = True
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)

def show_text( msg, color, x, y ):
    global screen, font
    text = font.render( msg, True, color)
    screen.blit(text, ( x, y ) )

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    environement = {
        "candy_pos" : candy_pos
    }

    for child in child_agents:
        child.update(environement,dt)
        
        

    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (*teacher_pos, 50, 50))

    for child in child_agents:
        pygame.draw.rect(screen, BLUE, (*child.position, 50, 50))
        show_text(str(round(child.hungry_timer,1)), BLACK, child.position.x, child.position.y)

    pygame.draw.rect(screen, RED, (*candy_pos, 20, 20))

    pygame.display.flip()

    dt = clock.tick(60) /1000

pygame.quit()