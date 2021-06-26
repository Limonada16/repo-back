import sys
import pygame

pygame.init()

#CONFIGURACIÓN DE PANTALLA DEL JUEGO
size = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Juego")

#CARGAR IMAGENES
ball = pygame.image.load("pelota.png")
ballreact = ball.get_rect()
barra = pygame.image.load("barra.png")
barreact = ball.get_rect()
#MOVIMIENTO
speed = [1,1]

#CONTROL DEL CICLE
run = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #DETECCION DE TECLAS
    keys = pygame.key.get_pressed()
    if keys[pygame.K_DOWN]:
        barreact = barreact.move(0, 1)
    if keys[pygame.K_UP]:
        barreact = barreact.move(0, -1)
    #MOVER PELOTA        
    ballreact = ballreact.move(speed)
    #DETECTAR COLISIÓN
    if ballreact.top < 0 or ballreact.bottom > 600:
        speed[1] = -speed[1]
    if ballreact.left < 0 or ballreact.right > 800:
        speed[0] = -speed[0]
    if(barreact.colliderect(ballreact)):
        speed[0] = -speed[0]
    #MOSTRAR IMAGENES    
    screen.blit(ball, ballreact)
    screen.blit(barra, barreact)
    pygame.display.flip()
pygame.quit()