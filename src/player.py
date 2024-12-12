import pyxel


from config import INITIAL_PLAYER_HEALTH, INITIAL_PLAYER_MUN, MAX_PLAYER_HEALTH, MAX_PLAYER_MUN, FIRE_RATE, SPRITES, TIR_GAUCHE, TIR_DROIT, TIR_HAUT, TIR_BAS, DEPLACEMENT_BAS, DEPLACEMENT_HAUT, DEPLACEMENT_GAUCHE, DEPLACEMENT_DROIT, INITIAL_PLAYER_SPEED

class Player:
    def __init__(self):
        self.vaisseau = [60, 60]
        self.vies = INITIAL_PLAYER_HEALTH
        self.vies_max = MAX_PLAYER_HEALTH
        self.mun = INITIAL_PLAYER_MUN
        self.mun_max = MAX_PLAYER_MUN
        self.speed = INITIAL_PLAYER_SPEED
        self.timer = 0
        self.t = FIRE_RATE
        self.current_direction = "up"
        

    def deplacement(self):
        keys = [DEPLACEMENT_HAUT, DEPLACEMENT_BAS, DEPLACEMENT_GAUCHE, DEPLACEMENT_DROIT]
        self.pressed_keys = [key for key in keys if pyxel.btn(key)]
        if pyxel.btn(DEPLACEMENT_DROIT) and self.vaisseau[0] < 120 and len(self.pressed_keys) == 1:
            self.vaisseau[0] += self.speed
            self.current_direction = "right"
        if pyxel.btn(DEPLACEMENT_GAUCHE) and self.vaisseau[0] > 0 and len(self.pressed_keys) == 1:
            self.vaisseau[0] -= self.speed
            self.current_direction = "left"
        if pyxel.btn(DEPLACEMENT_BAS) and self.vaisseau[1] < 120 and len(self.pressed_keys) == 1:
            self.vaisseau[1] += self.speed
            self.current_direction = "down"
        if pyxel.btn(DEPLACEMENT_HAUT) and self.vaisseau[1] > 0 and len(self.pressed_keys) == 1:
            self.vaisseau[1] -= self.speed
            self.current_direction = "up"
        else :
            if pyxel.btn(DEPLACEMENT_DROIT) and self.vaisseau[0] < 120 and len(self.pressed_keys) >= 2:
                self.vaisseau[0] += self.speed / 1.5
                self.current_direction = "right"
            if pyxel.btn(DEPLACEMENT_GAUCHE) and self.vaisseau[0] > 0 and len(self.pressed_keys) >= 2:
                self.vaisseau[0] -= self.speed / 1.5
                self.current_direction = "left"
            if pyxel.btn(DEPLACEMENT_BAS) and self.vaisseau[1] < 120 and len(self.pressed_keys) >= 2:
                self.vaisseau[1] += self.speed / 1.5
                self.current_direction = "down"
            if pyxel.btn(DEPLACEMENT_HAUT) and self.vaisseau[1] > 0 and len(self.pressed_keys) >= 2:
                self.vaisseau[1] -= self.speed / 1.5
                self.current_direction = "up"


    def tirs_creation(self, projectile_manager):
        self.timer -= 1
        if self.timer <= 0 and self.mun > 0:
            if pyxel.btnr(TIR_HAUT):
                projectile_manager.tirs_liste[0].append([self.vaisseau[0] + 3, self.vaisseau[1] - 4])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(TIR_BAS):
                projectile_manager.tirs_liste[1].append([self.vaisseau[0] + 3, self.vaisseau[1] + 8])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(TIR_GAUCHE):
                projectile_manager.tirs_liste[2].append([self.vaisseau[0] - 4, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1
            elif pyxel.btnr(TIR_DROIT):
                projectile_manager.tirs_liste[3].append([self.vaisseau[0] + 8, self.vaisseau[1] + 3])
                self.timer += self.t
                self.mun -= 1

    def draw(self):
        if self.vies > 0:
            sprite_x, sprite_y = SPRITES["vaisseau"][self.current_direction]
            pyxel.blt(self.vaisseau[0], self.vaisseau[1], 0, sprite_x, sprite_y, 15, 15, 5)