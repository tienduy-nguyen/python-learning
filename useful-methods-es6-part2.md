# Useful Methods In ES6 JavaScript - part 1

## Table of contents

- [Useful Methods In ES6 JavaScript - part 1](#useful-methods-in-es6-javascript---part-1)
  - [Table of contents](#table-of-contents)
  - [Reverse string](#reverse-string)
  - [Factiorial of numbers](#factiorial-of-numbers)
  - [Convert number to array](#convert-number-to-array)
  - [Test if a number is a power of 2](#test-if-a-number-is-a-power-of-2)
  - [Create array dictionary from objects](#create-array-dictionary-from-objects)
  - [Return max of array](#return-max-of-array)
  - [Check every items in array are equal?](#check-every-items-in-array-are-equal)
  - [Average of array](#average-of-array)
  - [Return power set of array](#return-power-set-of-array)



## Reverse string
```js
const reverseString = string => [...string].reverse().join('')
//Or
// const reverseString = string => string.split().reverse().join('')


// Example
reverseString('Medium') // "muideM"
reverseString('Better Programming') // "gnimmargorP retteB"
```


## Factiorial of numbers

```js
const factorialOfNumber = number => 
  number < 0
    ? (() => {
      throw new TypeError('Error')
    })()
    : number <= 1
      ? 1
      : number * factorialOfNumber(number - 1)


// Example
factorialOfNumber(4) // 24
factorialOfNumber(8) // 40320
```

## Convert number to array
```js
const converToArray = number => [...`${number}`].map(el => parseInt(el))

// Example
converToArray(5678) // [5, 6, 7, 8]
converToArray(12345678) // [1, 2, 3, 4, 5, 6, 7, 8]
```


## Test if a number is a power of 2
```js
const isNumberPowerOfTwo = number => !!number && (number & (number - 1)) == 0

// Example
isNumberPowerOfTwo(100) // false
isNumberPowerOfTwo(128) // true
```

## Create array dictionary from objects

```js
const keyValuePairsToArray = object => Object.keys(object)
  .map(el => [el, object[el]])

// Example
keyValuePairsToArray({Better: 4, Programming: 2})
// [['Better', 4], ['Programming', 2]]

keyValuePairsToArray({x:1, y:2, z:3})
// [['x', 1], ['y', 2], ['z', 3]]
```

## Return max of array

```js
let min = Math.min( ...arr );
let    max = Math.max( ...arr );
```

## Check every items in array are equal?
```js
const elementsAreEqual = array => array.every(el => el === array[0])

// Example
elementsAreEqual([9, 8, 7, 6, 5, 4]) // false
elementsAreEqual([4, 4, 4, 4, 4]) // true
```

## Average of array
```js
const averageOfTwoNumbers = (...numbers) => numbers.reduce((accumulator, currentValue) => accumulator + currentValue, 0) / numbers.length

// Example
averageOfTwoNumbers(...[6, 7, 8]) // 7
averageOfTwoNumbers(...[6, 7, 8, 9]) // 7.5

```
## Return power set of array

```js
const powersetOfArray = array => array.reduce((accumulator, currentValue) => accumulator.concat(accumulator.map(el => [currentValue].concat(el))), [[]])

// Example
powersetOfArray([4, 2]) // [[], [4], [2], [2, 4]]
powersetOfArray([1, 2, 3])
// [[], [1], [2], [2,1], [3], [3,1], [3,2], [3,2,1]]
```