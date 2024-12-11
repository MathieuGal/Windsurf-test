import pyxel
from config import *
from random import *
from utils import *

class jeu:
    def __init__(self):
        pyxel.init(128, 128, title="Nuit du c0de")
        
        self.tir_velocity = 2
        self.vaisseau = [60, 60]
        self.vies = 5
        self.vies_max = 5
        self.mun = 60
        self.mun_max = 60
        self.speed = 1
        self.tirs_liste = [[], [], [], []]
        self.ennemis_liste = []
        self.vagues = 0
        self.spawner = 5
        self.ennemi_timer = 0
        self.enn_spawn = 0
        self.ennemi_sprite_index = 0
        self.ennemi_sprite_timer = 0
        self.ennemi_sprites = [(0, 120), (16, 120), (16, 136)]  # Liste des sprites des ennemis (x, y) sur la tilesheet
        self.timer = 0
        self.t = 20
        self.et = 30
        self.life_liste = []
        self.mun_liste = []
        
        self.life_up = []
        self.mun_up = []
        self.fire_rate_up = []
        self.speed_up = []
            
        self.vaisseau_sprites = {
            "up": (17, 24),
            "down": (1, 24), 
            "left": (17, 8), 
            "right": (1, 8)
        }
        self.tir_sprites = {
            "up": (48, 8),
            "down": (48, 8),
            "left": (48, 8),
            "right": (48, 8)
        }
            
        self.life_sprites = (50, 202)
        self.mun_sprites = (2, 202)
        self.life_up_sprite = (50,185)
        self.mun_up_sprite = (2,185)
        self.fire_rate_up_sprite = (18,185)
        self.speed_up_sprite = (34,185)
        
        self.current_direction = "up"
        
        pyxel.load("C:/Users/mathi/NDC-PostProject/asset/pyxres/my_assets.pyxres")

    def deplacement(self):
        if pyxel.btn(pyxel.KEY_RIGHT) and self.vaisseau[0] < 120:
            self.vaisseau[0] += self.speed
            self.current_direction = "right"
        if pyxel.btn(pyxel.KEY_LEFT) and self.vaisseau[0] > 0:
            self.vaisseau[0] -= self.speed
            self.current_direction = "left"
        if pyxel.btn(pyxel.KEY_DOWN) and self.vaisseau[1] < 120:
            self.vaisseau[1] += self.speed
            self.current_direction = "down"
        if pyxel.btn(pyxel.KEY_UP) and self.vaisseau[1] > 0:
            self.vaisseau[1] -= self.speed
            self.current_direction = "up"

    def tirs_creation(self):
        self.timer -= 1
        if self.timer <= 0 and self.mun > 0:
            if pyxel.btnr(pyxel.KEY_Z):
                self.tirs_liste[0].append([self.vaisseau[0] + 3, self.vaisseau[1] - 4])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_S):
                self.tirs_liste[1].append([self.vaisseau[0] + 3, self.vaisseau[1] + 8])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_Q):
                self.tirs_liste[2].append([self.vaisseau[0] - 4, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(pyxel.KEY_D):
                self.tirs_liste[3].append([self.vaisseau[0] + 8, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1

    def tirs_deplacement(self):
        for tirs in self.tirs_liste:
            for tir in tirs:
                if tirs == self.tirs_liste[0]:
                    tir[1] -= self.tir_velocity
                    if tir[1] < -8:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[1]:
                    tir[1] += self.tir_velocity
                    if tir[1] > 128:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[2]:
                    tir[0] -= self.tir_velocity
                    if tir[0] < -8:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[3]:
                    tir[0] += self.tir_velocity
                    if tir[0] > 128:
                        tirs.remove(tir)

    def ennemis_creation(self):
        x = randint(0,120)
        y = randint(0,120)
        if x == 120 or y == 120 or x == 0 or y == 0:
            self.ennemis_liste.append([x,y])
        else:
            self.ennemis_creation()

    def vagues_avances(self):
        if self.ennemi_timer > 0:
            self.ennemi_timer -= 1
        elif self.enn_spawn < self.spawner:
            self.ennemis_creation()
            self.enn_spawn += 1
            self.ennemi_timer = self.et
        if self.enn_spawn == self.spawner and self.ennemis_liste == []:
            self.vagues += 1
            self.spawner += 5
            self.enn_spawn = 0
            self.ennemi_timer = 150
            self.et -= 2
            self.amelioration()

    def ennemis_deplacement(self):
        for ennemi in self.ennemis_liste:
            if ennemi[0] < self.vaisseau[0]:
                ennemi[0] += 0.4
            elif ennemi[0] > self.vaisseau[0]:
                ennemi[0] -= 0.4
            if ennemi[1] < self.vaisseau[1]:
                ennemi[1] += 0.4
            elif ennemi[1] > self.vaisseau[1]:
                ennemi[1] -= 0.4

    def vaisseau_suppression(self):    
        for ennemi in self.ennemis_liste:
            if check_collision(self.vaisseau, ennemi):
                self.ennemis_liste.remove(ennemi)
                self.vies -= 1

    def ennemis_suppression(self):
        for idex in range(4):
            for ennemi in self.ennemis_liste:
                if idex == 0:
                    for tir in self.tirs_liste[0]:
                        if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1] and ennemi[1] <= tir[1] + 1:
                            self.ennemis_liste.remove(ennemi)
                            self.tirs_liste[0].remove(tir)
                            if randint(0, 100) >= 97:
                                self.life_liste.append([ennemi[0], ennemi[1]])
                            if randint(0, 100) >= 75:
                                self.mun_liste.append([ennemi[0], ennemi[1]])
                                    
                elif idex == 1:
                    for tir in self.tirs_liste[1]:
                        if ennemi[0] <= tir[0] + 1 and ennemi[0] + 8 >= tir[0] and ennemi[1] + 8 >= tir[1] and ennemi[1] <= tir[1] + 1:
                            self.ennemis_liste.remove(ennemi)
                            self.tirs_liste[1].remove(tir)
                            if randint(0, 100) >= 97:
                               self.life_liste.append([ennemi[0], ennemi[1]])
                            if randint(0, 100) >= 75:
                                self.mun_liste.append([ennemi[0], ennemi[1]])
                elif idex == 2:
                    for tir in self.tirs_liste[2]:
                        if ennemi[1] <= tir[1] + 1 and ennemi[1] + 8 >= tir[1] and ennemi[0] + 8 >= tir[0] and ennemi[0] <= tir[0] + 1:
                            self.ennemis_liste.remove(ennemi)
                            self.tirs_liste[2].remove(tir)
                            if randint(0, 100) >= 97:
                                self.life_liste.append([ennemi[0], ennemi[1]])
                            if randint(0, 100) >= 75:
                                self.mun_liste.append([ennemi[0], ennemi[1]])
                elif idex == 3:
                    for tir in self.tirs_liste[3]:
                        if ennemi[1] <= tir[1] + 1 and ennemi[1] + 8 >= tir[1] and ennemi[0] + 8 >= tir[0] and ennemi[0] <= tir[0] + 1:
                            self.ennemis_liste.remove(ennemi)
                            self.tirs_liste[3].remove(tir)
                            if randint(0, 100) >= 97:
                                self.life_liste.append([ennemi[0], ennemi[1]])
                            if randint(0, 100) >= 75:
                                self.mun_liste.append([ennemi[0], ennemi[1]])

    def power_up_collision(self):
        for up in self.life_up:
            if check_collision(self.vaisseau, up):
                self.vies_max += 1
                self.ennemi_timer = 60
                self.life_up.clear()
                self.speed_up.clear()            
                self.fire_rate_up.clear()       
                self.mun_up.clear()

        for up in self.speed_up:
            if check_collision(self.vaisseau, up):
                self.speed += 0.5
                self.ennemi_timer = 60
                self.speed_up.clear()
                self.fire_rate_up.clear()
                self.mun_up.clear()
                self.life_up.clear()

        for up in self.mun_up:
            if check_collision(self.vaisseau, up):
                self.mun_max += 10
                self.ennemi_timer = 60
                self.mun_up.clear()
                self.speed_up.celar()
                self.fire_rate_up.clear()
                self.life_up.clear()

        for up in self.fire_rate_up:
            if check_collision(self.vaisseau, up):
                self.t -= 2  # Decrease time between shots
                self.ennemi_timer = 60
                self.fire_rate_up.clear()
                self.speed_up.clear()
                self.mun_up.clear()
                self.life_up.clear()

    def life_creation(self):
        for life in self.life_liste:
            if check_collision(self.vaisseau, life):
                self.life_liste.remove(life)
                if self.vies < self.vies_max:
                    self.vies += 1
    
    def mun_creation(self):
        for mun in self.mun_liste:
            if check_collision(self.vaisseau, mun):
                self.mun += 5
                if self.mun > self.mun_max:
                    self.mun = self.mun_max
                self.mun_liste.remove(mun)

    def amelioration(self):
        if self.vagues % 5 == 0:
            self.ennemi_timer = 99999999
            for i in range(3):
                x = (i + 1) * 30
                up_type = randint(1, 4)
                if up_type == 1:
                    self.life_up.append([x, 60])
                elif up_type == 2:
                    self.speed_up.append([x, 60])
                elif up_type == 3:
                    self.mun_up.append([x, 60])
                elif up_type == 4:
                    self.fire_rate_up.append([x, 60])

    def update(self):
        self.deplacement()
        self.tirs_creation()
        self.tirs_deplacement()
        self.ennemis_deplacement()
        self.ennemis_suppression()
        self.vaisseau_suppression()
        self.vagues_avances()
        self.life_creation()
        self.mun_creation()
        self.power_up_collision()
            
        self.ennemi_sprite_timer += 1
        if self.ennemi_sprite_timer > 10:  # Change sprite toutes les 10 frames
            self.ennemi_sprite_index = (self.ennemi_sprite_index + 1) % len(self.ennemi_sprites)
            self.ennemi_sprite_timer = 0

    def draw(self):
        pyxel.cls(5)
        sprite_x, sprite_y = self.vaisseau_sprites[self.current_direction]
        pyxel.blt(self.vaisseau[0], self.vaisseau[1], 0, sprite_x, sprite_y, 15, 15, 5)
        
        if self.vies > 0:
            pyxel.text(5, 5, 'VIES:' + str(self.vies), 7)
            
            for tirs in self.tirs_liste:
                for tir in tirs:
                    if tirs == self.tirs_liste[0]:
                        sprite_x, sprite_y = self.tir_sprites["up"]
                    elif tirs == self.tirs_liste[1]:
                        sprite_x, sprite_y = self.tir_sprites["down"]
                    elif tirs == self.tirs_liste[2]:
                        sprite_x, sprite_y = self.tir_sprites["left"]
                    elif tirs == self.tirs_liste[3]:
                        sprite_x, sprite_y = self.tir_sprites["right"]
                    pyxel.blt(tir[0], tir[1], 0, sprite_x, sprite_y, 7, 7)
                
            for ennemi in self.ennemis_liste:
                sprite_x, sprite_y = self.ennemi_sprites[self.ennemi_sprite_index]
                pyxel.blt(ennemi[0], ennemi[1], 0, sprite_x, sprite_y, 15, 15, 5)
        else:
            pyxel.text(50, 64, 'GAME OVER', 7)
            
        pyxel.text(5, 110, 'VAGUES:' + str(self.vagues), 7)
        pyxel.text(50, 110, 'MUNITION:' + str(self.mun) + '/' + str(self.mun_max), 6)
            
        for up in self.life_up:
            pyxel.blt(up[0], up[1], 0, self.life_up_sprite[0], self.life_up_sprite[1], 11, 11, 5) 
        for up in self.speed_up:
            pyxel.blt(up[0], up[1], 0, self.speed_up_sprite[0], self.speed_up_sprite[1], 11, 11, 5) 
        for up in self.mun_up:
            pyxel.blt(up[0], up[1], 0, self.mun_up_sprite[0], self.mun_up_sprite[1], 11, 11, 5)  
        for up in self.fire_rate_up:
            pyxel.blt(up[0], up[1], 0, self.fire_rate_up_sprite[0], self.fire_rate_up_sprite[1], 11, 11, 5)  
                
        for life in self.life_liste:
            pyxel.blt(life[0], life[1], 0, self.life_sprites[0], self.life_sprites[1], 11, 11, 5)
                
        for mun in self.mun_liste:
            pyxel.blt(mun[0], mun[1], 0, self.mun_sprites[0], self.mun_sprites[1], 11, 11, 5)