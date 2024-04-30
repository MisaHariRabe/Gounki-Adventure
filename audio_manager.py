
import pygame
from pygame.mixer import *
from const import BGM_PATH, EFFECT_SOUND, PERSO_SOUND

pygame.init()
class AudioManager:
    def __init__(self, game):
        pygame.mixer.init()
        self.sfx_volume  = 0.6
        self.music_volume  = 0.3
        self.bgm_menu = f"{BGM_PATH}menu_01.mp3"
        self.bgm_game = f"{BGM_PATH}game_01.ogg"
        self.sound_effects = self.load_sound_effects()
        self.perso_effects = self.load_perso_effects()

        
        
    def load_sound_effects(self):
        
        sound_effects = {
            "forward_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}forward_effect.ogg"),
            "backward_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}backward_effect.ogg"),
            "close_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}close_effect.ogg"),
            "game_over_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}game_over_effect.mp3"),
            "level_start_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}level_start_effect.mp3"),
            "map_select_effect": pygame.mixer.Sound(f"{EFFECT_SOUND}map_select_effect.wav"),
        }

        for sound, effect in sound_effects.items():
            effect.set_volume(self.sfx_volume)
            sound_effects[sound] = effect
        return sound_effects

    def load_perso_effects(self):

        perso_effects = {
            "jump_effect": pygame.mixer.Sound(f"{PERSO_SOUND}jump_effect.wav"),
            "spear_throw_effect": pygame.mixer.Sound(f"{PERSO_SOUND}spear_throw_effect.wav"),
            "spear_hit_effect": pygame.mixer.Sound(f"{PERSO_SOUND}spear_hit_effect.wav"),
            "enemy_dying_effect": pygame.mixer.Sound(f"{PERSO_SOUND}enemy_dying_effect.wav"),
        }

        for sound, effect in perso_effects.items():
            effect.set_volume(self.sfx_volume)
            perso_effects[sound] = effect
        return perso_effects
    
    def play_sound(self, music):
        self.sound_effects[music].play()

    def play_player_sound(self, music):
        self.perso_effects[music].play()
        
    def load_bgm_menu(self):
        """charger la music de fond"""
        music.load(self.bgm_menu)
        pygame.mixer.music.set_volume(self.music_volume)
        music.play(loops=-1, fade_ms=1000)
        
    def load_bgm_game(self, level):
        """charger la music de fond"""
        music.load(level)
        pygame.mixer.music.set_volume(self.music_volume)
        music.play(loops=-1, fade_ms=1000)
        
        
    def play_bgm(self):
        """jouer le son en arriere plan"""
        music.play(loops=0, fade_ms=1000)

    def cut_music(self):
        if(pygame.mixer.music.load != None):
            pygame.mixer.music.stop()
            pygame.mixer.music.unload()
        
