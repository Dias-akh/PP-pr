import pygame
import json
from sys import exit
from random import randint , choice
from car import Enemy, Oil, Coin, Car, Obst, Bump, PowerUp

pygame.init()

width=500
height=700
screen=pygame.display.set_mode((width,height))
pygame.display.set_caption('Racer game')

image_object1=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object1=pygame.transform.scale(image_object1,(500,350))
image_object2=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object2=pygame.transform.scale(image_object2,(500,350))
image_object3=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/Road.png')
image_object3=pygame.transform.scale(image_object3,(500,350))

font_object=pygame.font.SysFont('Arial',20)

clock=pygame.time.Clock()


car_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/car1.png')
car_image = pygame.transform.scale(car_image, (100, 150))
car = Car(90, 500, car_image)

lines = [90, 160, 245, 325]
lines2 = [110,177,257,345]
lines3 = [90, 160]
coin_image=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/Practice10/Racer/images/coin.png')
coin_image=pygame.transform.scale(coin_image,(55,55))

coin2_image=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/coin2.png')
coin2_image=pygame.transform.scale(coin2_image,(55,55))

coin1 = Coin(lines2[0], -80, coin_image)
coin2=Coin(lines2[3],-80,coin2_image)

enemy_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/enemy.png')
enemy_image = pygame.transform.scale(enemy_image, (75, 90))
enemy = Enemy(choice(lines3), -150, enemy_image)
enemy_speed = 4

oil_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/oil.png')
oil_image = pygame.transform.scale(oil_image,(55,55))

obst_image= pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/obst.png')
obst_image= pygame.transform.scale(obst_image,(55,55))

bump_image=pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/bump.png')
bump_image= pygame.transform.scale(bump_image,(55,55))

nitro_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/nitro.png')
nitro_image = pygame.transform.scale(nitro_image, (55, 55))

shield_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/shield.png')
shield_image = pygame.transform.scale(shield_image, (55, 55))

repair_image = pygame.image.load('/Users/dias_akhmatgali/Desktop/PP-pr/TSIS3/assets/repair.png')
repair_image = pygame.transform.scale(repair_image, (55, 55))

oil=Oil(choice(lines2),-200,oil_image)
obst=Obst(choice(lines2),-300,obst_image)
bump=Bump(choice(lines2),-500,bump_image)
nitro = PowerUp(choice(lines2), -700, nitro_image, 'nitro')
shield = PowerUp(choice(lines2), -800, shield_image, 'shield')
repair = PowerUp(choice(lines2), -900, repair_image, 'repair')

road1_y = 0
road2_y = 350    
road3_y = -350   
road_speed = 3
slow_timer = 0
lane_index=1
coin_y=0
speed_coin=3
score=0
lives = 1  
active_powerup = None  
powerup_timer = 0      
shield_active = False
distance_traveled = 0
finish_distance = 5000

