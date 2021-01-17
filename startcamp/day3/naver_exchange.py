# 웹페이지 크롤링
# https://finance.naver.com/marketindex/

# 1. 크롤링 할 때 필요한 기능 모음(라이브러리) 가져오기
import requests  # 요청을 보내고 응답을 받아오는 역할
from bs4 import BeautifulSoup  # 데이터를 구조화 (예쁘게!)

# 2. 데이터를 추출할 URL 확인
url = 'https://finance.naver.com/marketindex/' # 요청 보낼 주소 필요

# 3. 요청 보내기
# response = requests.get(url)    # 상태코드 200 == 불러오는데 성공. 잘 왔다
response = requests.get(url).text
# print(type(response))

# 4. 응답받은 값을 추출하기 쉬운 형태로 구조화 (예쁘게 만들기)
soup = BeautifulSoup(response, 'html.parser')
# print(type(soup))

# 5. 원하는 데이터 추출하기
exchange = soup.select_one('#exchangeList > li:nth-child(1) > a.head.usd > div > span.value').text
print(exchange)

# 최종 결과값 출력
# 현재 원/달러 환율은 000입니다.
print(f'현재 원/달러 환율은 {exchange}입니다.')