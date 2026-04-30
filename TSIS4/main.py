import pygame
import json
import random
from sys import exit
from db import Database
from snake import Snake
from food import Food, PowerUp
from obstacles import Obstacles

STATE_MENU = "menu"
STATE_GAME = "game"
STATE_OVER = "game_over"
STATE_LEADERBOARD = "leaderboard"
STATE_SETTINGS = "settings"

class SnakeGame:
    def __init__(self):
        pygame.init()
        self.cell_size = 20
        self.grid_w, self.grid_h = 30, 20
        self.screen = pygame.display.set_mode((self.grid_w * self.cell_size, self.grid_h * self.cell_size))
        pygame.display.set_caption("Snake TSIS 4")
        self.font_main = pygame.font.SysFont("Arial", 24)
        self.font_title = pygame.font.SysFont("Arial", 40, bold=True)
        self.db = Database()
        self.state = STATE_MENU
        self.username = ""
        self.load_settings()
        self.reset_game()

    def load_settings(self):
        try:
            with open("settings.json", "r") as f: self.settings = json.load(f)
        except:
            self.settings = {"color": [0, 255, 0], "grid": True, "sound": True}
            self.save_settings()

    def save_settings(self):
        with open("settings.json", "w") as f: json.dump(self.settings, f)

    def reset_game(self):
        self.snake = Snake(self.cell_size, tuple(self.settings["color"]))
        self.food = Food(self.grid_w, self.grid_h, self.cell_size)
        self.powerup = PowerUp(self.grid_w, self.grid_h, self.cell_size)
        self.powerup.pos = (-1, -1)
        self.obstacles = Obstacles(self.cell_size)
        self.score, self.level, self.base_speed = 0, 1, 200
        self.shield = False
        self.active_powerup = None
        self.powerup_end = 0
        self.MOVE_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MOVE_EVENT, self.base_speed)

    def draw_button(self, text, x, y, w, h, color=(100, 100, 100)):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # Эффект наведения
        if x < mouse[0] < x + w and y < mouse[1] < y + h:
            pygame.draw.rect(self.screen, (150, 150, 150), (x, y, w, h))
            if click[0] == 1: return True
        else:
            pygame.draw.rect(self.screen, color, (x, y, w, h))
        
        txt_surf = self.font_main.render(text, True, (255, 255, 255))
        self.screen.blit(txt_surf, (x + (w - txt_surf.get_width()) // 2, y + (h - txt_surf.get_height()) // 2))
        return False

    def run(self):
        clock = pygame.time.Clock()
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT: exit()
                if self.state == STATE_MENU and event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE: self.username = self.username[:-1]
                    else: self.username += event.unicode

            self.screen.fill((0, 0, 0))
            
            if self.state == STATE_MENU: self.screen_menu()
            elif self.state == STATE_GAME: self.screen_game(events)
            elif self.state == STATE_OVER: self.screen_over()
            elif self.state == STATE_LEADERBOARD: self.screen_leaderboard()
            elif self.state == STATE_SETTINGS: self.screen_settings()

            pygame.display.flip()
            clock.tick(60)


    def screen_menu(self):
        title = self.font_title.render("SNAKE GAME", True, (0, 255, 0))
        self.screen.blit(title, (self.grid_w*10 - 100, 50))
        
        name_hint = self.font_main.render(f"Name: {self.username}", True, (255, 255, 255))
        self.screen.blit(name_hint, (200, 120))

        if self.draw_button("PLAY", 200, 180, 200, 40):
            if self.username:
                self.player_id = self.db.get_or_create_player(self.username)
                self.best_score = self.db.get_personal_best(self.player_id)
                self.reset_game()
                self.state = STATE_GAME
        
        if self.draw_button("LEADERBOARD", 200, 230, 200, 40): self.state = STATE_LEADERBOARD
        if self.draw_button("SETTINGS", 200, 280, 200, 40): self.state = STATE_SETTINGS
        if self.draw_button("QUIT", 200, 330, 200, 40): exit()

    def screen_game(self, events):
        now = pygame.time.get_ticks()
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = {pygame.K_UP: (0, -1), pygame.K_DOWN: (0, 1), pygame.K_LEFT: (-1, 0), pygame.K_RIGHT: (1, 0)}
                if event.key in keys: self.snake.change_direction(keys[event.key])
            if event.type == self.MOVE_EVENT:
                self.move_logic()

        if self.settings["grid"]: # Сетка
            for x in range(0, 600, 20): pygame.draw.line(self.screen, (30, 30, 30), (x, 0), (x, 400))
        
        self.snake.draw(self.screen)
        self.food.draw(self.screen)
        self.obstacles.draw(self.screen)
        if self.powerup.pos != (-1, -1): self.powerup.draw(self.screen)
        
        stats = self.font_main.render(f"Score: {self.score} | Lvl: {self.level} | Best: {self.best_score}", True, (255, 255, 255))
        self.screen.blit(stats, (10, 10))

    def move_logic(self):
        head = self.snake.body[0]
        new_pos = (head[0] + self.snake.direction[0], head[1] + self.snake.direction[1])

        if (new_pos[0] < 0 or new_pos[0] >= self.grid_w or new_pos[1] < 0 or new_pos[1] >= self.grid_h or 
            new_pos in self.snake.body or new_pos in self.obstacles.blocks):
            if self.shield: self.shield = False
            else: 
                self.db.save_session(self.player_id, self.score, self.level)
                self.state = STATE_OVER
            return

        if new_pos == self.food.pos:
            if self.food.is_poison:
                self.snake.shorten(2)
                if len(self.snake.body) <= 1: self.state = STATE_OVER
            else:
                self.snake.move(grow=True)
                self.score += self.food.weight
                if self.score // 10 + 1 > self.level:
                    self.level += 1
                    self.base_speed = max(50, self.base_speed - 20)
                    pygame.time.set_timer(self.MOVE_EVENT, self.base_speed)
                    self.obstacles.generate(self.level, self.snake.body, self.grid_w, self.grid_h)
            self.food.spawn(self.snake.body + self.obstacles.blocks)
        elif new_pos == self.powerup.pos:
            self.apply_powerup()
            self.powerup.pos = (-1, -1)
            self.snake.move()
        else: self.snake.move()

    def apply_powerup(self):
        self.powerup_end = pygame.time.get_ticks() + 5000
        if self.powerup.type == "speed": pygame.time.set_timer(self.MOVE_EVENT, 70)
        elif self.powerup.type == "slow": pygame.time.set_timer(self.MOVE_EVENT, 350)
        elif self.powerup.type == "shield": self.shield = True

    def screen_over(self):
        txt = self.font_title.render("GAME OVER", True, (255, 0, 0))
        self.screen.blit(txt, (200, 50))
        info = self.font_main.render(f"Score: {self.score} | Lvl: {self.level} | Best: {self.best_score}", True, (255, 255, 255))
        self.screen.blit(info, (180, 120))
        
        if self.draw_button("RETRY", 200, 200, 200, 40): 
            self.reset_game()
            self.state = STATE_GAME
        if self.draw_button("MAIN MENU", 200, 260, 200, 40): self.state = STATE_MENU

    def screen_leaderboard(self):
        self.screen.blit(self.font_title.render("LEADERBOARD", True, (255, 255, 0)), (180, 20))
        leaders = self.db.get_leaderboard()
        for i, r in enumerate(leaders):
            line = f"{i+1}. {r[0]} - {r[1]} pts (Lvl {r[2]})"
            self.screen.blit(self.font_main.render(line, True, (200, 200, 200)), (100, 80 + i*25))
        
        if self.draw_button("BACK", 200, 350, 200, 40): self.state = STATE_MENU

    def screen_settings(self):
        self.screen.blit(self.font_title.render("SETTINGS", True, (255, 255, 255)), (220, 20))
        

        grid_status = "ON" if self.settings["grid"] else "OFF"
        if self.draw_button(f"GRID: {grid_status}", 200, 100, 200, 40):
            self.settings["grid"] = not self.settings["grid"]
            pygame.time.delay(150)
            
        color_name = "GREEN" if self.settings["color"] == [0, 255, 0] else "BLUE"
        if self.draw_button(f"COLOR: {color_name}", 200, 160, 200, 40):
            self.settings["color"] = [0, 0, 255] if color_name == "GREEN" else [0, 255, 0]
            pygame.time.delay(150)

        if self.draw_button("SAVE & BACK", 200, 300, 200, 40):
            self.save_settings()
            self.state = STATE_MENU

if __name__ == "__main__":
    SnakeGame().run()