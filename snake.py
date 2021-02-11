import pygame, time
from pygame.locals import *
pygame.init()
disp_width =  960
disp_height = 540

snake_size = 10

dis=pygame.display.set_mode((disp_width, disp_height))
pygame.display.update()
pygame.display.set_caption("Snake By Luks")
gameOver = False
x_start = (disp_width-snake_size)/2
y_start = (disp_height-snake_size)/2
dx = 0
dy = 0
snake_speed = 30

timer = pygame.time.Clock()

head_c = (0, 0, 225)

black = (0,0,0)

red = (255,0,0)

font = pygame.font.SysFont(None, 50)

def message(color, text):
    display_text = font.render(text, True, color)
    dis.blit(display_text, [disp_width/2, disp_height/2])


curr_x = x_start
curr_y = y_start

snake_length = 1



start = False
while not start:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            start = True
            dis.fill(black)
pygame.draw.rect(dis, head_c, (x_start, y_start, 10, 10))
message(red, "Press any key to begin")
while not gameOver :
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameOver=True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                dx = 0
                dy = 0
            elif event.key == pygame.K_LEFT:
                dx = -10
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = 10
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -10
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = 10
    if curr_x > disp_width or curr_x < 0 or curr_y > disp_height or curr_y < 0:
        gameOver = True
        break
    pygame.draw.rect(dis, black, (curr_x, curr_y, 10, 10))           
    curr_y = curr_y+dy
    curr_x = curr_x+dx
    pygame.draw.rect(dis, head_c, (curr_x, curr_y, 10, 10))
    pygame.display.update()
    timer.tick(snake_speed)
time.sleep(1)
pygame.quit()
quit()
