from random import randint

print("Welcome to Python Casino!")

pc_choice = randint(1, 100)  #imported random

playing = 0
heart = 5
view = heart-1

while playing < heart:
    user_choice = int(input("Choose number (1~100) : "))  #(int) 실수랑 비교 할때 넣어야함
    if user_choice == pc_choice:
        print("정답이에요!")
        print("정답은", pc_choice,"이었습니다.")
        exit()
    elif user_choice > pc_choice:
        print("너무 높아요 \n남은기회 :", view)
        playing = playing + 1
        view = view - 1
    elif user_choice < pc_choice:
        print("너무 낮아요 \n남은기회 :", view)
        playing = playing + 1
        view = view - 1

if playing == heart:
    print("기회가 소진되었습니다.")
    print("정답은", pc_choice,"이었습니다.")
