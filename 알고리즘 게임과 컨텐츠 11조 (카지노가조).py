print("블랙잭을 시작하시겠습니까? 네 or 아니오")

start =input()
print(f'{start}를 선택하셨습니다.')

if start == "네":
    print("블랙잭을 시작합니다. 카드를 분배합니다.")
elif start == "아니오":
    print("게임을 종료합니다.")
    quit()

  
#블랙잭 카드 분배

import random


# s = 스페이드, c = 클로버, h = 하트, d = 다이아몬드

s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
h = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#뽑은 숫자 변수 선언
num1 = 0
num2 = 0
num3 = 0
num4 = 0
num5 = 0
num6 = 0

#카드 섞고 랜덤으로 2개 뽑기

deck = (s+c+h+d)
random.shuffle(deck) 

class card:
    def draw():
        r = deck[random.randrange(len(deck))]
        return r
        
for i in range(2):
    num1 = card.draw()
    num2 = card.draw()
    deck.remove(num1)
    deck.remove(num2)


#딜러의 카드 출력
number1 = 0
number2 = 0
number3 = 0
number4 = 0
number5 = 0
number6 = 0
numbers = number1 + number2 + number3 + number4 + number5 + number6
dealer_number = 0

#딜러의 카드 뽑기
class card:
    def draw():
        s = deck[random.randrange(len(deck))]
        return s
        
for i in range(2):
    number1 = card.draw()
    number2 = card.draw()
    deck.remove(number1)
    deck.remove(number2)

while numbers < 17:
    if number3 == 0:
        number3 = card.draw()
        deck.remove(number3)
        numbers = number1 + number2 + number3 + number4 + number5 + number6
        dealer_number = 1
        
    elif number3 != 0:
            if number4 == 0:
                number4 = card.draw()
                deck.remove(number4)
                numbers = number1 + number2 + number3 + number4 + number5 + number6
                dealer_number = 2
            elif number4 != 0:
                if number5 == 0:
                    number5 = card.draw()
                    deck.remove(number5)
                    numbers = number1 + number2 + number3 + number4 + number5 + number6
                    dealer_number = 3
                elif number5 != 0:
                    if number6 ==0:
                        number6 = card.draw()
                        deck.remove(number6)
                        numbers = number1 + number2 + number3 + number4 + number5 + number6
                        dealer_number = 4

#카드 결과 출력

print("첫 번째 카드는", num1, "입니다.")
print("두 번째 카드는", num2, "입니다.")
print("카드의 총합은", num1+num2, "입니다.")
# print(number1,number2,number3,number4,number5,number6)
if dealer_number == 0:
    print("상대의 두번째 숫자는", number2, "입니다.")
elif dealer_number == 1:
    print("상대의 두번째, 세번째 숫자는", number2,",", number3, "입니다.")
elif dealer_number == 2:
    print("상대의 두번째, 세번째 숫자, 네번째 숫자는", number2,",", number3,",", number4, "입니다.")
elif dealer_number == 3:
    print("상대의 두번째, 세번째 숫자, 네번째 숫자, 다섯번째 숫자는", number2,",", number3,",", number4,",", number5, "입니다.")
elif dealer_number == 4:
    print("상대의 두번째, 세번째 숫자, 네번째 숫자, 다섯번째 숫자, 여섯번째 숫자는", number2,",", number3,",", number4,",", number5,",", number6, "입니다.")

if numbers == 21:
    if num1 + num2 < 21:
        print("블랙잭! 당신의 패배입니다!")
        quit()
    elif num1 + num2 == 21:
        print("무승부입니다.")
        quit()
elif numbers > 21:
    print("상대의 숫자 합이 21을 넘었습니다. 당신의 승리입니다.")
    quit()

if num1 + num2 > 21:
    print("당신의 패배입니다!")
    quit()
elif num1 + num2 == 21:
        print("블랙잭! 당신의 승리입니다!")
        quit()
elif num1 + num2 < 21:
    print("카드를 더 받으시겠습니까? 네 or 아니오")
    
#카드받기 질문의 반복
    
choice =input()
print(f'{choice}를 선택하셨습니다.')

if choice == "네":
    print("카드를 한 장 더 분배합니다.")
    card.draw()
    for i in range(1):
        num3 = card.draw()
        deck.remove(num3)
    print("추가된 카드는",num3, "입니다.")
    print("카드의 총합은", num1 + num2 + num3, "입니다.")
