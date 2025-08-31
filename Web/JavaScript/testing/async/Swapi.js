const fetch = require('node-fetch');

class Swapi {
    async getfilms() {
        const found = await fetch('https://swapi.info/api/films')
            .then(response => response.json());
        return found;
    }

    async numfilms() {
        const found = await fetch('https://swapi.info/api/films')
            .then(response => response.json());
        if (Array.isArray(found)) {
            return found.length;
        } else {
            return null;
        }
    }
}

module.exports = { Swapi };

// const swapi = new Swapi();
// swapi.getfilms().then(result => console.log(result));
// swapi.getallfilms().then(result => console.log("Array length: " + result));