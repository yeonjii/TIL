[TOC]

# RESET CSS

> 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
>
> HTML5 Element, Typograph, Table, List 등의 요소들에 일관성있게 스타일을 적용 시키는 기본 단계

<br>

## 사용 배경

- 모든 브라우저는 각자의 `user agent stylesheet` 를 가지고 있는데 (웹사이트를 보다 읽기 편하게 하기 위해)
- 문제는 이 설정이 브라우저마다 상이하다는 것

<br>

## 종류

**Normalize CSS**

> gentle solution

- W3C 의 표준을 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정한다.
- 경우에 따라 IE 또는 EDGE 는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 Normalize 는 IE 또는 EDGE 의 스타일을 나머지 브라우저에 적용시킨다.
- 실제 bootstrap 에서는 normalize.css를 자체적으로 커스텀해서 `bootstrap-reboot.css` 라는 이름으로 사용한다.

<br>

**Reset CSS**

>  aggressive solution

- 브라우저의 기본 스타일이 전혀 필요 없다는 방식으로 접근한다.
- 따라서 브라우저의 user agent와 함께 제공되는 모든 스타일을 재설정한다.
- Reset CSS의 문제점은 너무나 많은 선택자가 엉켜있고, 불필요한 오버라이드가 많이 발생하며 디버깅 시 제대로 읽을 수 없다.

<br>

## 마무리

- 현재는 Normalize CSS 를 중심으로 사용하며 더해서 적절한 Reset CSS을 섞어 쓰라고 권장한다. (오래된 Reset CSS 를 사용하지 않도록 주의한다.)
- 무엇보다 더 중요한 건, ***"내 프로젝트에 명확하게 필요한 사항들인지 확인"*** 하는 것
- 최종적으로 자신만의 Reset style sheet를 만들어 나가기는 것이 좋다.

<br>

## 참고문헌

https://cssreset.com/

https://github.com/necolas/normalize.css/blob/master/normalize.css

https://medium.com/@elad/normalize-css-or-css-reset-9d75175c5d1e