/*
	[배열 관련 주요 메서드 연습 1]
	
	주어진 배열의 요소 중 null 값을 제거한 새로운 배열을 만드세요.
*/

const homeworks = ['david.zip', null, 'maria.zip', 'tom.zip', null]

const result = []
for (const homework of homeworks) {
	if (homework != null)  // if (homework) 로 써도 된다. 값이 있으면 true이기 때문
	result.push(homework)
}


/*
	[배열 관련 주요 메서드 연습 2]
	
	주어진 배열을 사용하여 아래 문자열을 완성하세요.

	'www.samsung.com/sec/buds/galaxy-buds-pro'

*/

const arr1 = ['www', 'samsung', 'com']
const arr2 = ['galaxy', 'buds', 'pro']
const arr3 = ['sec', 'buds']

// let result = ''
// result = arr1.join('.') + ('/') + arr3.join('/') + ('/') + arr2.join('-')

let homepage = arr1.join('.')
let product = arr2.join('-')
arr3.unshift(homepage)  // ["www.samsung.com", "sec", "buds"]
arr3.push(product)  // ["www.samsung.com", "sec", "buds", "galaxy-buds-pro"]


/*
	[배열 관련 주요 메서드 연습 3]

	주어진 배열의 요소 중 모든 'rainy' 요소를 'sunny'로 교체하세요
	- indexOf 메서드를 사용합니다.
*/

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']
while (weather.indexOf('rainy') > 0) {
	weather[weather.indexOf('rainy')] = 'sunny'
}
console.log(weather)

/*
includes 메서드 사용 ver.

const weather = ['sunny', 'sunny', 'sunny', 'sunny', 'rainy', 'rainy', 'sunny']
while (weather.includes('rainy')) {
	weather[weather.indexOf('rainy')] = 'sunny'
}
console.log(weather)

*/