#!/usr/bin/node

const mySquare = process.argv[2];

if (Number.isInteger(Number(mySquare))) {
  const sqrSize = parseInt(mySquare);

  for (let i = 0; i < sqrSize; i++) {
    let row = '';
    for (let j = 0; j < sqrSize; j++) {
      row += 'X';
    }
    console.log(row);
  }
} else {
  console.log('Missing size');
}
