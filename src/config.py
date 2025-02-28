import pyxel
import sys

# Configurations globales
WINDOW_WIDTH = 128
WINDOW_HEIGHT = 128

# Difficulty settings
DIFFICULTY_SETTINGS = {
    "easy": {
        "ENEMY_BASE_SPEED": 0.3,
        "ENEMY_SPAWN_DELAY": 40,
        "WAVE_ENEMY_INCREMENT": 3,
        "INITIAL_PLAYER_HEALTH": 7,
        "MAX_PLAYER_HEALTH": 7,
        "PROBA_DROP_LIFE": 95,  # 5% chance
        "PROBA_DROP_MUN": 70    # 30% chance
    },
    "normal": {
        "ENEMY_BASE_SPEED": 0.4,
        "ENEMY_SPAWN_DELAY": 30,
        "WAVE_ENEMY_INCREMENT": 5,
        "INITIAL_PLAYER_HEALTH": 5,
        "MAX_PLAYER_HEALTH": 5,
        "PROBA_DROP_LIFE": 97,  # 3% chance
        "PROBA_DROP_MUN": 75    # 25% chance
    },
    "hard": {
        "ENEMY_BASE_SPEED": 0.5,
        "ENEMY_SPAWN_DELAY": 25,
        "WAVE_ENEMY_INCREMENT": 7,
        "INITIAL_PLAYER_HEALTH": 3,
        "MAX_PLAYER_HEALTH": 3,
        "PROBA_DROP_LIFE": 98,  # 2% chance
        "PROBA_DROP_MUN": 80    # 20% chance
    }
}

# Default settings (will be updated based on difficulty)
ENEMY_BASE_SPEED = DIFFICULTY_SETTINGS["normal"]["ENEMY_BASE_SPEED"]
ENEMY_SPAWN_DELAY = DIFFICULTY_SETTINGS["normal"]["ENEMY_SPAWN_DELAY"]
WAVE_ENEMY_INCREMENT = DIFFICULTY_SETTINGS["normal"]["WAVE_ENEMY_INCREMENT"]
INITIAL_PLAYER_HEALTH = DIFFICULTY_SETTINGS["normal"]["INITIAL_PLAYER_HEALTH"]
MAX_PLAYER_HEALTH = DIFFICULTY_SETTINGS["normal"]["MAX_PLAYER_HEALTH"]
PROBA_DROP_LIFE = DIFFICULTY_SETTINGS["normal"]["PROBA_DROP_LIFE"]
PROBA_DROP_MUN = DIFFICULTY_SETTINGS["normal"]["PROBA_DROP_MUN"]

PLAYER_SPEED_INCREMENT = 0.5

# Gameplay
larg_sprite = 8
longeur_sprite = 8
Temps_avant_pick = 150
BULLET_SPEED = 2
INITIAL_PLAYER_SPEED = 1
INITIAL_PLAYER_MUN = 60
MAX_PLAYER_MUN = 60
FIRE_RATE = 20
POWER_UP_SPAWN_TIME = 99999999

# Keyboard layout (will be set by menu)
QWERTY = False

#COMMANDES
def update_keyboard_layout(is_qwerty):
    global QWERTY, TIR_GAUCHE, TIR_HAUT
    QWERTY = is_qwerty
    TIR_GAUCHE = pyxel.KEY_A if QWERTY else pyxel.KEY_Q
    TIR_HAUT = pyxel.KEY_W if QWERTY else pyxel.KEY_Z

def update_difficulty(difficulty_level):
    global ENEMY_BASE_SPEED, ENEMY_SPAWN_DELAY, WAVE_ENEMY_INCREMENT
    global INITIAL_PLAYER_HEALTH, MAX_PLAYER_HEALTH, PROBA_DROP_LIFE, PROBA_DROP_MUN
    
    difficulty = ["easy", "normal", "hard"][difficulty_level]
    settings = DIFFICULTY_SETTINGS[difficulty]
    
    ENEMY_BASE_SPEED = settings["ENEMY_BASE_SPEED"]
    ENEMY_SPAWN_DELAY = settings["ENEMY_SPAWN_DELAY"]
    WAVE_ENEMY_INCREMENT = settings["WAVE_ENEMY_INCREMENT"]
    INITIAL_PLAYER_HEALTH = settings["INITIAL_PLAYER_HEALTH"]
    MAX_PLAYER_HEALTH = settings["MAX_PLAYER_HEALTH"]
    PROBA_DROP_LIFE = settings["PROBA_DROP_LIFE"]
    PROBA_DROP_MUN = settings["PROBA_DROP_MUN"]

# Initial keyboard setup
update_keyboard_layout(QWERTY)

##tirs
TIR_DROIT = pyxel.KEY_D
TIR_BAS = pyxel.KEY_S
##DEPLACEMENTS
DEPLACEMENT_GAUCHE = pyxel.KEY_LEFT
DEPLACEMENT_DROIT = pyxel.KEY_RIGHT
DEPLACEMENT_HAUT = pyxel.KEY_UP
DEPLACEMENT_BAS = pyxel.KEY_DOWN

#SPRITE
SPRITES = {
    "vaisseau": {"up": (17, 24), "down": (1, 24), "left": (17, 8), "right": (1, 8)},
    "tir": {"up": (48, 8), "down": (48, 8), "left": (48, 8), "right": (48, 8)},
    "ennemis": [(0, 120), (16, 120), (16, 136)],
    "life": (50, 202),
    "mun": (2, 202),
    "life_up": (50,185),
    "mun_up": (2,185),
    "fire_rate_up": (18,185),
    "speed_up": (34,185)
}