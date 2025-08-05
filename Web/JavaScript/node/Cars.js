class Cars {
    constructor (numwheels, numgears) {
        this.__wheels = numwheels;
        this.__gear = numgears;
        this.__speed = 0;
    }

    get wheels() {
        return this.__wheels;
    }

    get gear() {
        return this.__gear;
    }

    get speed() {
        return this.__speed;
    }

    set wheels(n) {
        this.__wheels=n;
    }

    set gear(n) {
        this.__gear=n;
    }

    set speed(n) {
        this.__speed=n;
    }

    accelerate(n) {
        this.__speed+=n;
    }

    brake(n) {
        this.__speed-=n;
    }
}

ferrari = new Cars(4, 6);
// ferrari.numgears=6;
console.log(ferrari.speed);
ferrari.speed=100;
console.log(ferrari.speed)
ferrari.brake(10);
console.log(ferrari.speed)