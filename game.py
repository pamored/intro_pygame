import pygame

pygame.init()

screen = pygame.display.set_mode( (800, 600) ) #definimos una tupla, para el alto y ancho de la pantalla de juego

#he cargado mi sprite en memoria
spr_ball = pygame.image.load("assets/soccer.png")
spr_ball = pygame.transform.scale(spr_ball,(64,64))
rect_ball = spr_ball.get_rect()

black = (0, 0, 0)
velocidad = [2,2]

terminado = False
#Game Loop
while not terminado:
    # gestionar los eventos del usuario
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminado = True
            break
        elif event.type == pygame.KEYDOWN:  #se tiene q presionar una tecla, luego vemos cual  
            if event.key == pygame.K_RIGHT:
                rect_ball = rect_ball.move([5,0])
            elif event.key == pygame.K_LEFT:
                rect_ball = rect_ball.move([-5,0])
            elif event.key == pygame.K_UP:
                rect_ball = rect_ball.move([0,-5])
            elif event.key == pygame.K_DOWN:
                rect_ball = rect_ball.move([0,5])

    # actualizar los estados del juego
    #Rebote de pelota
    #rect_ball = rect_ball.move(velocidad)
    #if rect_ball.y > 536:
    #    velocidad[1] = -1
    #if rect_ball.y <= 0:
    #    velocidad[1] = 2

    #if rect_ball.x > 736:
    #    velocidad[0] = -2
    #if rect_ball.x <= 0:
    #    velocidad[0] = -velocidad[0]

    print(rect_ball)

    # renderizar la interfaz grafica, (pinta cosas en la pantalla)
    screen.fill(black)
    screen.blit(spr_ball, rect_ball)
    pygame.display.flip()