def get_username():
    user_name = ""
    entering = True
    while entering:
        screen.fill((50, 50, 50))
        prompt = font_object.render("Enter your name and press ENTER:", True, (255, 255, 255))
        name_text = font_object.render(user_name, True, (0, 255, 0))
        
        screen.blit(prompt, (width//2 - prompt.get_width()//2, 200))
        screen.blit(name_text, (width//2 - name_text.get_width()//2, 250))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and user_name != "":
                    entering = False
                elif event.key == pygame.K_BACKSPACE:
                    user_name = user_name[:-1]
                else:
                    if len(user_name) < 10: # Ограничим длину имени
                        user_name += event.unicode
        pygame.display.flip()
    return user_name
player_name = get_username()

def save_score(name, score, distance):
    file_path = 'leaderboard.json'
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append({
        "name": name,
        "score": score,
        "distance": int(distance)
    })
    # Сортируем по очкам (от большего к меньшему) и оставляем ТОП-10
    data = sorted(data, key=lambda x: x['score'], reverse=True)[:10]
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

def show_leaderboard():
    showing = True
    while showing:
        screen.fill((0, 0, 0))
        title = font_object.render("TOP 10 LEADERBOARD", True, (255, 215, 0))
        screen.blit(title, (width//2 - title.get_width()//2, 50))
        try:
            with open('leaderboard.json', 'r') as f:
                data = json.load(f)
        except:
            data = []
        for i, entry in enumerate(data):
            text = f"{i+1}. {entry['name']} - {entry['score']} pts ({entry['distance']}m)"
            row = font_object.render(text, True, (255, 255, 255))
            screen.blit(row, (width//2 - row.get_width()//2, 100 + i * 30))
        hint = font_object.render("Press SPACE to Exit", True, (150, 150, 150))
        screen.blit(hint, (width//2 - hint.get_width()//2, 500))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showing = False
        pygame.display.flip()
def load_settings():
    try:
        with open('settings.json', 'r') as f:
            return json.load(f)
    except:
        return {"sound": True, "car_color": "red", "difficulty": "Medium"}

def save_settings(settings):
    with open('settings.json', 'w') as f:
        json.dump(settings, f, indent=4)
settings = load_settings()

def draw_button(text, x, y, w, h, color, hover_color):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    current_color = hover_color if x < mouse[0] < x + w and y < mouse[1] < y + h else color
    pygame.draw.rect(screen, current_color, (x, y, w, h), border_radius=10)
    btn_text = font_object.render(text, True, (255, 255, 255))
    screen.blit(btn_text, (x + (w - btn_text.get_width()) // 2, y + (h - btn_text.get_height()) // 2))
    return x < mouse[0] < x + w and y < mouse[1] < y + h and click[0]

def show_menu():
    screen.fill((30, 30, 30))
    title = font_object.render("SUPER RACER 2026", True, (255, 215, 0))
    screen.blit(title, (width // 2 - title.get_width() // 2, 100))
    if draw_button("PLAY", 150, 200, 200, 50, (0, 150, 0), (0, 200, 0)): return 'game'
    if draw_button("LEADERBOARD", 150, 270, 200, 50, (0, 100, 200), (0, 150, 250)): return 'leaderboard'
    if draw_button("SETTINGS", 150, 340, 200, 50, (100, 100, 100), (150, 150, 150)): return 'settings'
    if draw_button("QUIT", 150, 410, 200, 50, (150, 0, 0), (200, 0, 0)): pygame.quit(); exit()
    return 'menu'

def show_settings():
    global settings
    screen.fill((40, 40, 40))
    diff_text = font_object.render(f"Difficulty: {settings['difficulty']}", True, (255, 255, 255))
    screen.blit(diff_text, (150, 150))
    if draw_button("Change", 300, 145, 100, 35, (80, 80, 80), (120, 120, 120)):
        diffs = ["Easy", "Medium", "Hard"]
        idx = (diffs.index(settings['difficulty']) + 1) % 3
        settings['difficulty'] = diffs[idx]
        pygame.time.delay(150) # Защита от дребезга клика
    if draw_button("BACK & SAVE", 150, 500, 200, 50, (50, 50, 50), (80, 80, 80)):
        save_settings(settings)
        return 'menu'
    return 'settings'
game_state = 'menu'

def reset_game():
    global score, lives, distance_traveled, active_powerup, road_speed, lane_index
    score = 0
    lives = 1
    distance_traveled = 0
    active_powerup = None
    road_speed = 3
    lane_index = 1
    car.rect.x = lines[lane_index]
    enemy.rect.y = -200
while True:
    # 1. Получаем события ОДИН РАЗ за итерацию
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 2. ЭКРАН МЕНЮ
    if game_state == 'menu':
        game_state = show_menu()
        if game_state == 'game': # Если нажали PLAY
            reset_game()

    # 3. ЭКРАН НАСТРОЕК
    elif game_state == 'settings':
        game_state = show_settings()

    # 4. ЭКРАН ТАБЛИЦЫ ЛИДЕРОВ
    elif game_state == 'leaderboard':
        show_leaderboard()
        game_state = 'menu'

    # 5. САМА ИГРА (Твой основной код теперь здесь)
    elif game_state == 'game':
        collision_happened = False
        
        # Управление машиной (перехватываем события из списка events)
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if lane_index > 0:
                        lane_index -= 1
                        car.rect.x = lines[lane_index]
                if event.key == pygame.K_RIGHT:
                    if lane_index < len(lines) - 1:
                        lane_index += 1
                        car.rect.x = lines[lane_index]

        # --- ТВОЯ ЛОГИКА ДВИЖЕНИЯ И ОТРИСОВКИ ---
        road1_y += road_speed
        road2_y += road_speed
        road3_y += road_speed  
        if road1_y >= 700: road1_y = -350
        if road2_y >= 700: road2_y = -350
        if road3_y >= 700: road3_y = -350
        
        screen.blit(image_object1,(0,road1_y))
        screen.blit(image_object2,(0,road2_y))
        screen.blit(image_object3, (0, road3_y))
        car.draw(screen)

        # Монеты
        for c in [coin1,coin2]:
            c.move(0,road_speed)
            if c.rect.y>=700:
                c.rect.x=choice(lines2); c.rect.y=-80
            if pygame.sprite.collide_rect(car, c):
                score += 20 if c == coin2 else 5
                c.rect.y = -80; c.rect.x = choice(lines2)
            c.draw(screen)
        
        # Масло
        oil.move(0, road_speed)
        if oil.rect.y >= 700:
            oil.rect.y = randint(-900, -700); oil.rect.x = choice(lines2)
        if pygame.sprite.collide_rect(car, oil):
            score = max(0, score - 15) 
            lane_index = (lane_index + 1) if lane_index == 0 else (lane_index - 1)
            car.rect.x = lines[lane_index]
            oil.rect.y = -300; oil.rect.x = choice(lines2)
        oil.draw(screen)

        # Препятствия и бонусы
        bump.move(0, road_speed)
        if bump.rect.y >= 700: bump.rect.y = -150; bump.rect.x = choice(lines2)
        if pygame.sprite.collide_rect(car, bump):
            slow_timer = 180; bump.rect.y = -300
        bump.draw(screen)

        for pu in [nitro, shield, repair]:
            pu.move(0, road_speed)
            if pu.rect.y >= 700: pu.rect.y = -200; pu.rect.x = choice(lines2)
            if pygame.sprite.collide_rect(car, pu):
                if pu.ptype == 'repair':
                    lives = min(3, lives + 1)
                elif active_powerup is None:
                    active_powerup = pu.ptype
                    powerup_timer = 300 if pu.ptype == 'nitro' else 600
                pu.rect.y = -1000
            pu.draw(screen)

        # Обработка скоростей
        if active_powerup == 'nitro' and slow_timer == 0:
            road_speed = 6
        elif slow_timer > 0:
            road_speed = 1; slow_timer -= 1
        else:
            road_speed = 3
        
        if active_powerup:
            powerup_timer -= 1
            if powerup_timer <= 0: active_powerup = None

        # Враги
        enemy.move(enemy_speed + road_speed)
        if enemy.rect.y >= 700:
            enemy.rect.x = choice(lines3); enemy.rect.y = randint(-300, -100)
        if pygame.sprite.collide_rect(car, enemy):
            if active_powerup == 'shield': active_powerup = None; enemy.rect.y = -200
            elif lives > 1: lives -= 1; enemy.rect.y = -200
            else: collision_happened = True
        enemy.draw(screen)

        # Текст на экране (HUD)
        dist_text = font_object.render(f"Distance: {int(distance_traveled)} / {finish_distance}m", True, (255, 255, 255))
        screen.blit(dist_text, (width - 250, 10))
        lives_text = font_object.render(f"Lives: {lives}", True, (0, 255, 0))
        screen.blit(lives_text, (10, 60))
        score_text = font_object.render(f"Score {score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Логика смерти
        if collision_happened:
            final_score = score + int(distance_traveled)
            save_score(player_name, final_score, distance_traveled)
            show_leaderboard() # Показываем топ после смерти
            game_state = 'menu' # Возвращаемся в меню

        enemy_speed = 4 + (score // 50)
        distance_traveled += road_speed * 0.1

    pygame.display.flip()
    clock.tick(60)