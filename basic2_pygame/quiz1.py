'''
Quiz) 하늘에서 떨어지는 똥 피하기 게임

[게임 조건]
1. 캐릭터는 화면 가장 아래에 위치, 좌우로만 이동 가능
2. 똥은 화면 가장 위에서 떨어짐. x 좌표는 매번 랜덤으로 설정
3. 캐릭터가 똥을 피하면 다음 똥이 다시 떨어짐
4. 캐릭터가 똥과 충돌하면 게임 종료
5. FPS 는 30 으로 고정

[게임 이미지]
1. 배경 480 * 640
2. 캐릭터 70 * 70
3. 똥 70 * 70
'''

import pygame
import random
######################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init()

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("똥 피하기 게임")

# FPS (초당 프레임 수)
clock = pygame.time.Clock()
######################################################################


# 1. 사용자 게임 초기화 (배경화면, 게임 이미지, 좌표, 속도, 폰트, 게임 시간 등)

# 배경
background = pygame.image.load("C:/Users/TA9/Documents/python/basic2_pygame/background.png")

# 캐릭터
character = pygame.image.load("C:/Users/TA9/Documents/python/basic2_pygame/character.png")
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) / 2
character_y_pos = screen_height - character_height

to_x = 0

character_speed = 0.6

# 똥
enemy = pygame.image.load("C:/Users/TA9/Documents/python/basic2_pygame/enemy.png")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = random.randint(0, screen_width - enemy_width + 1)
enemy_y_pos = 0

enemy_speed = 0.3

# 폰트
game_font = pygame.font.Font(None, 40)

start_ticks = pygame.time.get_ticks()

running = True
while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    # 3-1. 사용자 캐릭터
    character_x_pos += to_x * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 3-2. 똥 움직임
    enemy_y_pos += enemy_speed * dt

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width + 1)

    # 4. 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    if character_rect.colliderect(enemy_rect):
        print("충돌!")
        running = False

    # 5. 화면에 그리기
    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    

    pygame.display.update()

pygame.quit()