import pyxel
from config import *

def __init__(self):
    pyxel.init(128, 128, title="Nuit du c0de")
    
    self.tir_velocity = 2
    self.vaisseau_x = 60
    self.vaisseau_y = 60
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
    
    pyxel.load("3.pyxres")
    pyxel.run(self.update, self.draw)