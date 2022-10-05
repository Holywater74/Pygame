from calendar import c
from math import fabs
from pickletools import pyunicode
from tkinter import E
from turtle import back
import pygame

pygame.init() # 초기화 *반드시*

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

#화면 타이틀
pygame.display.set_caption("Demo1")

#FPS
clock = pygame.time.Clock()

#배경 불러오기
#background = pygame.image.load("C:\\Users\\min79\\Desktop\\code\\python\\background.png")

#스프라이트 불러오기
character = pygame.image.load("C:\\Users\\min79\\Desktop\\code\\python\\character.png")\

character_size = character.get_rect().size #이미지의 크기를 구해옴
character_width = character_size[0] #캐릭터 가로
character_height = character_size[1] # 캐릭터 세로
character_x_pos = (screen_width / 2) - (character_width / 2) #화면 가로 가운데
character_y_pos = screen_height - character_height #화면 세로

#이동할 좌표
to_x = 0
to_y = 0

#캐릭터 속도
character_speed = 0.3

#적 캐릭터
enemy = pygame.image.load("C:\\Users\\min79\\Desktop\\code\\python\\enemy.png")\

enemy_size = enemy.get_rect().size #이미지의 크기를 구해옴
enemy_width = enemy_size[0] #캐릭터 가로
enemy_height = enemy_size[1] # 캐릭터 세로
enemy_x_pos = (screen_width / 2) - (enemy_width / 2) #화면 가로 가운데
enemy_y_pos = (screen_height / 2) - (enemy_height / 2) #화면 세로

#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트객체 생성 (폰트 , 크기)

#총 시간
total_time = 10

#시작 시간
start_ticks = pygame.time.get_ticks()



#이벤트 루프
running = True #게임이 진행중인가

while running:
    dt = clock.tick(60) #프레임 60

    for event in pygame.event.get(): #동작이 들어오는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가
            running = False #게임 진행 멈춤

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= character_speed #to_x = to_x - 0.1
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += character_speed 
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y += character_speed

        if event.type == pygame.KEYUP: #방향키 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #가로 경계
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width
    
    #세로 경계
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    #충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    #충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌")
        running = False

    screen.fill((67, 161, 73)) #배경 rgb값

    screen.blit(character, (character_x_pos, character_y_pos))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))#적 그리기

    #타이머
    #경과시간
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 #경과시간 1000나누기 = 초단위표시

    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255, 255,255))
    #출력 할 글자, True 글자색상
    screen.blit(timer, (10, 10))

    #시간 되면 게임 종료
    if total_time - elapsed_time <= 0:
        print("시간종료")
        running = False

    pygame.display.update()#화면 다시 나타내기

#대기
pygame.time.delay(2000) #2초 대기

# 종료
pygame.quit()
