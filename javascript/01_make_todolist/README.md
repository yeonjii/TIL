# Todo List  만들어보기

### 최종 결과물

![todo_c_GIF](https://user-images.githubusercontent.com/77573938/116540663-706ce180-a925-11eb-8593-e3c96c01438c.gif)

<br>

### 처음 결과물

![todoGIF](https://user-images.githubusercontent.com/77573938/116397758-f32c6880-a861-11eb-9755-9baab4d450bf.gif)

<br><br>

## 세부 사항

다음의 기능을 충족하는 todo app 을 완성했다.

- form 태그를 사용하여, submit 되었을 시 todo가 작성된다.
- 작성된 todo는 ul 태그의 li 태그로 추가된다.
- 작성 후 input value 값는 초기화 된다.
- 빈 값의 데이터는 입력을 방지한다.
- 빈 값 입력 시 브라우저 팝업을 출력한다.
- 작성한 Todo 아이템을 클릭 시 아이템에 취소선을 추가하고 제거할 수 있다.
- `X` 버튼을 통해 아이템을 삭제할 수 있다.

<br>

## 💾 최종 버전 (todo_complete.html)

### form 태그 사용하여, submit 되었을 시 todo가 자동으로 등록

```javascript
// Enter, click 전부 가능
const form = document.querySelector('form')
form.addEventListener('submit', addTodo)
```

<br>

### 빈 값을 입력한 경우, 알림창 띄우기

`trim()` 메소드를 사용해 양쪽의 띄어쓰기를 날렸다.

```javascript
    function addTodo () {
      event.preventDefault()  // 파라미터가 비었음에도 디폴트로 event가 들어가기 때문에 preventDefault를 넣어준다.
      const input = document.querySelector('input')
      const content = input.value

      if (content.trim()) {  // trim:양쪽에 띄어쓰기를 날린 것
        ...

      } else {
        alert('빈칸 입니다 ! 내용을 입력해주세요.')
      }
  
      event.target.reset()  // input.value를 초기화
    }
```

<br>

### 작성한 아이템을 클릭 시 취소선을 추가 및 제거하기

- 방법 1

`toggle` 을 사용해 on-off 기능을 구현했다.

```javascript
        li.addEventListener('click', function (event) {
          event.target.classList.toggle('done')  // toggle: on-off 기능 구현
        })
```

- 방법 2 

조건문으로 class를 더하고 제거한다.

```javascript
        li.addEventListener('click', function (event) {
          if (event.target.classList.contains('done')) {
            event.target.classList.remove('done')
          } else {
            event.target.classList.add('done')
          }
        })
```

<br>

### `X` 버튼을 통해 아이템 삭제하기

- 방법 1

가장 나은 방식

```javascript
        const deleteBtn = document.createElement('button')
        deleteBtn.innerText = 'X'
        li.appendChild(deleteBtn)
        deleteBtn.addEventListener('click', function () {
          event.target.parentNode.remove()
        })
```

- 방법 2

`li` 가 함수 밖에 있는데 그걸 참조하므로 방법 1에 비해 선호되는 방식은 아니다.

외부함수가 종료돼서 변수가 없어져야하는데, 내부함수가 참조하고 있어서 데이터가 삭제되지 않고 계속해서 존재해서 li를 참조할 수 있는 것이다.

```javascript
        const deleteBtn = document.createElement('button')
        deleteBtn.innerText = 'X'
        li.appendChild(deleteBtn)
        deleteBtn.addEventListener('click', function () {
          // ul.removeChild(li)  // 1️⃣ 또는
          li.remove()  // 2️⃣
        })
```

<br><br>

## 💾 처음 버전 (todo_first.html)

처음 버전은 form태그로 구성하지 않고 script에서 함수로 기능을 구현했다.



### add버튼이 눌리면 alert로 버튼이 눌렸다고 알리는 방법

1. 함수를 바로 정의

```js
    const addButton = document.querySelector('button')
    addButton.addEventListener('click', function(){
      alert('버튼 눌렸음!')
    })
```

2. 함수를 미리 만들고 갖고 오기

```js
    function onClick(){
      alert('버튼 눌렸음!')
    }

    const addButton = document.querySelector('button')
    addButton.addEventListener('click', onClick)
```

<br>

### 빈 값을 입력한 경우, 알림창 띄우기

함수 내에 조건문 사용 가능. 함수를 즉시 종료하고 싶은 경우에는 `return`을 사용한다.

```js
    function onClick(){
      // input창에 입력된 텍스트를 가지고 온다.
      const input = document.querySelector('input')
      // 빈 값인 경우 alert 띄우기
      if (input.value == '') {
        alert('빈값입니다 !')
        return  // 함수를 즉시 탈출 하게 함
      }
        
      const newTodoLi = document.createElement('li')
      newTodoLi.innerText = input.value
      const ul = document.querySelector('ul')
      ul.appendChild(newTodoLi)
      input.value = ''
    }

    const addButton = document.querySelector('button')
    addButton.addEventListener('click', onClick)
```

<br>

## Enter로 입력되게 하기

![click,enter](https://user-images.githubusercontent.com/77573938/116397754-f1fb3b80-a861-11eb-8e36-597aa8f5faa2.gif)

`change` 속성은 실제 Enter 버튼만 가능한 것은 아니다. 입력 값에 어떤 변화가 있을 경우 함수가 실행되도록 하는 것이다.

폼태그를 쓰면 따로 클릭과 엔터를 안 나눠도 둘 다 가능하다. (form태그로 구현하면 뭘로 하든 자동으로 submit됨)

이 경우 form태그를 사용하지 않아 클릭과 엔터 두가지로 구성했다.

```js
    function onClick(){
      // input창에 입력된 텍스트를 가지고 온다.
      const input = document.querySelector('input')

      // 빈 값은 입력하지 못하도록 설정
      if (input.value != '') {
        // ul태그에 자식으로 li태그를 만들어서 추가하려면? -> li태그 만들고 ul태그 갖고 와서 자식으로 추가
        const newTodoLi = document.createElement('li')
        newTodoLi.innerText = input.value  // li태그에 글 추가
        const ul = document.querySelector('ul')
        ul.appendChild(newTodoLi)
        input.value = ''  // input 입력 후 초기화 (null로 해도 됨)
      }
    }

    const addButton = document.querySelector('button')  // 버튼 클릭 시 함수 실행
    addButton.addEventListener('click', onClick)

    // 위의 함수에서 사용하는 input은 여기서 사용 못하기 때문에 새로 가져와야 한다.
    const myInput = document.querySelector('input')
    myInput.addEventListener('change', onClick)
```

