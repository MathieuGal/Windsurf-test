from random import randint
from config import *
from utils import check_collision
import pyxel

class EnemyManager:
    def __init__(self):
        self.ennemis_liste = []
        self.spawner = WAVE_ENEMY_INCREMENT
        self.enn_spawn = 0
        self.ennemi_timer = 0
        self.et = ENEMY_SPAWN_DELAY
        
        self.ennemi_sprite_index = 0
        self.ennemi_sprite_timer = 0
        self.ennemi_sprites = [(0, 120), (16, 120), (16, 136)]
        self.current_ennemi_sprite = self.ennemi_sprites[0]

    def ennemis_creation(self):
        x = randint(0, 120)
        y = randint(0, 120)
        if x == 120 or y == 120 or x == 0 or y == 0:
            self.ennemis_liste.append([x, y])
        else:
            self.ennemis_creation()

    def ennemis_deplacement(self, vaisseau):
        for ennemi in self.ennemis_liste:
            if ennemi[0] < vaisseau[0]:
                ennemi[0] += ENEMY_BASE_SPEED
            elif ennemi[0] > vaisseau[0]:
                ennemi[0] -= ENEMY_BASE_SPEED
            if ennemi[1] < vaisseau[1]:
                ennemi[1] += ENEMY_BASE_SPEED
            elif ennemi[1] > vaisseau[1]:
                ennemi[1] -= ENEMY_BASE_SPEED

    def vagues_avances(self, game):
        if self.ennemi_timer > 0:
            self.ennemi_timer -= 1
        elif self.enn_spawn < self.spawner:
            self.ennemis_creation()
            self.enn_spawn += 1
            self.ennemi_timer = self.et
        
        if self.enn_spawn == self.spawner and self.ennemis_liste == []:
            game.vagues += 1
            self.spawner += 5
            self.enn_spawn = 0
            self.ennemi_timer = 150
            self.et -= 2
            game.powerup_manager.amelioration(game)

    def vaisseau_suppression(self, player):    
        for ennemi in self.ennemis_liste:
            if check_collision(player.vaisseau, ennemi):
                self.ennemis_liste.remove(ennemi)
                player.vies -= 1

    def ennemis_suppression(self, projectile_manager, powerup_manager):
        for idex in range(4):
            for ennemi in self.ennemis_liste.copy():
                for tir in projectile_manager.tirs_liste[idex].copy():
                    if check_collision(tir, ennemi):
                        self.ennemis_liste.remove(ennemi)
                        projectile_manager.tirs_liste[idex].remove(tir)
                        
                        # Drop logic
                        if randint(0, 100) >= PROBA_DROP_LIFE:
                            powerup_manager.life_liste.append([ennemi[0], ennemi[1]])
                        if randint(0, 100) >= PROBA_DROP_MUN:    
                            powerup_manager.mun_liste.append([ennemi[0], ennemi[1]])
                        
                        break  # Prevent multiple hits

    def update_sprite_animation(self):
        self.ennemi_sprite_timer += 1
        if self.ennemi_sprite_timer > 10:
            self.ennemi_sprite_index = (self.ennemi_sprite_index + 1) % len(SPRITES["ennemis"])
            self.current_ennemi_sprite = SPRITES["ennemis"][self.ennemi_sprite_index]
            self.ennemi_sprite_timer = 0

    def draw(self):
        for ennemi in self.ennemis_liste:
            sprite_x, sprite_y = self.ennemi_sprites[self.ennemi_sprite_index]
            pyxel.blt(ennemi[0], ennemi[1], 0, sprite_x, sprite_y, 15, 15, 5)