import pygame

pygame.init() # 초기화(반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width,screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Jooyi Game") # 게임 이름

# FPS (초당 프레임 수)
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/TA9/Documents/python/basic2_pygame/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:/Users/TA9/Documents/python/basic2_pygame/character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width =  character_size[0] # 캐릭터의 가로 크기
character_height = character_size[1] # 캐릭터의 세로 크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로 위치)
character_y_pos = screen_height - character_height # 화면 세로크기 가장 아래에 해당하는 곳에 위치 (세로 위치)

# 캐릭터가 이동할 좌표
to_x = 0
to_y = 0

# 이동 속도
character_speed = 0.6

# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(30) # 게임화면의 초당 프레임 수를 설정
    
    # print("fps : " + str(clock.get_fps())) # 현재 프레임 수 출력

    # 캐릭터가 1초 동안에 100 만큼 이동 해야함
    # 10 fps : 1초 동안에 10번 동작 -> 1번에 10만큼 이동해야함! 10 * 10 = 100
    # 20 fps : 1초 동안에 20번 동작 -> 1번에 5만큼 이동해야함! 5 * 20 = 100
    # => 기본 속도를 작게 지정한 경우, 프레임수를 낮추게 되면 버벅이면서 속도가 느려지게 된다!
    # => 프레임 수 달라진다고 속도가 달라지게되면 안됨! 보정해줘야함 
    # => dt(게임화면의 초당 프레임 수)를 곱해서 보정하여 어떤 프레임이어도 속도는 일정하게 유지시킨다! (character_x_pos += to_x * dt)

    for event in pygame.event.get(): # 어떤 이벤트가 발생하였는가? 마우스, 키보드 동작 이벤트가 있을 경우
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False # 게임이 진행중이 아님

        if event.type == pygame.KEYDOWN: # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: # 캐릭터를 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT: # 캐릭터를 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP: # 캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: # 캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0
            
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경곗값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    # 세로 경곗값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height
    
    
    # blit으로 이미지를 그리게 되면 왼쪽위 좌표 기준으로 이미지가 채워지기 때문에 좌표를 잘 지정해야함!
    screen.blit(background, (0, 0)) # 배경 그리기

    screen.blit(character, (character_x_pos, character_y_pos)) # 캐릭터 그리기

    pygame.display.update() # 게임화면 다시 그리기

# pygame 종료
pygame.quit()