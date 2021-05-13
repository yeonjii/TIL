# Vue Digest

> **Vuex를 사용하는 이유 ?**
>
> - 컴포넌트가 많아졌을 경우 데이터의 관리가 어려워짐
> - **컴포넌트 간 데이터 공유**를 편하게 하기 위하여 사용

대부분의 경우, 실제로 Vuex 거의 사용



## 1. Vuex 구성 요소

- state : 데이터
- getters : computed와 비슷한 역할
- mutations : state를 변경하는 역할 (== state를 직접 조작하면 안된다는 뜻)
- actions : state를 비동기적으로 변경하는 역할 
  - (참고) mutations를 통해 "간접적으로" state를 변경한다.



## 2. 컴포넌트에서의 활용법

- state, getters => computed에서 주로 활용

  ```javascript
  // state
  this.$store.state.키 값
  
  // getters
  this.$store.getters.함수명
  ```



- mutations, actions => methods에서 주로 활용

  ```javascript
  // mutations
  // git에서 commit? => 기록.
  // mutations은 state의 변경사항을 기록.
  this.$store.commit('함수명', 매개변수)
  
  // actions
  this.$store.dispatch('함수명', 매개변수)
  ```



## 3. Vuex Helper

> Vuex의 각 속성들을 더 쉽게 사용하는 방법

- store에 있는 요소들의 등록을 도와주는 함수

  - 더이상 `this.$store` 이렇게 할 필요 없음

  ```javascript
  // App.vue
  
  import { mapState } from 'vuex'
  import { mapGetters } from 'vuex'
  import { mapMutations } from 'vuex'
  import { mapActions } from 'vuex'
  
  export default {
      computed: {
          ...mapState(['이름1', '이름2']),  // 불러오고 싶은거 배열형태로
          ...mapGetters(['이름1', '이름2']),
      },
      methods: {
          ...mapMutations(['함수명1', '함수명2']),
          ...mapActions(['함수명1', '함수명2']),
      },    
  }
  ```

<br>

---



# [animal-app] Vuex 연습

```bash
$ vue create appname
$ cd appname/
$ vue add vuex
$ npm run serve
```

<br>

## async - await

함수 앞에 `async` 붙이고, 비동기적으로 동작하는 코드들(대표적으로 axios 같은거) 앞에 `await`를 붙이면 마치 동기처럼 작동한다.

- 에러는 `try~catch` 를 작성하여 처리

- 장점 : 가독성 굿굿 & 최신문법 - 실제 개발, 현업에서는 `async-await` 많이 씀

<br>

- `async-await`  사용전

```javascript
// App.vue

methods: {
  ...mapMutations(['UPDATE_ANIMAL_IMAGES']),
  fetchCatImg() {
    const CAT_API_URL = 'https://api.~~~'
    axios.get(CAT_API_URL)
    .then((response) => {
      const catImgUrl = response.data[0].url
      this.UPDATE_ANIMAL_IMAGES(catImgUrl)
    })
    .catch((error) => {
      console.log(error)
    })
  },
}
```



- `async-await` 사용
  - axios는 promise 객체를 반환하는데,  resolve일때의 값이 response에 담기는 것

```javascript
methods: {
    ...mapMutations(['UPDATE_ANIMAL_IMAGES']),
    async fetchCatImg() {
        const CAT_API_URL = 'https://api.~~~'
        const response = await axios.get(CAT_API_URL)
        const catImgUrl = response.data[0].url
        this.UPDATE_ANIMAL_IMAGES(catImgUrl)
    }
}
```



- `async-await` 사용 + 에러 처리

```javascript
methods: {
    ...mapMutations(['UPDATE_ANIMAL_IMAGES']),
    async fetchCatImg() {
        const CAT_API_URL = 'https://api.~~~'
        try {
            const response = await axios.get(CAT_API_URL)
            const catImgUrl = response.data[0].url
            this.UPDATE_ANIMAL_IMAGES(catImgUrl)
        } catch(err) {
            console.error(error)  // console.log(error)와 차이점: 개발자도구에서 에러가 빨갛게 뜸
        }
    }
}
```



<br>

## 결과

![resgif](https://user-images.githubusercontent.com/77573938/118144014-ebb2b500-b446-11eb-9e10-9627a9600086.gif)




