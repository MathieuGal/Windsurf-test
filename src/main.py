import pyxel
from config import WINDOW_HEIGHT, WINDOW_WIDTH, ENEMY_SPAWN_DELAY, INITIAL_PLAYER_HEALTH, \
MAX_PLAYER_HEALTH, INITIAL_PLAYER_MUN, MAX_PLAYER_MUN, INITIAL_PLAYER_SPEED, FIRE_RATE, WAVE_ENEMY_INCREMENT, \
update_keyboard_layout, update_difficulty
from player import Player
from enemies import EnemyManager
from projectiles import ProjectileManager
from powerups import PowerUpManager
from menu import MainMenu

class Game:
    def __init__(self):
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, title="Nuit du c0de")
        pyxel.load("../assets/pyxres/my_assets.pyxres")
        
        self.menu = MainMenu()
        self.game_started = False
        self.initialize_game()

    def initialize_game(self):
        self.player = Player()
        self.enemy_manager = EnemyManager()
        self.projectile_manager = ProjectileManager()
        self.powerup_manager = PowerUpManager()
        
        self.vagues = 0
        self.ennemi_timer = self.enemy_manager.ennemi_timer
        self.et = ENEMY_SPAWN_DELAY

    def update(self):
        if not self.game_started:
            self.menu.update()
            if self.menu.is_done:
                settings = self.menu.get_game_settings()
                update_difficulty(settings["difficulty"])
                update_keyboard_layout(settings["is_qwerty"])
                self.game_started = True
                self.initialize_game()  # Réinitialiser le jeu avec les nouveaux paramètres
            return

        if self.player.vies <= 0:
            if pyxel.btn(pyxel.KEY_SPACE):
                self.game_started = False
                self.menu = MainMenu()
                return
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
        
        if not self.game_started:
            self.menu.draw()
            return
            
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