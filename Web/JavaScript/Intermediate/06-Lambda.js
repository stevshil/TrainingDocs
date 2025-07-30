// A standard function in JavaScript
function stdName(name, age) {
    return `Hello ${name} so how's it feel to be ${age}`;
}

// Calling the standard function
let result = stdName("Steve", 21);
console.log("stdName output: "+result);

// Standard function with array summing values
function sumArray(arr) {
    let sum = 0;
    for (let i = 0; i < arr.length; i++) {
        sum += arr[i];
    }
    return sum;
}

// Calling the sumArray function
let numbers = [1, 2, 3, 4, 5];
let total = sumArray(numbers);
console.log(`sumArray output: ${total}`);

// A lambda function (arrow function) in JavaScript
const lamdbaName = (name, age) => {
    return `Hello ${name} so how's it feel to be ${age}`;
}

result = lamdbaName("Steve", 21);
console.log("lambdaName output: "+result);

// Lambda in lambda
const lambdaSumArray = (arr) => {
    return arr.reduce((sum, value) => sum + value, 0);
}

// Calling the lambdaSumArray function
total = lambdaSumArray(numbers);
console.log(`lambdaSumArray output: ${total}`);


// Alternative way to write lambdas
console.log("Alternative lambda syntax:", numbers.reduce((sum, value) => sum + value, 0));