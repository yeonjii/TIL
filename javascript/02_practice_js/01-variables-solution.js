/*
  [let 키워드 연습]
  
  1. let 키워드를 이용하여 ssafy 변수를 작성하세요.
  2. ssafy 변수에 '제주도'를 할당하세요.
  3. ssafy 변수의 값을 현재 여러분의 지역으로 재할당하세요.
*/

let ssafy = '제주도'
ssafy = '광주'
console.log(ssafy)  // 광주


/*
  [const 키워드 연습]
  
  1. const 키워드를 이용하여 phone 변수를 작성하세요.
  2. phone 변수에 'Galaxy S2'을 할당하세요.
  3. phone 변수의 값을 현재 여러분의 핸드폰 기종을 재할당하세요.
  4. 재할당 에러를 확인하세요.
*/

const phone = 'Galaxy S2'
phone = 'iphone XR'
// Uncaught TypeError: Assignment to constant variable. 값이 이미 할당된 const 변수에 재할당했기 때문


/*
  [블록 스코프 - let 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  console.log('블록 스코프:', fullName)  // 블록 스코프: Guido Van Rossum
}

console.log('전역 스코프:', fullName)  // 전역 스코프: Brendan Eich


/*
  [블록 스코프 - const 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

let fullName = 'Brendan Eich'

if (fullName === 'Brendan Eich') {
  let fullName = 'Guido Van Rossum'
  const language = 'Python'
}

console.log(language) // ReferenceError: language is not defined


/*
  [var 키워드 연습]
  
  1. var 키워드를 이용하여 framework 변수를 작성하세요.
  2. framework 변수에 'Bootstrap'를 할당하세요.
  3. framework 변수에 'Django'를 재할당하세요.
  4. framework 변수를 재선언하고 'Vue'를 할당하세요.
*/

var framework = 'Bootstrap'  // Bootstrap
framework = 'Django'  // Django
var framework = 'Vue'  // Vue


/*
  [함수 스코프 - var 키워드 예시]
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

function f1() {
  var message = 'You are doing great!'
}
console.log(message) // ReferenceError: message is not defined


/*
  [블록 스코프 - var 키워드 예시]

  Tip.
    if문은 블록 스코프를 생성합니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

const codeEditor = 'vscode'

if (codeEditor === 'vscode') {
  var theme = 'dark+'
}
console.log(theme)  // dark+


/*
  [블록 스코프 - const, let 키워드 예시]
  
  Tip. 
    const와 let은 블록 스코프입니다.
    함수의 중괄호도 블록에 해당됩니다.
  
  아래 코드 실행 후 결과를 확인해보세요.
*/

function f2() {
  const stack = 'Last In, First Out'
}
console.log(stack)  // ReferenceError: stack is not defined

function f3() {
  let queue = 'First In, First Out'
}
console.log(queue)  // ReferenceError: queue is not defined


/*
  [호이스팅(hoisting)]
  
  아래 코드 실행 후 결과를 확인해보세요.
  그리고 const와 let의 경우와 비교해보세요.
*/

console.log(hoisted)  // undefined
var hoisted = 'can you see me?'

console.log(lunch)  // Uncaught ReferenceError: Cannot access 'lunch' before initialization. 초기화 전에는 참조할 수 없다
const lunch = '초밥'

console.log(dinner)  // Uncaught ReferenceError: dinner is not defined
let dinner = '스테이크'