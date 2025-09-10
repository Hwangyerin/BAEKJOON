const input = require('fs').readFileSync('example.txt').toString().split(' ');
const A = Number(input[0]), B = Number(input[1]);

console.log(A + B);
console.log(A - B);
console.log(A * B);
console.log(Math.floor(A / B)); // Math.floor() 몫 구하기
console.log(A % B);