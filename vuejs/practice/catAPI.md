# [Vue.js] API로 서버에 요청보내고 이미지 응답받기

Vue와 axios를 활용하여 API 서버로 요청을 보내 응답 받은 이미지를 화면에 표시하는 앱을 완성해보자

- 사용 API : https://api.thecatapi.com/v1/images/search

![image-20210506201546836](https://user-images.githubusercontent.com/77573938/117289942-2e551a00-aea8-11eb-8458-05a2468923d5.png)

<br>

## 과정

Get Cat 버튼을 클릭하면 axios를 통해 API로 요청을 보내고 응답 받은 데이터를 img 요소의 리소스로 할당한다.

잊지말고 img 태그에 바인딩 시켜주자 !

<br><br>

## 결과물

![catapi](https://user-images.githubusercontent.com/77573938/117289929-2b5a2980-aea8-11eb-8fc5-93dc5dcb89a0.gif)

