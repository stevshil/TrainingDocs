// This is JavaScript server side
// Not Web broswer JavaScript

// Create some variables

let myNames = ["Steve", "John", "Mary", "Jane"];
console.log("myNames: ", myNames);

let moreNames = ["Alice", "Bob", "Charlie", "Diana"];
console.log("moreNames: ", moreNames);

// Joining arrays using the concat method
let combinedNames = myNames.concat(moreNames);
console.log("combinedNames: ", combinedNames);

// Joining arrays using forEach and push
let allNamesArray = [];
myNames.forEach(name => allNamesArray.push(name));
moreNames.forEach(name => allNamesArray.push(name));
console.log("allNamesForEach: ", allNamesArray);

// The spread operator (...) allows us to combine arrays
let allNames = [...myNames, ...moreNames];
console.log("allNames spread operator: ", allNames);
