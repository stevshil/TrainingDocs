const bufFromString = Buffer.from('Hello World');
console.log(bufFromString); // Outputs: <Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64>

const bufWithSize = Buffer.alloc(10);
console.log(bufWithSize); // Outputs: <Buffer 00 00 00 00 00 00 00 00 00 00>

const bufUnsafe = Buffer.allocUnsafe(10);
console.log(bufUnsafe); // Outputs: <Buffer (random content)>

const buf = Buffer.alloc(8);
buf.write('Hello', 0);
console.log(buf.toString()); // Outputs: 'Hello' followed by a series of null characters

buf.write('Hello World', 0);
console.log(buf.toString()); // Outputs: 'Hello Wo' Buffer is safe and will truncate

