if True:
    # -*- coding: utf-8 -*-
    import pygame
    import os, sys, re
    from collections import namedtuple

    Size = namedtuple('Size', ['width', 'height'])
    Pos = namedtuple('Pos', ['x', 'y'])
    
    class cosa(object):
        x=0;y=0
        incrx=0;incry=0
        pasox=0;pasoy=0
        imagen=None
        
    class clr(): pass
    _clr = {'bluish': (0, 128, 255), 'black': (0, 0, 0), 'redish': (255, 100, 0), 'white': (255, 255, 255)}
    clr.__dict__.update(_clr)


    def correctPosition():
        global incrx, incry
        tmpx = incrx * pasox + x
        tmpy = incry * pasoy + y
        if tmpx < 0 or tmpx + mrect.width > screct.width:
            tmpx = x; incrx = -incrx
        if tmpy < 0 or tmpy + mrect.height > screct.height:
            tmpy = y; incry = -incry
        return tmpx, tmpy


    if __name__ == '__main__':
        # 1)Hacer fondo y limites
        pygame.init()
        # Screen
        screct = Size(800, 500)
        screen = pygame.display.set_mode(screct, pygame.RESIZABLE)
        # Rectangle
        mrect = Size(111, 111)
        # surface = pygame.Surface(111)
        #os.chdir('/home/lmvalverde/Trabajo/Varios/Pablo/JUEGO1')
        os.chdir('C:\Users\CASA\Desktop\JUEGO1')
        fondo = pygame.image.load("campo.jpg").convert_alpha()
        bola = pygame.image.load("ball.gif").convert_alpha()
        comida = pygame.image.load("comida.jpg").convert_alpha()
        
        # Init
        done = False
        # is_blue = True
        x = 30; y = 30
        clock = pygame.time.Clock()
        incrx = 0; incry = 1; pasox = 3; pasoy = 3

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.VIDEORESIZE:
                    screct = Size(event.w, event.h)
                    screen = pygame.display.set_mode(screct, pygame.RESIZABLE)
                # if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    # is_blue = not is_blue
            keypress = False
            pressed = pygame.key.get_pressed()
            # if pressed[pygame.K_SPACE]: is_blue = not is_blue
            if pressed[pygame.K_UP]:    incrx = 0;  incry = -1; keypress = True
            if pressed[pygame.K_DOWN]:  incrx = 0;  incry = +1; keypress = True
            if pressed[pygame.K_LEFT]:  incrx = -1; incry = 0;  keypress = True
            if pressed[pygame.K_RIGHT]: incrx= +1;  incry = 0;  keypress = True
            if pressed[pygame.K_p]:        incrx = 0;  incry = 0;  keypress = True
            x, y = correctPosition()

            # _ = screen.fill(clr.white)

            # if is_blue: color = clr.bluish
            # else: color = clr.redish
            # _ = pygame.draw.rect(screen, color, pygame.Rect(x, y, 60, 60))
            _ = screen.blit(fondo, (0, 0))
            _ = screen.blit(bola, (x, y))
            _ = screen.blit(comida, (50,50))
            _ = screen.blit(comida, (50,500))
            _ = screen.blit(comida, (500,80))
            
            if keypress == True:
                print x,y
            _ = pygame.display.flip()
            _ = clock.tick(60)
            
        # 2)Disenar el objeto
        # 3)Hacer que se mueva
        # 4)Controlar las direcciones
        # 5)detectar que toca 
        # 6)si toca terminamos
        # 7)si no toca seguimos en "3"