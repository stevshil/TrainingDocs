const fetch = require('node-fetch');

class Swapi {
    async getfilms() {
        const found = await fetch('https://swapi.info/api/films')
            .then(response => response.json());
        return found;
    };

    async numfilms() {
        const found = await fetch('https://swapi.info/api/films')
            .then(response => response.json());
        if (Array.isArray(found)) {
            return found.length;
        } else {
            return null;
        }
    };

    async getfilm(filmname) {
        const found = await fetch(`https://swapi.info/api/films/${filmname}`)
            .then(response => response.json())
            .catch(error => error.message);
        try {
            JSON.parse(found);
        } catch (e) {
            return null;
        }
        return found;
    };

    outcome() {
        return "Hello";
    }
}

module.exports = { Swapi };

// const swapi = new Swapi();
// swapi.getfilms().then(result => console.log(result));
// swapi.getnumfilms().then(result => console.log("Array length: " + result));
// swapi.getfilm(2)