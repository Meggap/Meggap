"""
Esta modulo es utilizado para desarrollar el jugador.
"""
import pygame

import constantes
from puntos import Punto
from platforms import MovingPlatform
from funciones_spritesheet import SpriteSheet

class Player(pygame.sprite.Sprite):

    # -- Atributos
    mover_x = 0
    mover_y = 0
    
    # Estas listas definen todas las imagenes de nuestro jugador.
    jugador_frame_izq = []
    jugador_frame_der = []
    
    puntaje = 0
    # Direccion en la que va el jugador.
    direccion = "R"

    # Lista de sprite con las cosas que nos podemos chocar.
    nivel = None

    colision = None
    
    # -- Methods
    def __init__(self):
        """ Constructor function """

        pygame.sprite.Sprite.__init__(self)
        self.comidas = pygame.sprite.Group()
        sprite_sheet = SpriteSheet("imagenes/rastaspritesheet.png")
        # Carga de todos los sprite de la imagen hacia la derecha.
        image = sprite_sheet.get_image(0, 0, 36, 64)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(36, 0, 36, 64)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(72, 0, 36, 64)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(108, 0, 36, 64)
        self.jugador_frame_der.append(image)
        image = sprite_sheet.get_image(144, 0, 36, 64)
        self.jugador_frame_der.append(image)


        # # Carga de todos los sprite de la imagen hacia la derecha y la rotamos.
        
        image = sprite_sheet.get_image(0, 0, 36, 64)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(36, 0, 36, 64)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(72, 0, 36, 64)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(108, 0, 36, 64)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)
        image = sprite_sheet.get_image(144, 0, 36, 64)
        image = pygame.transform.flip(image, True, False)
        self.jugador_frame_izq.append(image)

        # Seteamos con que sprite comenzar
        self.image = self.jugador_frame_der[0]

        self.rect = self.image.get_rect()

        self.colision = pygame.mixer.Sound("sonido/sonidocolicion.ogg")

    def update(self):
        """ Metodo que mueve al jugador. """
        # Gravedad
        self.calc_grav()

        # Movimientos Izquierda/Derecha
        self.rect.x += self.mover_x
        pos = self.rect.x + self.nivel.world_shift
        if self.direccion == "R":
            frame = (pos // 30) % len(self.jugador_frame_der)
            self.image = self.jugador_frame_der[frame]
        else:
            frame = (pos // 30) % len(self.jugador_frame_izq)
            self.image = self.jugador_frame_izq[frame]

        # Verficiamos si colisionamos con algo
        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:
            if self.mover_x > 0:
                self.rect.right = block.rect.left
            elif self.mover_x < 0:
                self.rect.left = block.rect.right
          
            self.colision.play()
        
        self.rect.y += self.mover_y

        lista_de_bloques_colisionados = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        for block in lista_de_bloques_colisionados:

            if self.mover_y > 0:
                self.rect.bottom = block.rect.top
            elif self.mover_y < 0:
                self.rect.top = block.rect.bottom
            self.colision.play()

            self.mover_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.mover_x
             
        lista_de_comidas_a_comer = pygame.sprite.spritecollide(self, self.nivel.lista_de_comidas,False)
        for comidas_que_chocan in lista_de_comidas_a_comer:
            comidas_que_chocan.kill()
            self.puntaje = self.puntaje + 1

    def calc_grav(self):
        """ Calcula el efecto de la grabedad. """
        if self.mover_y == 0:
            self.mover_y = 1
        else:
            self.mover_y += .35

        # Verificamos si estamos en el suelo.
        if self.rect.y >= constantes.LARGO_PANTALLA - self.rect.height and self.mover_y >= 0:
            self.mover_y = 0
            self.rect.y = constantes.LARGO_PANTALLA - self.rect.height

    def jump(self):
        """ Metodo que se llamam si saltamos. """

        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.nivel.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constantes.LARGO_PANTALLA:
            self.mover_y = -10

    def go_left(self):
        """ Se llama cuando movemos hacia la izq. """
        self.mover_x = -6
        self.direccion = "L"

    def go_right(self):
        """ Se llama cuando movemos hacia la der. """
        self.mover_x = 6
        self.direccion = "R"

    def stop(self):
        """ Se llama cuando soltamos la tecla. """
        self.mover_x = 0

    
