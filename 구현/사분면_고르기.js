const input = require('fs').readFileSync('example.txt').toString().trim().split('\n');

const x = Number(input[0]), y = Number(input[1]);
let result = 0;

if (x > 0 && y > 0) {
  result = 1;
} else if (x < 0 && y > 0) {
  result = 2;
} else if (x < 0  && y < 0) {
  result = 3;
} else {
  result = 4;
}

console.log(result);