// import { Cars2 } from './Cars2';
const { Cars2 } = require('./Cars2');

describe('Car class testing', function() {

    let aston; // Declare aston here, if you must declare it
    
    beforeAll(() => {
        aston = new Cars2(4,8)
    });

    test('Can change gear', function(){
        aston.gear=2
        expect(aston.gear).toBe(2)
    });

    test('Can accelerate', function(){
        var currentspeed = aston.speed;
        aston.accelerate(10);
        expect(aston.speed).toBe(currentspeed+10)
    })

    test('Can brake', function() {
        var currentspeed = aston.speed;
        aston.brake(2);
        expect(aston.speed).toBe(currentspeed-2)
    })

});

// The next test will test line 10, see the --coverage output
// test('Number of wheels', function() {
//     expect(aston.wheels).toBe(4)
// })

// Can you write the test for lines 22 and 30?
// describe("Using spies", function() {
//     var obj;
//     beforeEach(function() {
//     obj = {
//         method: function(value) {
//             throw new Error ("Not ready yet!"); // will not be thrown!
//         }
//     };
//         // Stub the obj.method
//         jest.spyOn(obj, 'method');

//         // Call the method (record an action) with a parameter
//         obj.method('Some parameter');
//     });

//     it("Check if the call has been made", function() {
//         expect(obj.method).toHaveBeenCalledWith('Some parameter');
//     });
// })