elif choice == "아니오":
    num3 = 0
    nums = num1 + num2 + num3 + num4 + num5 + num6
    print("결과를 확인합니다. 플레이어의 숫자 합은", nums,"이고, 상대의 숫자 합은", numbers , "입니다.")
    if nums > numbers:
        print("플레이어가 이겼습니다.")
    elif nums == numbers:
        print("무승부입니다.")
    else :
        print("패배하였습니다.")
    quit()

if num1 + num2 + num3 > 21:
    print("당신의 패배입니다!")
    quit()
elif num1 + num2 + num3 == 21:
    print("블랙잭! 당신의 승리입니다!")
    quit()
elif num1 + num2 + num3 < 21:
    print("카드를 더 받으시겠습니까? 네 or 아니오")


choice =input()
print(f'{choice}를 선택하셨습니다.')    

if choice == "네":
    print("카드를 한 장 더 분배합니다.")
    card.draw()
    for i in range(1):
        num4 = card.draw()
        deck.remove(num4)
    print("추가된 카드는",num4, "입니다.")
    print("카드의 총합은", num1 + num2 + num3 + num4, "입니다.")
elif choice == "아니오":
    num4 = 0
    print("결과를 확인합니다.")
    nums = num1 + num2 + num3 + num4 + num5 + num6
    print("결과를 확인합니다. 플레이어의 숫자 합은", nums,"이고, 상대의 숫자 합은", numbers , "입니다.")
    if nums > numbers:
        print("플레이어가 이겼습니다.")
    elif nums == numbers:
        print("무승부입니다.")
    else :
        print("패배하였습니다.")
    quit()
    
if num1 + num2+ num3 + num4 > 21:
    print("당신의 패배입니다!")
    quit()
elif num1 + num2 + num3 + num4 == 21:
        print("블랙잭! 당신의 승리입니다!")
        quit()
elif num1 + num2 + num3 + num4 < 21:
    print("카드를 더 받으시겠습니까? 네 or 아니오")


choice =input()
print(f'{choice}를 선택하셨습니다.')    

if choice == "네":
    print("카드를 한 장 더 분배합니다.")
    card.draw()
    for i in range(1):
        num5 = card.draw()
        deck.remove(num5)
    print("추가된 카드는",num5, "입니다.")
    print("카드의 총합은", num1 + num2 + num3 + num4 + num5, "입니다.")
elif choice == "아니오":
    num5 = 0
    print("결과를 확인합니다.")
    nums = num1 + num2 + num3 + num4 + num5 + num6
    print("결과를 확인합니다. 플레이어의 숫자 합은", nums,"이고, 상대의 숫자 합은", numbers , "입니다.")
    if nums > numbers:
        print("플레이어가 이겼습니다.")
    elif nums == numbers:
        print("무승부입니다.")
    else :
        print("패배하였습니다.")
    quit()
    
if num1 + num2+ num3 + num4 + num5 > 21:
    print("당신의 패배입니다!")
    quit()
elif num1 + num2 + num3 + num4 + num5 == 21:
        print("블랙잭! 당신의 승리입니다!")
        quit()
elif num1 + num2 + num3 + num4 + num5 < 21:
    print("카드를 더 받으시겠습니까? 네 or 아니오")


choice =input()
print(f'{choice}를 선택하셨습니다.')    

if choice == "네":
    print("카드를 한 장 더 분배합니다.")
    card.draw()
    for i in range(1):
        num6 = card.draw()
        deck.remove(num6)
    print("추가된 카드는",num6, "입니다.")
    print("카드의 총합은", num1 + num2 + num3 + num4 + num5 + num6, "입니다.")
elif choice == "아니오":
    q = 0
    nums = num1 + num2 + num3 + num4 + num5 + num6
    print("결과를 확인합니다. 플레이어의 숫자 합은", nums,"이고, 상대의 숫자 합은", numbers , "입니다.")
    if nums > numbers:
        print("플레이어가 이겼습니다.")
    elif nums == numbers:
        print("무승부입니다.")
    else :
        print("패배하였습니다.")
    print("결과를 확인합니다.")
    quit()
    
if num1 + num2+ num3 + num4 + num5 + num6 > 21:
    print("당신의 패배입니다!")
    quit()
elif num1 + num2 + num3 + num4 + num5 + num6 == 21:
    print("블랙잭! 당신의 승리입니다!")
    quit()
elif num1 + num2 + num3 + num4 + num5 + num6 < 21:
    print("카드를 더 받으시겠습니까? 네 or 아니오")

    

