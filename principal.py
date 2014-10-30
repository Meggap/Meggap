import pygame

import constantes
from nivel1 import Level_01
from nivel2 import Level_02 

from jugador import Player

def main():
    """ Programa principal """
    pygame.init()
    
    # Set the height and width of the screen
    size = [constantes.ANCHO_PANTALLA, constantes.LARGO_PANTALLA]
    screen = pygame.display.set_mode(size)
    letraParaMarcador = pygame.font.Font(None,36)
    pygame.display.set_caption("Meggap")

    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(Level_01(player))
    #level_list.append(Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.nivel = current_level

    player.rect.x = 340
    player.rect.y = constantes.LARGO_PANTALLA - player.rect.height
    active_sprite_list.add(player)
    
    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.go_left()
                if event.key == pygame.K_RIGHT:
                    player.go_right()
                if event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and player.mover_x < 0:
                    player.stop()
                if event.key == pygame.K_RIGHT and player.mover_x > 0:
                    player.stop()
            
        # Update the jugador.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()

        # If the jugador gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the jugador gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)

        # If the jugador gets to the end of the level, go to the next level
        current_position = player.rect.x + current_level.world_shift
        print current_position
        if current_position < current_level.level_limit:
            player.rect.x = 120
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.nivel = current_level

        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        text = letraParaMarcador.render("Puntos: "+str(player.puntaje), 1 , constantes.ROJO)
        screen.blit(text, (650,0))

        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()

if __name__ == "__main__":
    main()
