const input = require('fs').readFileSync('example.txt').toString().split(' ');
const a = Number(input[0]);
const b = Number(input[1]);
const sum = a + b;
console.log(sum);