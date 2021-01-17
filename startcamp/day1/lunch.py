menu = ['맥날', '버거킹', '롯데리아', '맘스터치']
print(menu[-1], menu[-2]) # 음수는 뒤에서 부터 카운트

phone_book = {'맥날' : '123-456', '버거킹': '000-204', '롯데리아': '02-573', '맘스터치': '697-203'}  #<-딕셔너리
print(phone_book)
print(phone_book['맥날'])


# 1. 가계 하나 랜덤으로 추천받기
import random

my_menu = random.choice(menu)
print(my_menu)
print(phone_book[my_menu])

my_menu = random.choice(menu)
print(my_menu + '의 전화번호는 ' + phone_book[my_menu] + '입니다.') # 문자열은 플러스 연산자로 연결해서 나타낼 수 있음.
print(f'{my_menu}의 전화번호는 {phone_book[my_menu]}입니다.')  # f-string -> python 3.6