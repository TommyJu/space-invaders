import pygame
from constants import screen_size
from audio_manager import AudioManager

# Wrapper function for all collision checks
def handle_collisions(player, obstacle_blocks, alien_manager, score):
        alien_screen_collision(alien_manager)
        alien_laser_collision_checks(alien_manager, player, obstacle_blocks)
        player_laser_collision_checks(player, alien_manager, obstacle_blocks, score)


def alien_screen_collision(alien_manager):
    for alien in alien_manager.aliens:
        # Horizontal collision with screen
        if alien.rect.left <= 0 or alien.rect.right >= screen_size.SCREEN_WIDTH:
            alien_manager.flip_aliens_x_direction()
            alien_manager.shift_aliens_down()
            return
            

# Checks collisions for the player's laser
def player_laser_collision_checks(player, alien_manager, obstacle_blocks, score):
    if player.sprite.lasers:
        for laser in player.sprite.lasers:
            
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            
            # Alien collision
            if pygame.sprite.spritecollide(laser, alien_manager.aliens, dokill = True):
                laser.kill()
                score.increment_score_alien_hit()
                # Alien kill sound effect
                AudioManager.play_alien_hit_sound()
            
            # Extra alien collision
            if pygame.sprite.spritecollide(laser, alien_manager.extra_alien, dokill = True):
                laser.kill()
                score.increment_score_extra_alien_hit()
                AudioManager.play_extra_alien_hit_sound()
    

# Checks the collisions for the alien lasers
def alien_laser_collision_checks(alien_manager, player, obstacle_blocks):
    if alien_manager.alien_lasers:
        for laser in alien_manager.alien_lasers:
            
            # Obstacle collision
            if pygame.sprite.spritecollide(laser, obstacle_blocks, dokill = True):
                laser.kill()
            
            # Player collision
            if pygame.sprite.spritecollide(laser, player, dokill = False):
                AudioManager.play_player_damage_sound()
                laser.kill()
                player.sprite.damage()