# Todo List  만들어보기

![todoGIF](https://user-images.githubusercontent.com/77573938/116397758-f32c6880-a861-11eb-9755-9baab4d450bf.gif)

<br>

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









