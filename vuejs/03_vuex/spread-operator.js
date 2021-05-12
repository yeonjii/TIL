// ... (Spread Operator)
const numbers = [1, 2, 3, 4, 5]
const newNumbers = [...numbers]  // [ 1, 2, 3, 4, 5 ]
console.log(newNumbers) // 콘솔 찍어볼때 터미널창에 "$ node spread-operator.js" 입력
console.log(...numbers) // 1 2 3 4 5

const obj = {
  a: 1,
  b: 2,
}
const newObj = {
  ...obj,
}
console.log(newObj)  // { a: 1, b: 2 }