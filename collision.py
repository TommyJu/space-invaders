import pygame, sys
from alien import shift_aliens_down
from constants import screen_size
from audio_manager import AudioManager
from events import GAME_OVER_EVENT

# Wrapper function for all collision checks with side effects and no return values
def handle_side_effect_collisions(player, obstacle_blocks, alien_manager, score):
        alien_laser_collision_checks(alien_manager.alien_lasers, player, obstacle_blocks)
        player_laser_collision_checks(player, alien_manager.aliens, alien_manager.extra_alien, obstacle_blocks, score)

def alien_screen_collision(aliens, aliens_x_direction):
    for alien in aliens:
        # Horizontal collision with screen
        if alien.rect.left <= 0 or alien.rect.right >= screen_size.SCREEN_WIDTH:
            shift_aliens_down(aliens)
            return aliens_x_direction * -1
    return aliens_x_direction

# Checks collisions for the player's laser
def player_laser_collision_checks(player, aliens, extra_alien, obstacle_blocks, score):
    if player.sprite.lasers:
        for laser in player.sprite.lasers:
            
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            
            # Alien collision
            if pygame.sprite.spritecollide(laser, aliens, dokill = True):
                laser.kill()
                score.increment_score()
                # Alien kill sound effect
                AudioManager.play_alien_hit_sound()
            
            # Extra alien collision
            if pygame.sprite.spritecollide(laser, extra_alien, dokill = True):
                laser.kill()
                score.increment_score()
                AudioManager.play_extra_alien_hit_sound()
    

# Checks the collisions for the alien lasers
def alien_laser_collision_checks(alien_lasers, player, obstacle_blocks):
    if alien_lasers:
        for laser in alien_lasers:
            
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            
            # Player collision
            if pygame.sprite.spritecollide(laser, player, dokill = False):
                laser.kill()
                player.sprite.damage()