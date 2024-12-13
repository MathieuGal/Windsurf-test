import pyxel
from config import WINDOW_HEIGHT, WINDOW_WIDTH, ENEMY_SPAWN_DELAY, INITIAL_PLAYER_HEALTH, \
MAX_PLAYER_HEALTH, INITIAL_PLAYER_MUN, MAX_PLAYER_MUN, INITIAL_PLAYER_SPEED, FIRE_RATE, WAVE_ENEMY_INCREMENT
from player import Player
from enemies import EnemyManager
from projectiles import ProjectileManager
from powerups import PowerUpManager

class Game:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Nuit du c0de")
        
        pyxel.load("../assets/pyxres/my_assets.pyxres")
        
        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.projectile_manager = ProjectileManager()
        self.powerup_manager = PowerUpManager()
        
        self.vagues = 0
        self.ennemi_timer = self.enemy_manager.ennemi_timer
        self.et = ENEMY_SPAWN_DELAY

    def update(self):
        if self.player.vies <= 0:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.vaisseau = [60, 60]
                self.player.vies = INITIAL_PLAYER_HEALTH
                self.player.vies_max = MAX_PLAYER_HEALTH
                self.player.mun = INITIAL_PLAYER_MUN
                self.player.mun_max = MAX_PLAYER_MUN
                self.player.speed = INITIAL_PLAYER_SPEED
                self.player.timer = 0
                self.player.t = FIRE_RATE
                self.player.current_direction = "up"
                self.enemy_manager.ennemis_liste = []
                self.enemy_manager.spawner = WAVE_ENEMY_INCREMENT
                self.enemy_manager.enn_spawn = 0
                self.enemy_manager.ennemi_timer = 0
                self.enemy_manager.et = ENEMY_SPAWN_DELAY
                self.enemy_manager.ennemi_sprite_index = 0
                self.enemy_manager.ennemi_sprite_timer = 0
                self.enemy_manager.ennemi_sprites = [(0, 120), (16, 120), (16, 136)]
                self.powerup_manager.life_up = []
                self.powerup_manager.speed_up = []
                self.powerup_manager.mun_up = []
                self.powerup_manager.fire_rate_up = []
                self.powerup_manager.life_liste = []
                self.powerup_manager.mun_liste = []
            else:
                return
        # Player updates
        self.player.deplacement()
        self.player.tirs_creation(self.projectile_manager)
        
        # Projectile updates
        self.projectile_manager.tirs_deplacement()
        
        # Enemy updates
        self.enemy_manager.ennemis_deplacement(self.player.vaisseau)
        self.enemy_manager.vagues_avances(self)
        
        # Collision checks
        self.check_collisions()
        
        # Power-up updates
        self.powerup_manager.power_up_collision(self.player, self.enemy_manager)
        
        # Sprite animation
        self.update_sprites()

    def check_collisions(self):
        # Enemy-player collisions
        self.enemy_manager.vaisseau_suppression(self.player)
        
        # Enemy-projectile collisions
        self.enemy_manager.ennemis_suppression(
            self.projectile_manager, 
            self.powerup_manager
        )
        
        # Power-up and resource pickups
        self.powerup_manager.life_creation(self.player)
        self.powerup_manager.mun_creation(self.player)

    def update_sprites(self):
        # Update enemy sprite animation
        self.enemy_manager.update_sprite_animation()

    def draw(self):
        pyxel.cls(5)
        
        # Draw player
        self.player.draw()
        
        # Draw projectiles
        self.projectile_manager.draw()
        
        # Draw enemies
        self.enemy_manager.draw()
        
        # Draw UI
        self.draw_ui()
        
        # Draw power-ups
        self.powerup_manager.draw()

    def draw_ui(self):
        if self.player.vies > 0:
            pyxel.text(5, 5, f'VIES:{self.player.vies}', 7)
            pyxel.text(5, 110, f'VAGUES:{self.vagues}', 7)
            pyxel.text(50, 110, f'MUNITION:{self.player.mun}/{self.player.mun_max}', 6)
        else:
            pyxel.text(50, 64, 'GAME OVER', 7)
            pyxel.text(20, 100, 'Press space to restart', 7)

def main():
    game = Game()
    pyxel.run(game.update, game.draw)

if __name__ == "__main__":
    main()