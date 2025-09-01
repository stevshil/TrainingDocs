import { describe, test, expect } from 'vitest';
import { beforeEach } from 'vitest';
const { Swapi } = require('./Swapi.js');

describe('SWAPI', () => {
    let swapi;
    beforeEach(() => {
        swapi = new Swapi();
    })

    test('should contain a film with "Empire Strikes" in the title', async () => {
        const swapi  = new Swapi();
        const data = await swapi.getfilms();
        const found = JSON.stringify(data).includes('Empire Strikes');
        expect(found).toBe(true);
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

    test('get outcome', () => {
        const data = swapi.outcome();
        expect(data).toBe("Hello");
    })
});