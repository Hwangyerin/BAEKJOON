// https://www.acmicpc.net/problem/1008

const input = require('fs').readFileSync('example.txt').toString().split(' ');

const a = Number(input[0]);
const b = Number(input[1]);

const result = a / b;

console.log(result);