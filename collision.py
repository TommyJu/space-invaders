import pygame
from alien import shift_aliens_down
from constants import screen_size


def alien_screen_collision(aliens, aliens_x_direction):
    for alien in aliens:
        # Horizontal collision with screen
        if alien.rect.left <= 0 or alien.rect.right >= screen_size.SCREEN_WIDTH:
            shift_aliens_down(aliens)
            return aliens_x_direction * -1
    return aliens_x_direction


def player_laser_collision_checks(player, aliens, obstacle_blocks):
    if player.sprite.lasers:
        for laser in player.sprite.lasers:
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            # Alien collision
            if pygame.sprite.spritecollide(laser, aliens, dokill = True):
                laser.kill()
            # Extra alien collision
            if pygame.sprite.spritecollide(laser, aliens, dokill = True):
                laser.kill()
    

def alien_laser_collision_checks(alien_lasers, player, obstacle_blocks):
    if alien_lasers:
        for laser in alien_lasers:
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            # Player collision
            if pygame.sprite.spritecollide(laser, player, dokill = False):
                laser.kill()
                print("Player Hit")
                # TODO: Game over logic