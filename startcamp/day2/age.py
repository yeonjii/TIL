import requests

# API 요청 URL 확인 + 필요한 데이터 건네주기
name = input()
url = f'https://api.agify.io/?name={name}'

# URL로 요청 보내기
response = requests.get(url).json()  # requests.get(url)를 분석해서 json화 시켜줌
print(response)

# 응답결과 확인 후 정보 추출하기
name = response['name']
age = response['age']
print(f'{name}님의 예상 나이는 {age}살 입니다.')