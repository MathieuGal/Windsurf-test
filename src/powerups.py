import pyxel
from random import randint
from config import *
from utils import check_collision

class PowerUpManager:
    def __init__(self):
        self.life_up = []
        self.speed_up = []
        self.mun_up = []
        self.fire_rate_up = []
        self.life_liste = []
        self.mun_liste = []

    def amelioration(self, game, ennemis):
        """
        Génère des power-ups tous les 5 niveaux
        """
        if game.vagues % 5 == 0:
            ennemis.ennemi_timer = POWER_UP_SPAWN_TIME
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

    def power_up_collision(self, player, ennemis):
        """
        Gère les collisions avec les power-ups
        """
        power_up_actions = [
            (self.life_up, self.life_power_up, player),
            (self.speed_up, self.speed_power_up, player),
            (self.mun_up, self.mun_power_up, player),
            (self.fire_rate_up, self.fire_rate_power_up, player)
        ]
        
        if ennemis.ennemi_timer <= POWER_UP_SPAWN_TIME - Temps_avant_pick :
            for power_up_list, effect_method, player_obj in power_up_actions:
                for up in power_up_list.copy():
                    if check_collision(player_obj.vaisseau, up):
                        effect_method(player_obj)
                        self.clear_power_ups()
                        ennemis.ennemi_timer = 150
                        break

    def life_power_up(self, player):
        """Augmente la vie maximale du joueur"""
        player.vies_max += 1

    def speed_power_up(self, player):
        """Augmente la vitesse du joueur"""
        player.speed += PLAYER_SPEED_INCREMENT

    def mun_power_up(self, player):
        """Augmente la munition maximale du joueur"""
        player.mun_max += 10

    def fire_rate_power_up(self, player):
        """Réduit le temps entre les tirs"""
        player.t -= 2

    def clear_power_ups(self):
        """Efface tous les power-ups"""
        self.life_up.clear()
        self.speed_up.clear()
        self.mun_up.clear()
        self.fire_rate_up.clear()

    def life_creation(self, player):
        """Gère la collecte des points de vie"""
        for life in self.life_liste.copy():
            if check_collision(player.vaisseau, life):
                self.life_liste.remove(life)
                if player.vies < player.vies_max:
                    player.vies += 1

    def mun_creation(self, player):
        """Gère la collecte des munitions"""
        for mun in self.mun_liste.copy():
            if check_collision(player.vaisseau, mun):
                self.mun_liste.remove(mun)
                player.mun += 5
                if player.mun > player.mun_max:
                    player.mun = player.mun_max

    def draw(self):
        """Dessine les différents power-ups"""
        power_up_types = [
            (self.life_up, SPRITES["life_up"]),
            (self.speed_up, SPRITES["speed_up"]),
            (self.mun_up, SPRITES["mun_up"]),
            (self.fire_rate_up, SPRITES["fire_rate_up"]),
            (self.life_liste, SPRITES["life"]),
            (self.mun_liste, SPRITES["mun"])
        ]
        
        for power_up_list, sprite in power_up_types:
            for up in power_up_list:
                pyxel.blt(up[0], up[1], 0, sprite[0], sprite[1], 11, 11, 5)