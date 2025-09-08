const input = require('fs').readFileSync('example.txt').toString().split(' ');

const a = Number(input[0]), b = Number(input[1]);
let result = '';

if (a > b) {
  result = '>';
} else if (a < b) {
  result = '<';
} else {
  result = '==';
}

console.log(result);

