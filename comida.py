import pygame

from funciones_spritesheet import SpriteSheet, SpriteSheetNotas
import constantes

class Amarillo (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        
        self.image = sprite_sheet.get_image(0,0,39,50)
      
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

            
class Azul (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(40,0,39,50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

            
class Celeste (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(79,0,39,50)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

            
class Naranja (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(118,0,39,50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
        
class Rojo (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(157,0,39,50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
class Verde (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(196,0,39,50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        
class Violeta (pygame.sprite.Sprite):
        
    def __init__ (self,pos_x,pos_y): 
        pygame.sprite.Sprite.__init__(self)
        
        sprite_sheet = SpriteSheetNotas("imagenes/puntos/puntos_spritesheet.png")
        self.image = sprite_sheet.get_image(235,0,39,50)
        
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

