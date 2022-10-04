from math import fabs
from turtle import back
import pygame

pygame.init() # 초기화 *반드시*

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

#화면 타이틀
pygame.display.set_caption("Demo1")

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

#이벤트 루프
running = True #게임이 진행중인가

while running:
    for event in pygame.event.get(): #동작이 들어오는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가
            running = False #게임 진행 멈춤

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT: #캐릭터를 왼쪽으로
                to_x -= 0.1 #to_x = to_x - 0.1
            elif event.key == pygame.K_RIGHT: #캐릭터를 오른쪽으로
                to_x += 0.1 
            elif event.key == pygame.K_UP: #캐릭터를 위로
                to_y -= 0.1
            elif event.key == pygame.K_DOWN: #캐릭터를 아래로
                to_y += 0.1

        if event.type == pygame.KEYUP: #방향키 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x
    character_y_pos += to_y

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

    screen.fill((67, 161, 73)) #배경 rgb값

    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()#화면 다시 나타내기

# 종료
pygame.quit()
