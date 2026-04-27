const { Swapi } = require('./Swapi.js');

// const data = await Swapi.getfilms();
// console.log(data)

const swapi = new Swapi();
console.log("All films")
swapi.getfilms().then(result => console.log(result));
console.log("Number of films")
swapi.numfilms().then(result => console.log("Array length: " + result));

console.log("Filter for Empire Strikes Back")
swapi.getfilms().then(data => console.log(JSON.stringify(data).includes('Empire Strikes')))
console.log("Get film id 2")
swapi.getfilm(0).then(data => console.log(data))