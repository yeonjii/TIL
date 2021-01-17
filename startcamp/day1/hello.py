greeting = '안녕하세요!'

# 1. while문 반복 (while 몇번 반복할건지 조건이 들어가야함)
count = 0
while count < 5:
    print(greeting)
    count+= 1


# 2. for문 반복
count_list = [0, 1, 2, 3]
for num in count_list:
    print(greeting)


# 3. for문 반복 (함수 활용)
for num in range(4):
    print(greeting)