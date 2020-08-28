import pygame
import time
import random


pygame.init()
 
class App():
    def __init__(self):
        self.white = (255, 255, 255)
        self.yellow = (255, 255, 102)
        self.black = (0, 0, 0)
        self.red = (213, 50, 80)
        self.green = (0, 255, 0)
        self.blue = (50, 153, 213)
        self.score = 0
        self.dis_width = 600
        self.dis_height = 400
         
        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Aim training by denis244')
         
        self.clock = pygame.time.Clock()
        

        self.target_block = 20
         
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)


    def Your_score(self, score):
        value = self.score_font.render("Your Score: " + str(self.score), True, self.yellow)
        self.dis.blit(value, [0, 0])
     
     
    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])
     
    def get_target(self):
        foodx = round(random.randrange(0, self.dis_width) / 10.0) * 10.0
        foody = round(random.randrange(0, self.dis_height) / 10.0) * 10.0

        b = pygame.draw.rect(self.dis, self.green, [int(foodx), int(foody), self.target_block, self.target_block])
        return b
     
    def gameLoop(self):
        game = True
        try:
            foodx = round(random.randrange(0, self.dis_width - pygame.mouse.get_pos()[0] + pygame.mouse.get_pos()[1]) / 10.0) * 10.0
            foody = round(random.randrange(0, self.dis_height - pygame.mouse.get_pos()[0] + pygame.mouse.get_pos()[1]) / 10.0) * 10.0
        except:
            foodx = round(random.randrange(0, self.dis_width) / 10.0) * 10.0
            foody = round(random.randrange(0, self.dis_height) / 10.0) * 10.0
        
        b = pygame.draw.rect(self.dis, self.green, [int(foodx), int(foody), self.target_block, self.target_block])
        while game:
            self.clock.tick(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if b.collidepoint(pygame.mouse.get_pos()):
                        self.score += 1
                        self.gameLoop()
                        
     
            self.dis.fill(self.blue)
            self.Your_score(self.score)
            if foodx >= self.dis_width or foodx < -2 or foody >= self.dis_height or foody < -2:
                self.gameLoop()

            pygame.draw.rect(self.dis, self.green, [int(foodx), int(foody), self.target_block, self.target_block])
            pygame.display.update()

        pygame.quit()
        quit()


App().gameLoop()     
 
