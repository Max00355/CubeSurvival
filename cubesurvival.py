import pygame
from pygame.locals import *
import random

class zc:
    def __init__(self):
        self.player = pygame.Rect(400,400, 25,25)
        self.enemies = []
        self.bullets = []
        self.size = (800, 500)
        self.level = 2
        self.kills = 0

    def run(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        facing = "up"
        clock = pygame.time.Clock()
        font = pygame.font.SysFont("Arial", 20)
        while True:
            clock.tick(45)
            if len(self.enemies) <= 10 * self.level:
                position = {0:"top", 1:"left",2:"right", 3:"bottom"}
                check = random.randint(0,3)
                if position[check] == "top":
                    y = 0
                    x = random.randint(0, self.size[0])
                elif position[check] == "left":
                    y = random.randint(0,self.size[1])
                    x = 0
                elif position[check] == "bottom":
                    y = self.size[1]
                    x = random.randint(0,self.size[0]) 
                else:
                    x = self.size[0]
                    y = random.randint(0, self.size[1])
                self.enemies.append(pygame.Rect(x,y,25,25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

            key = pygame.key.get_pressed()
            if key[K_UP]:
                facing = "up"
                self.player[1] -= 10
                if self.player[1] <= 0:
                    self.player[1] += 10
            elif key[K_DOWN]:
                facing = "down"
                self.player[1] += 10
                if self.player[1] >= self.size[1]-25:
                    self.player[1] -= 10
            elif key[K_LEFT]:
                facing = "left"
                self.player[0] -= 10
                if self.player[0] <= 0:
                    self.player[0] += 10
            elif key[K_RIGHT]:
                facing = "right"
                self.player[0] += 10
                if self.player[0] >= self.size[0]-25:
                    self.player[0] -= 10
            elif key[K_SPACE]:
                self.bullets.append((facing, pygame.Rect(self.player[0], self.player[1], 5, 5)))

            self.screen.fill((255,255,255))
            
            on = 0
            for x in self.enemies:
                player_x = self.player[0]
                player_y = self.player[1]
                enemy_x = x[0]
                enemy_y = x[1]
                if enemy_x < player_x:
                    enemy_x += 1
                    
                else:
                    enemy_x -= 1

                if enemy_y < player_y:
                    enemy_y += 1
                else:
                    enemy_y -= 1
                self.enemies[on] = pygame.Rect(enemy_x, enemy_y, 25,25)
                pygame.draw.rect(self.screen,(255,0,0),x)
                on += 1
            
            
            on = 0
            for x in self.bullets:
                if x[0] == "left":
                    x[1][0] -= 10
                elif x[0] == "right":
                    x[1][0] += 10
                elif x[0] == "down":
                    x[1][1] += 10
                elif x[0] == "up":
                    x[1][1] -= 10
                try:
                    self.bullets[on] = x
                except:
                    pass
                if len(self.bullets) > 15:
                    self.bullets = []
                pygame.draw.rect(self.screen, (0,0,0), x[1])
                on += 1
            for x in self.bullets:
                for y in self.enemies:
                    if x[1].colliderect(y):
                        self.enemies.remove(y)
                        self.bullets.remove(x)
                        self.kills += 1
                        break
            
            for x in self.enemies:
                if self.player.colliderect(x):
                    print "Game Over!"
                    print "Kills: "+str(self.kills)
                    exit()
            
            self.screen.blit(font.render("Kills: "+str(self.kills), 1, (0,0,0)), (self.size[0]-100, 10))
            pygame.draw.rect(self.screen, (0,255,0), self.player)
            pygame.display.update()
zc().run()
