/*
  [Number 타입 연습]

  - hour 변수에 현재 시간의 "시(hour)를 초(second)로 바꿔서" 저장하세요.
  - minute 변수에 현재 시간의 "분(minute)을 초(second)로 바꿔서" 저장하세요. 
  - curTime 변수에 hour와 minute의 합을 저장 후 출력해보세요.
*/

const hour = 9*60*60
const minute = 43*60
const curTime = hour + minute
console.log(curTime)


/*
  [String 타입 연습]

  - username 변수에 여러분의 이름을 입력하세요.
  - message 변수에 인사말을 작성하세요.
  - username 변수에 greeting을 할당 연산자로 이어붙인 후 출력해보세요. 
*/

let username = 'yeonji'
let message = '안녕하세요!'
username += message
console.log(username)  // yeonji안녕하세요!


/*
  [String 타입 연습]

  템플릿 리터럴(Template Literal) 활용

  - viewCnt 변수를 활용하여 예시와 같은 문장을 만들어보세요.
  - 예시) 조회수 500회
*/

const viewCnt = 500
console.log(`조회수 ${viewCnt}회`)


/*
  [undefined vs. null]

  Tip.
    - undefined는 변수 선언 시 값을 할당하지 않을 때 할당되는 값입니다.
    - null은 개발자가 의도적으로 값이 없음을 표현할 때 할당하는 값입니다. 

  아래 코드 실행 후 결과를 확인해보세요.
*/

let unknown
console.log(unknown)  // undefined (unknown이라는 변수를 만들고 값을 안 넣어줬기 때문에)

const nullValue = null
console.log(nullValue)  // null
console.log(typeof nullValue)  // object


/*
  [Boolean 타입 연습]

  Tip.
    파이썬과 다르게 자바스크립트의 Boolean 타입은 
    첫 단어가 소문자임에 주의하세요.

  - isLoggedIn 변수에 false를 할당하세요.
  - isLoggedIn 변수의 값을 true로 바꾸고 출력해보세요.
*/
let isLoggedIn = false
isLoggedIn = true
console.log(isLoggedIn)  // true


/*
  [삼항(Ternary) 연산자 연습]
  
  Tip.
    condition ? expression if true : expression if false

  아래의 조건을 만족하는 삼항 연산자를 작성해보세요.
  - 조건문에서 subscribed 변수의 참/거짓 여부를 판별합니다.
  - 조건이 참이면 '구독취소'를 반환합니다.
  - 조건이 거짓이면 '구독중'을 반환합니다.
  - 삼항 연산자의 반환값을 message 변수에 할당 후 출력합니다.
*/

const subscribed = false
const message = subscribed ? '구독취소' : '구독중'
console.log(message)  // 구독중