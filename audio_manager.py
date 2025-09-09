import pygame

# A utility class for playing the game's audio
class AudioManager:
    BACKGROUND_VOLUME = 0.05
    LASER_VOLUME = 0.2
    HIT_VOLUME = 0.2
    SCREEN_OVERLAY_VOLUME = 0.2
    
    def play_background_music():
        music = pygame.mixer.Sound("./assets/audio/background_music.mp3")
        music.set_volume(AudioManager.BACKGROUND_VOLUME)
        music.play(loops = -1)

    def play_laser_sound():
        music = pygame.mixer.Sound("./assets/audio/laser.mp3")
        music.set_volume(AudioManager.LASER_VOLUME)
        music.play()

    def play_extra_alien_hit_sound():
        music = pygame.mixer.Sound("./assets/audio/extra_alien_hit.wav")
        music.set_volume(AudioManager.HIT_VOLUME)
        music.play()

    def play_alien_hit_sound():
        music = pygame.mixer.Sound("./assets/audio/alien_hit.mp3")
        music.set_volume(AudioManager.HIT_VOLUME)
        music.play()

    def play_player_damage_sound():
        music = pygame.mixer.Sound("./assets/audio/player_damage.mp3")
        music.set_volume(AudioManager.HIT_VOLUME)
        music.play()

    def play_game_over_sound():
        music = pygame.mixer.Sound("./assets/audio/game_over.mp3")
        music.set_volume(AudioManager.SCREEN_OVERLAY_VOLUME)
        music.play()

    def play_game_start_sound():
        music = pygame.mixer.Sound("./assets/audio/game_start.mp3")
        music.set_volume(AudioManager.SCREEN_OVERLAY_VOLUME)
        music.play()

    def play_wave_start_sound():
        music = pygame.mixer.Sound("./assets/audio/wave_start.mp3")
        music.set_volume(AudioManager.SCREEN_OVERLAY_VOLUME)
        music.play()
    
    def play_wave_complete_sound():
        music = pygame.mixer.Sound("./assets/audio/wave_complete.wav")
        music.set_volume(AudioManager.SCREEN_OVERLAY_VOLUME)
        music.play()
