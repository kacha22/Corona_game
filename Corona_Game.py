import random
import pygame

pygame.init()

gray = (132,136,112)
yellow = (255,255,102)
green = (0,255,0)
red = (255,0,0)
sand = (142,118,93)

dis_width = 600
dis_height = 400

display = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Corona Game")

clock = pygame.time.Clock()

snake_block = 15
snake_speed = 15

press_initie = pygame.font.SysFont("bahnschrift", 20)
font_style = pygame.font.SysFont("bahnschrift", 20)
score_font = pygame.font.SysFont("comicsansms", 15)
score_final = pygame.font.SysFont("bahnschrift", 25)


virus_image = pygame.image.load('Virus4.png')
virus_image = pygame.transform.scale(virus_image, (12,12))

def our_snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(display, green, pygame.Rect(x[0], x[1], 10, 10))

def inicio(msg, color):
    mesg = press_initie.render(msg, True, color)
    display.blit(mesg, [dis_width / 10, dis_height / 3])

def menssage(msg,color):
    mesg = font_style.render(msg, True, color)
    display.blit(mesg, [dis_width/10, dis_height/3])

def pont_final(final, color):
    pont = score_final.render(final, True, color)
    display.blit(pont, [dis_width / 4, dis_height / 2])

def your_score(score):
    value = score_font.render("Pontuação: " + str(score), True, yellow)
    display.blit(value, [0,0])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            display.fill(gray)
            menssage("Você perdeu! Pressione Q para sair ou C para continuar", red)
            pont_final("Você eliminou " + str(length_of_snake -1) + "% do vírus", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    elif event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit()
                if event.key == pygame.K_LEFT:
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -10
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = 10

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        display.fill(sand)

        display.blit(virus_image,[foodx,foody,snake_block,snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_list)
        your_score(length_of_snake -1)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()
gameLoop()