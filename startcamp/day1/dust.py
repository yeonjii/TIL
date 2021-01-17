# 패키지 설치
# pip install beautifulsoup4 requests lxml

import requests
from bs4 import BeautifulSoup

key = 'SJq6idSlitXpK%2BZDyH%2BgJYwz9HOo8HR2htxRSTBTCIxzPDsTVqXsOcz5I5ZrCUHXw4o4CAE6HFdgkZCzsMQSeA%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'

response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)

item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')


# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해보세요.
if dust > 150:
    print('매우나쁨')
elif dust > 81:
    print('나쁨')
elif dust > 31:
    print('보통')
else:
    print('좋음')
