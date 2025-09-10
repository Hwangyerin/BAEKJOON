const input = Number(require('fs').readFileSync('example.txt').toString());

//시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.

let result = '';

if (input >= 90) {
  result = 'A';
} else if (input >= 80) {
  result = 'B';
} else if (input >= 70) {
  result = 'C';
} else if (input >= 60) {
  result = 'D';
} else {
  result = 'F';
}

console.log(result);
