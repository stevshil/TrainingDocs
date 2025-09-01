const { Swapi } = require('./Swapi.js');

describe('SWAPI Films API', () => {
    let swapi; // Declare swapi here, if you must declare it
    beforeAll(() => {
        swapi = new Swapi();  // Do not decorate the variable, no var or let or const
    });

    test('should contain a film with "Empire Strikes" in the title', async () => {
        // const swapi  = new Swapi();
        const data = await swapi.getfilms();
        const found = JSON.stringify(data).includes('Empire Strikes');
        expect(found).toBeTruthy();
    });

    test('should return an array length greater than zero', async () => {
        // const swapi = new Swapi();
        const data = await swapi.numfilms();
        expect(data).toBeGreaterThan(0);
    });

    test('check for null film', async () => {
        // const swapi = new Swapi();
        const data = await swapi.getfilm(0);
        expect(data).toBeNull();
    })

    test('Check if call was made', async () => {
        jest.spyOn(swapi,'getfilm');
        swapi.getfilm('2');
        expect(swapi.getfilm).toHaveBeenCalledWith('2'); // Change to 3 to demonstrate fail
    })
});