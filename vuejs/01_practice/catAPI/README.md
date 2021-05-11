# [Vue.js] API로 서버에 요청보내고 이미지 응답받기

Vue와 axios를 활용하여 API 서버로 요청을 보내 응답 받은 이미지를 화면에 표시하는 앱을 완성해보자

- 사용 API : https://api.thecatapi.com/v1/images/search

![image-20210506201546836](https://user-images.githubusercontent.com/77573938/117289942-2e551a00-aea8-11eb-8458-05a2468923d5.png)

<br>

## 과정

1. Vue와axios를 사용하기 위해 공식문서에서 CDN과 라이브러리를 설치한다.

2. HTML 기본 구조를 잡는다.

   API로 받은 이미지를 넣을 img 태그와 버튼을 누르면 이미지가 랜덤으로 바뀔 수 있도록 버튼 태그를 만들어줌.

   Vue 인스턴스와 연결시킬 예정이므로 잊지말고 **id를 할당**해주기 !

3. Vue 인스턴스를 만든다.

4. img 태그에 Vue인스턴스 데이터를 **바인딩** 시키고, 버튼이 클릭되었을 때 함수가 실행될 수 있도록 `@` 이벤트 핸들링을 해준다.

<br><br>

## 완성 !

`Get Cat` 버튼을 클릭하면 axios를 통해 API로 요청을 보내고 응답 받은 데이터를 img 요소의 리소스로 할당한다.

![catapi](https://user-images.githubusercontent.com/77573938/117289929-2b5a2980-aea8-11eb-8fc5-93dc5dcb89a0.gif)

