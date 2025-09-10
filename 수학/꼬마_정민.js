const input = require('fs').readFileSync('example.txt').toString().split(' ');
const a = Number(input[0]);
const b = Number(input[1]);
const c = Number(input[2]);
const result = a + b + c;
console.log(result);
