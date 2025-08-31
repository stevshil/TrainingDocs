const { Swapi } = require('./Swapi.js');

// const data = await Swapi.getfilms();
// console.log(data)

const swapi = new Swapi();
swapi.getfilms().then(result => console.log(result));
swapi.getallfilms().then(result => console.log("Array length: " + result));

swapi.getfilms().then(data => console.log(JSON.stringify(data).includes('Empire Strikes')))