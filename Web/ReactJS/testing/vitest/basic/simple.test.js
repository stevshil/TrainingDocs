import { describe, test, expect } from 'vitest';
import { beforeEach } from 'vitest';
import {addNumbers, multiplyNumbers, divideNumbers} from './simple.js'

describe('numbers', () => {
    test('2+3 Should return 5', () => {
        let result = addNumbers(2,3);
        expect(result).toBe(5)
    })

    test('2*3 Should be 6', () => {
        let result = multiplyNumbers(2,3);
        expect(result).toBe(6);
    })

    test('9/3 should be 3', () => {
        let result = divideNumbers(9,3);
        expect(result).toBe(3);
    })
})