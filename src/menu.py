import pyxel
from config import WINDOW_WIDTH, WINDOW_HEIGHT

class MainMenu:
    def __init__(self):
        self.selected_option = 0
        self.selected_difficulty = 1  # 0: Easy, 1: Normal, 2: Hard
        self.selected_keyboard = 0    # 0: AZERTY, 1: QWERTY
        self.state = "main"          # main, difficulty, keyboard
        self.is_done = False
        self.difficulty_names = ["FACILE", "NORMAL", "DIFFICILE"]
        self.keyboard_names = ["AZERTY", "QWERTY"]
        
    def update(self):
        if self.state == "main":
            if pyxel.btnp(pyxel.KEY_UP):
                self.selected_option = (self.selected_option - 1) % 2
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.selected_option = (self.selected_option + 1) % 2
            if pyxel.btnp(pyxel.KEY_RETURN):
                if self.selected_option == 0:
                    self.state = "difficulty"
                else:
                    self.state = "keyboard"
                    
        elif self.state == "difficulty":
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.selected_difficulty = (self.selected_difficulty - 1) % 3
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.selected_difficulty = (self.selected_difficulty + 1) % 3
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = "main"
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                self.state = "main"
                
        elif self.state == "keyboard":
            if pyxel.btnp(pyxel.KEY_LEFT) or pyxel.btnp(pyxel.KEY_RIGHT):
                self.selected_keyboard = 1 - self.selected_keyboard
            if pyxel.btnp(pyxel.KEY_RETURN):
                self.state = "main"
            if pyxel.btnp(pyxel.KEY_ESCAPE):
                self.state = "main"
                
        # Start game when space is pressed
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.is_done = True
            
    def draw(self):
        pyxel.cls(5)
        
        # Title
        pyxel.text(WINDOW_WIDTH//2 - 20, 20, "NUIT DU CODE", 7)
        
        if self.state == "main":
            # Main menu options
            color_diff = 7 if self.selected_option == 0 else 6
            color_keyb = 7 if self.selected_option == 1 else 6
            pyxel.text(WINDOW_WIDTH//2 - 25, 50, f"DIFFICULTE: {self.difficulty_names[self.selected_difficulty]}", color_diff)
            pyxel.text(WINDOW_WIDTH//2 - 25, 70, f"CLAVIER: {self.keyboard_names[self.selected_keyboard]}", color_keyb)
            
            # Instructions
            pyxel.text(10, WINDOW_HEIGHT - 30, "FLECHES: SELECTION", 6)
            pyxel.text(10, WINDOW_HEIGHT - 20, "ENTREE: MODIFIER", 6)
            pyxel.text(10, WINDOW_HEIGHT - 10, "ESPACE: JOUER", 6)
            
        elif self.state == "difficulty":
            pyxel.text(WINDOW_WIDTH//2 - 30, 40, "CHOISIR DIFFICULTE:", 7)
            for i, diff in enumerate(self.difficulty_names):
                color = 7 if i == self.selected_difficulty else 6
                pyxel.text(20 + i * 40, 60, diff, color)
                
        elif self.state == "keyboard":
            pyxel.text(WINDOW_WIDTH//2 - 30, 40, "CHOISIR CLAVIER:", 7)
            for i, kb in enumerate(self.keyboard_names):
                color = 7 if i == self.selected_keyboard else 6
                pyxel.text(30 + i * 40, 60, kb, color)
                
    def get_game_settings(self):
        return {
            "difficulty": self.selected_difficulty,  # 0: Easy, 1: Normal, 2: Hard
            "is_qwerty": self.selected_keyboard == 1
        }
