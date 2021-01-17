# 공공 데이터 API 활용 실습 (대기오염정보)

# 1. 필요한 라이브러리 import 하기
import requests, pprint

# 2. API URL 및 KEY 값 확인
sidoName = '서울'
key = '4lKc9J%2FqRiO9yasGEJ%2FejGxAR0y5yKZ72E9k3HgUnK%2BQTV9CsJ6xqyb3%2BcXWrcKeJUDTDdvSrDMyQY9qBTAnLw%3D%3D'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&sidoName={sidoName}&returnType=json'

# 3. 요청 및 응답값 확인
response = requests.get(url).json()
# pprint.pprint(response)

sidoName = response['response']['body']['items'][0]['sidoName']
pm10Value = response['response']['body']['items'][0]['pm10Value']
stationName = response['response']['body']['items'][0]['stationName']

# 4. 최종 출력 문자열
# '__의 미세먼지 농도는 __ 입니다. (측정소: ___)'
text = f'{sidoName}의 미세먼지 농도는 {pm10Value}입니다. (측정소: {stationName})'

# 5. 텔레그램 메세지 전송 (sendMessage)

token = ''
chat_id = ''

telegram_url = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={chat_id}&text={text}'

requests.get(message_url)