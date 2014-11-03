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
        self.lista_de_comidas.add(Azul(2150,520))
        self.lista_de_comidas.add(Verde(2250,520))
        self.lista_de_comidas.add(Celeste(2620,520))
        self.lista_de_comidas.add(Naranja(2800,520))
        self.lista_de_comidas.add(Violeta(2620,380))
        self.lista_de_comidas.add(Amarillo(2800,380))
        self.lista_de_comidas.add(Rojo(3100,420))
        self.lista_de_comidas.add(Azul(3120,250))
        self.lista_de_comidas.add(Rojo(3550,70))
        self.lista_de_comidas.add(Verde(3500,70))
        self.lista_de_comidas.add(Naranja(3400,500))
        self.lista_de_comidas.add(Celeste(3600,500))
        self.lista_de_comidas.add(Amarillo(3800,500))
        self.lista_de_comidas.add(Rojo(4155,120))
        self.lista_de_comidas.add(Azul(4800,500))
        self.lista_de_comidas.add(Verde(4600,200))
        self.lista_de_comidas.add(Violeta(4900,50))
        self.lista_de_comidas.add(Amarillo(4950,50))
        self.lista_de_comidas.add(Rojo(5150,500))
        self.lista_de_comidas.add(Naranja(5000,500))
        self.lista_de_comidas.add(Rojo(5245,270))
        self.lista_de_comidas.add(Violeta(5600,380))
        self.lista_de_comidas.add(Verde(5500,520))
        self.lista_de_comidas.add(Celeste(5700,520))
        self.lista_de_comidas.add(Azul(6300,430))
        self.lista_de_comidas.add(Amarillo(6500,430))
        self.lista_de_comidas.add(Naranja(6500,430))


        #Artefactos
        autorojo = pygame.image.load("imagenes/auto3.PNG").convert()
        autorojo.set_colorkey(constantes.BLANCO)
        #autorojo = pygame.transform.rotate(autorojo,90)
        self.background.blit(autorojo, (1980, 500))

        # ubicacion de las plataformas.
        level = [ [platforms.PISO, 0, 580],
                  [platforms.PISO, 6000, 580],
                  [platforms.PISO, 12000, 580],
                  [platforms.LADRILLO1, 560, 427],
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
                  [platforms.LADRILLO2, 5200, 320],
                  [platforms.LADRILLO3, 5400, 460],
                  [platforms.LADRILLO3, 5530, 460],
                  [platforms.LADRILLO3, 5660, 460],
                  [platforms.LADRILLO1, 5900, 350],
                  [platforms.LADRILLO1, 5955, 305],
                  [platforms.LADRILLO1, 6010, 260],
                  [platforms.LADRILLO1, 6065, 215],
                  [platforms.LADRILLO3, 6130, 215],
                  [platforms.LADRILLO3, 6260, 215],
                  [platforms.LADRILLO3, 6390, 215],
                  [platforms.LADRILLO3, 6520, 215],
                  [platforms.LADRILLO1, 7350, 450],
                  [platforms.LADRILLO1, 7600, 400],
                  [platforms.LADRILLO2, 7850, 350],
                  [platforms.LADRILLO3, 8100, 300],
                  [platforms.LADRILLO3, 8500, 350],
                  [platforms.LADRILLO3, 8630, 350],
                  [platforms.LADRILLO3, 8760, 350],
                  [platforms.LADRILLO1, 9500, 450],
                  [platforms.LADRILLO2, 10000, 450],
                  [platforms.LADRILLO1, 10250, 350],
                  [platforms.LADRILLO3, 11000, 380],
                  [platforms.LADRILLO3, 11130, 380],
                  [platforms.LADRILLO3, 11260, 380],
                  [platforms.LADRILLO3, 11390, 240],
                  [platforms.LADRILLO3, 11520, 240],
                  [platforms.LADRILLO3, 11650, 240],
                  [platforms.LADRILLO3, 11780, 240],
                  [platforms.LADRILLO3, 11910, 240],
                  [platforms.LADRILLO3, 12050, 240]
                  ] 
        

        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)

        level = [ [platforms.PISO, 100, 0], 
                 [platforms.LADRILLO3, 1550, 444],
                 [platforms.LADRILLO3, 1550, 367],
                 [platforms.LADRILLO3, 1880, 367],
                 [platforms.LADRILLO3, 4300, 444],
                 [platforms.LADRILLO3, 4300, 380],
                 [platforms.LADRILLO3, 4300, 300],
                 [platforms.LADRILLO3, 6900, 444],
                 [platforms.LADRILLO3, 6900, 380],
                 [platforms.LADRILLO3, 8890, 444],
                 [platforms.LADRILLO3, 8890, 380],
                 [platforms.LADRILLO3, 11390, 270],
                 [platforms.LADRILLO3, 11000, 435]

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
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 4150
        block.rect.y = 180
        block.boundary_top = 180
        block.boundary_bottom = 490
        block.mover_y = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 4850
        block.rect.y = 100
        block.boundary_left = 4850
        block.boundary_right = 4950
        block.mover_x = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 4650
        block.rect.y = 150
        block.boundary_top = 150
        block.boundary_bottom = 490
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO1)
        block.rect.x = 6700
        block.rect.y = 180
        block.boundary_top = 180
        block.boundary_bottom = 455
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)

        block = platforms.MovingPlatform(platforms.LADRILLO2)
        block.rect.x = 8350
        block.rect.y = 120
        block.boundary_top = 120
        block.boundary_bottom = 400
        block.mover_y = -1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
        
        block = platforms.MovingPlatform(platforms.LADRILLO3)
        block.rect.x = 10400
        block.rect.y = 300
        block.boundary_left = 10400
        block.boundary_right = 10700
        block.mover_x = 1
        block.player = self.player
        block.nivel = self
        self.platform_list.add(block)
