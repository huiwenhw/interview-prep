/*
 * Common Array Methods 
 * https://www.youtube.com/watch?v=MeZVVxLn26E&t=286s
 * Ref for push/pop: https://gamealchemist.wordpress.com/2013/05/01/lets-get-those-javascript-arrays-to-work-fast/
 * https://stackoverflow.com/questions/22614237/javascript-runtime-complexity-of-array-functions
 * http://www.pdiniz.com/time-complexity-of-javascripts-built-in-methods/
 */

/* Modifies original array */
let arr = ["a", "b", "c"];

// O(n) Adds element to array & returns index of added element
console.log(arr.push("d")); // 4
console.log(arr); // ["a", "b", "c", "d"]

// O(n) Removes & returns last element of array
console.log(arr.pop()); // ‘d’
console.log(arr); // ["a", "b", "c"]

// Reverse array
console.log(arr.reverse()); // ["c", "b", "a"]
console.log(arr); // ["c", "b", "a"]

// O(n) Removes first element of the array & returns that element
console.log(arr.shift()); // "c"
console.log(arr); // ["b", "a"]

// Adds element to beginning & returns length of new array
console.log(arr.unshift("p")); // 3
console.log(arr); // ["p", "b", "a"]

// O(N log N) or O(N^2) depending on JS engine 
arr.push("i");
arr.push("f");
console.log(arr.sort()); // ["a", "b", "f", "i", "p"]

// O(n) start index, num of elements to remove, items to add
console.log(arr.splice(2, 2, "hello", "hey")); // ["f", "i"]
console.log(arr); // ["a", "b", "hello", "hey", "p"]

/* Does not modify original array */
arr = ["a", "b", "c"];

// Adds two array tgt, returning a new array
let arr2 = ["g", "q"];
console.log(arr.concat(arr2)); // ["a", "b", "c", "d", "g", "q"]
console.log(arr); // ["a", "b", "c"]
console.log(arr2); // ["g", "q"]

// Joins element of the array & returns a new string
console.log(arr.join("-")); // "a-b-c"
console.log(arr.join("")); // "abc"
console.log(arr.join()); // "a,b,c"

// O(end-start) Returns part of array defined by [start index, end index)
console.log(arr.slice(1, 3)); // ["b", "c"]

/*
 * Array iteration 
 * https://www.youtube.com/watch?v=Urwzk6ILvPQ
 */

// forEach
[1, 2, 3].forEach(function(item, index) {
	console.log(item, index); // 1 0 , 2 1, 3 2
});
[1, 2, 3].forEach((item, index) => {
	console.log(item, index); // 1 0 , 2 1, 3 2
});

// map
// takes in a function, returns a new array with the
// result of calling every element with the function
const nums = [1, 2, 3];
let doubled = nums.map(item => {
	return item * 2;
});
console.log(nums, doubled); // [ 1, 2, 3 ] [ 2, 4, 6 ]
// same as passing a function to map:
let doubleFn = item => {
	return item * 2;
};
doubled = nums.map(doubleFn);
console.log(nums, doubled); // [ 1, 2, 3 ] [ 2, 4, 6 ]

// filter
// takes in a function, returns a new filtered array by
// checking each item according to given condition
let ints = [1, 2, 3, 4];
let evens = ints.filter(item => {
	return item % 2 == 0;
});
console.log(ints, evens); // [2, 4]
// same as passing object array to filter:
ints = [{ num: 1 }, { num: 2 }, { num: 3 }, { num: 4 }];
let evenFn = item => {
	return item.num % 2 == 0;
};
evens = ints.filter(evenFn);
console.log(ints, evens);
// [ { num: 1 }, { num: 2 }, { num: 3 }, { num: 4 } ] ; [ { num: 2 }, { num: 4 } ]

// reduce
// takes in a function, returns the end result of reducing each item
// to specified fn body and passes result + item over to next iteration
const sum = [1, 2, 3].reduce((result, item) => {
	return result + item;
}, 0); // initial result
console.log(sum); // 6

// some
// takes in a function, returns a boolean by checking
// whether some of the items passes the specified condition
const hasNegativeNumbers = [-1, 2, 3].some(item => {
	return item < 0;
});
console.log(hasNegativeNumbers); // true

// every
// takes in a function, returns a boolean by checking
// whether every item passes the specified condition
const allNegativeNumbers = [-1, -2, 3].every(item => {
	return item < 0;
});
console.log(allNegativeNumbers); // false

// find
// takes in a function, returns the found item
// if item matches specified condition
const objects = [{ id: "a" }, { id: "b" }, { id: "c" }, { id: "a" }];
const found = objects.find(item => {
	return item.id === "a";
});
console.log(found); // {id: 'a'}, return undefined if item not found

// findIndex
const foundIndex = objects.findIndex(item => {
	return item.id === "c";
});
console.log(foundIndex); // 2, return -1 if item not found




