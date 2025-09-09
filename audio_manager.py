import pygame
from constants import sound_settings

# A utility class for playing the game's audio
class AudioManager:
    BACKGROUND_VOLUME = 0.1
    LASER_VOLUME = 0.2
    ALIEN_HIT_VOLUME = 0.2
    
    def play_background_music():
        music = pygame.mixer.Sound("./assets/audio/music.wav")
        music.set_volume(AudioManager.BACKGROUND_VOLUME)
        music.play(loops = -1)

    def play_laser_sound():
        music = pygame.mixer.Sound("./assets/audio/laser.wav")
        music.set_volume(AudioManager.LASER_VOLUME)
        music.play()

    def play_extra_alien_hit_sound():
        music = pygame.mixer.Sound("./assets/audio/extra_alien_hit.wav")
        music.set_volume(AudioManager.ALIEN_HIT_VOLUME)
        music.play()

    def play_alien_hit_sound():
        music = pygame.mixer.Sound("./assets/audio/explosion.wav")
        music.set_volume(AudioManager.ALIEN_HIT_VOLUME)
        music.play()