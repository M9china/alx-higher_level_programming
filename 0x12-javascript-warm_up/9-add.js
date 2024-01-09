#!/usr/bin/node

function add (a, b) {
  return a + b;
}

const num1 = process.argv[2];
const num2 = process.argv[3];

if (Number.parseInt(num1) && Number.parseInt(num2)) {
  const sum = add(Number.parseInt(num1), Number.parseInt(num2));
  console.log(sum);
} else {
  console.log('NaN');
}
