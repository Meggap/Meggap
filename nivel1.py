'''
Created on 15/09/2014

@author: rodrigo
'''
import pygame
import constantes
import platforms
from levels import Level
from comida import Amarillo, Azul, Celeste, Naranja, Rojo, Verde, Violeta

# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """

    def __init__(self, player):
        """ Create level 1. """

        # Call the parent constructor
        Level.__init__(self, player)
        #Imagen de fondo
        self.background = pygame.image.load("imagenes/fondorasta.jpg").convert()
        
        #Establecemos el sonido de fondo
        #sonido=pygame.mixer.Sound("")
        #sonido.play()
        
        self.background.set_colorkey(constantes.BLANCO)
        self.level_limit = -15100
        
        #COMIDAS
        

        self.lista_de_comidas.add(Amarillo(1480,535))
        self.lista_de_comidas.add(Azul(800,280))
        self.lista_de_comidas.add(Celeste(1820,250))
        self.lista_de_comidas.add(Naranja(1580,430))
        self.lista_de_comidas.add(Rojo(1110,140))
        self.lista_de_comidas.add(Verde(1820,430))
        self.lista_de_comidas.add(Violeta(1420,535))
        self.lista_de_comidas.add(Rojo(2050,520))
        self.lista_de_comidas.add(Azul(2100,520))
        self.lista_de_comidas.add(Verde(2150,520))
        self.lista_de_comidas.add(Celeste(2620,520))
        self.lista_de_comidas.add(Naranja(2800,520))
        self.lista_de_comidas.add(Violeta(2620,420))
        self.lista_de_comidas.add(Amarillo(2800,420))
        self.lista_de_comidas.add(Rojo(3100,420))
        self.lista_de_comidas.add(Azul(3120,250))
        self.lista_de_comidas.add(Rojo(3550,70))
        self.lista_de_comidas.add(Verde(3500,70))


        #Artefactos
        autorojo = pygame.image.load("imagenes/auto3.PNG").convert()
        autorojo.set_colorkey(constantes.BLANCO)
        #autorojo = pygame.transform.rotate(autorojo,90)
        self.background.blit(autorojo, (1950, 500))

        # ubicacion de las plataformas.
        level = [ [platforms.LADRILLO1, 560, 427],
                  [platforms.LADRILLO2, 980, 247],
                  [platforms.LADRILLO3, 1200, 247],
                  [platforms.LADRILLO2, 1390, 297],
                  [platforms.LADRILLO3, 1620, 367],
                  [platforms.LADRILLO3, 1750, 367],
                  [platforms.LADRILLO3, 2500, 445],
                  [platforms.LADRILLO3, 2630, 445],
                  [platforms.LADRILLO3, 2760, 445],
                  [platforms.LADRILLO1, 3000, 367],
                  [platforms.LADRILLO1, 3200, 317],
                  [platforms.LADRILLO1, 3800, 317],
                  [platforms.PISO, 0, 580]

                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        level = [ [platforms.LADRILLO3, 1550, 444],
                 [platforms.LADRILLO3, 1550, 367],
                 [platforms.LADRILLO3, 1880, 367],
                 [platforms.PISO, 100, 0]

                  


                  ]

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.VerticalPlatform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

            #Add a custom moving platform
        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 690
        block.rect.y = 375
        block.boundary_left = 690
        block.boundary_right = 800
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO2)
        block.rect.x = 3300
        block.rect.y = 200
        block.boundary_left = 3300
        block.boundary_right = 3580
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)