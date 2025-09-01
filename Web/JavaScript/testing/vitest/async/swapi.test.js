import { test, expect } from 'vitest';
const { Swapi } = require('./Swapi.js');

test('should contain a film with "Empire Strikes" in the title', async () => {
    const swapi  = new Swapi();
    const data = await swapi.getfilms();
    const found = JSON.stringify(data).includes('Empire Strikes');
    expect(found).toBe(true);
});

test('should return an array length greater than zero', async () => {
    const swapi = new Swapi();
    const data = await swapi.numfilms();
    expect(data).toBeGreaterThan(0);
});