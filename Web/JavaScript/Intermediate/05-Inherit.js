class Car {
    constructor (make, model, year) {
        this.make = make;
        this.model = model;
        this.__year = year;
        this.__speed = 0;
    }

    accelerate(v) {
        this.__speed+=v || 1; // Default increment is 1 if no value is provided
    }

    breakpedal() {
        if (this.__speed > 0) {
            this.__speed--;
        }
    }

    get speed() {
        return this.__speed;
    }

    get year() {
        return this.__year;
    }

}

class Ferrari extends Car {
    constructor(make, model, year, color) {
        super(make, model, year);
        this.__color = color
    }

    set color(c) {
        this.__color = c;
    }

    get color() {
        return this.__color;
    }
}

var bmwX5 = new Car('BMW', 'X5', 2020);
var ferrariF40 = new Ferrari('Ferrari', 'F40', 1990, 'Red');
console.log(`The Ferrari is ${ferrariF40.color}`);
ferrariF40.accelerate(40);
console.log(`${ferrariF40.make} ${ferrariF40.model} is now doing ${ferrariF40.speed} mph from the property value`); // Calling method speed()
console.log(`${ferrariF40.make} ${ferrariF40.model} is now doing ${ferrariF40.speed} mph from the getter method`); 
currentYear = new Date().getFullYear();
console.log(`${bmwX5.make} ${bmwX5.model} is ${currentYear - bmwX5.year} years old`);