import pyxel
from config import BULLET_SPEED, SPRITES

class ProjectileManager:
    def __init__(self):
        self.tirs_liste = [[], [], [], []]

    def tirs_deplacement(self):
        for tirs in self.tirs_liste:
            for tir in tirs.copy():
                if tirs == self.tirs_liste[0]:
                    tir[1] -= BULLET_SPEED
                    if tir[1] < -8:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[1]:
                    tir[1] += BULLET_SPEED
                    if tir[1] > 128:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[2]:
                    tir[0] -= BULLET_SPEED
                    if tir[0] < -8:
                        tirs.remove(tir)
                elif tirs == self.tirs_liste[3]:
                    tir[0] += BULLET_SPEED
                    if tir[0] > 128:
                        tirs.remove(tir)

    def draw(self):
        for tirs in self.tirs_liste:
            for tir in tirs:
                if tirs == self.tirs_liste[0]:
                    sprite_x, sprite_y = SPRITES["tir"]["up"]
                elif tirs == self.tirs_liste[1]:
                    sprite_x, sprite_y = SPRITES["tir"]["down"]
                elif tirs == self.tirs_liste[2]:
                    sprite_x, sprite_y = SPRITES["tir"]["left"]
                elif tirs == self.tirs_liste[3]:
                    sprite_x, sprite_y = SPRITES["tir"]["right"]
                pyxel.blt(tir[0], tir[1], 0, sprite_x, sprite_y, 7, 7)