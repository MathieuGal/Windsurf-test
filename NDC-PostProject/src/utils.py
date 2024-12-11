from game import *
from config import *
from random import *


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

def life_creation(self):
        for life in self.life_liste:
            if self.vaisseau_x < life[0] + 8 and self.vaisseau_x + 8 > life[0] and self.vaisseau_y < life[1] + 8 and self.vaisseau_y + 8 > life[1] :
                self.life_liste.remove(life)
                if self.vies < self.vies_max:
                    self.vies += 1

def mun_creation(self):
        for mun in self.mun_liste:
            if self.vaisseau_x < mun[0] + 8 and self.vaisseau_x + 8 > mun[0] and self.vaisseau_y < mun[1] + 8 and self.vaisseau_y + 8 > mun[1]:
                self.mun += 5
                if self.mun > self.mun_max:
                    self.mun = self.mun_max
                self.mun_liste.remove(mun)
                
def amelioration(self):
        if self.vagues % 5 == 0:
            self.ennemi_timer = 99999999
            for i in range(3):
                x = (i + 1) * 30
                up_type = random.randint(1, 4)
                if up_type == 1:
                    self.life_up.append([x, 60])
                elif up_type == 2:
                    self.speed_up.append([x, 60])
                elif up_type == 3:
                    self.mun_up.append([x, 60])
                elif up_type == 4:
                    self.fire_rate_up.append([x, 60])
                    
def power_up_collision(self):
        for up in self.life_up:
            if self.vaisseau_x < up[0] + 8 and self.vaisseau_x + 8 > up[0] and self.vaisseau_y < up[1] + 8 and self.vaisseau_y + 8 > up[1]:
                self.vies_max += 1
                self.ennemi_timer = 60
                self.life_up.clear()
                self.speed_up.clear()            
                self.fire_rate_up.clear()       
                self.mun_up.clear()

        for up in self.speed_up:
            if self.vaisseau_x < up[0] + 8 and self.vaisseau_x + 8 > up[0] and self.vaisseau_y < up[1] + 8 and self.vaisseau_y + 8 > up[1]:
                self.speed += 0.5
                self.ennemi_timer = 60
                self.speed_up.clear()
                self.fire_rate_up.clear()
                self.mun_up.clear()
                self.life_up.clear()

        for up in self.mun_up:
            if self.vaisseau_x < up[0] + 8 and self.vaisseau_x + 8 > up[0] and self.vaisseau_y < up[1] + 8 and self.vaisseau_y + 8 > up[1]:
                self.mun_max += 10
                self.ennemi_timer = 60
                self.mun_up.clear()
                self.speed_up.celar()
                self.fire_rate_up.clear()
                self.life_up.clear()

        for up in self.fire_rate_up:
            if self.vaisseau_x < up[0] + 8 and self.vaisseau_x + 8 > up[0] and self.vaisseau_y < up[1] + 8 and self.vaisseau_y + 8 > up[1]:
                self.t -= 2  # Decrease time between shots
                self.ennemi_timer = 60
                self.fire_rate_up.clear()
                self.speed_up.clear()
                self.mun_up.clear()
                self.life_up.clear()