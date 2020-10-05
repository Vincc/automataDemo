from automaton import *
import pygame
from time import sleep
class Enemy(Automaton):
    PlayerNear = Event("wander","follow")
    PlayerFar = Event("follow","wander")


box_1x,box_1y = 200,200
box_2x,box_2y = 30,30
pygame.init()

box_2=Enemy(initial_state="wander")
size = width, height = 300,300
speed = [2,2]
scrn = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()
while not done:
        clock.tick(60)
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        print(box_1y)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and box_1y > 0: box_1y -= 3
        if pressed[pygame.K_DOWN] and box_1y +10 < 300: box_1y += 3
        if pressed[pygame.K_LEFT] and box_1x  > 0: box_1x -= 3
        if pressed[pygame.K_RIGHT] and box_1x+10 < 300: box_1x += 3
        scrn.fill((0, 0, 0))
        pygame.draw.rect(scrn, (255, 0, 0), pygame.Rect(box_1x, box_1y, 10, 10))
        pygame.draw.rect(scrn, (255, 0, 0), pygame.Rect(box_2x, box_2y, 10, 10))
        if box_1y-box_2y <= 50 or box_1x-box_2x <= 50:
            if box_2.state != "follow":
                box_2.event("PlayerNear")
        else:
            if box_2.state != "wander":
                box_2.event("PlayerFar")
        if box_2.state == "follow":
            if box_1x > box_2x:
                box_2x+=1
            else:
                box_2x -= 1
            if box_1y > box_2y:
                box_2y+=1
            else:
                box_2y -= 1

        if box_2.state == "wander":
            if 30 > box_2x:
                box_2x+=1
            else:
                box_2x -= 1
            if 30 > box_2y:
                box_2y+=1
            else:
                box_2y -= 1


        pygame.display.flip()




