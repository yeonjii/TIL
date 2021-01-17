# import 문은 스크립트 파일 최상단에 위치한다
import random

# 1~45번 숫자 만들어서 저장하기
numbers = range(1, 46)
# print(numbers)

# numbers에서 6개 숫자 뽑아서 저장하기
lucky_numbers = random.sample(numbers, 6)   # 리스트에서 특정 개수의 요소를 랜덤하게 비복원추출
print(sorted(lucky_numbers))    # sorted: 작은 숫자 순으로 정렬