import pygame,time,random

pygame.init()

white = (255,255,255)
yellow = (255,255,102)
balck = (0,0,0)
red = (213,50,80)
green = (0,255,0)
blue = (50,153,213)

width = 800
height = 600
dis = pygame.display.set_mode(width,height)
pygame.display.set_mode("Snake Game")

clock = pygame.time.clock()

snake_block = 10
snake_speed = 12

font_style = pygame.font.SysFont("bahnschrift",25)
score_font = pygame.font.SysFont("comicsansms",35)

def Your_score(score):
    value = score_font.render("Your Score:" + str(score),True,yellow)
    dis.blit(value,[0,])

def our_snake(snake_block,snake_list):
    for x in snake_list:
        pygame.draw.rect(dis,balck,[x[0],x[1],snake_block,snake_block])

def message(msg,colour):
    mesg = font_style.render(msg,True,colour)
    dis.blit(mesg,[width / 6,height / 3])

game_over =False
game_close = False

x1 = width / 2
y1 = height / 2
x1_change = 0
y1_change = 0
snake_list = []
snake_length = 1
foodx = round(random.randrange(0,width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0,height - snake_block) / 10.0) * 10.0

while game_close == True:
    dis.fill(blue)
    message("Oope!Your snake died! Press P to play again or Q to quit", red)
    Your_score(snake_length -1)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                game_over = True
                game_close = False
            if event.key == pygame.K_p:
                gameLoop()

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        game_over = True
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT or event.key == pygame.K_a:
            x1_change = -snake_block
            y1_change = 0
        elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            x1_change = snake_block
            y1_change = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_w:
            y1_change = -snake_block
            x1_change = 0
        elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
            y1_change = snake_block
            x1_change = 0

if x1 >= width or x1 < 0 or y1 >=height or y1 < 0:
    game_close = True
x1 += x1_change
y1 += y1_change
dis.fill(blue)
pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])

snake_Head = []
snake_Head.append(x1)
snake_Head.append(y1)
snake_List.append(snake_Head)
if len(snake_List) > snake_length:
    del snake_list[0]

for x in snake_list[:-1]:
    if x == snake_Head:
        game_close = True

our_snake(snake_block,snake_list)
Your_score(snake_length - 1)

pygame.display.update()

if x1 == foodx and y1 == foody:
    foodx = round(random.randrange(0,width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0,height - snake_block) / 10.0) * 10.0
    snake_length += 1
clock.tick(snake_speed)

pygame.quit()
quit()
gameLoop()