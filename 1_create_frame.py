from math import fabs
import pygame

pygame.init() # 초기화 *반드시*

#화면 크기
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height)) 

#화면 타이틀
pygame.display.set_caption("Demo1")

#이벤트 루프

running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #동작이 들어오는지 확인
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가
            running = False #게임 진행 멈춤

# 종료
pygame.quit()
