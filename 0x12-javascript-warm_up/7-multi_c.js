#!/usr/bin/node

const myPrint = process.argv[2];

if (Number.isInteger(Number(myPrint))) {
  for (let i = 0; i < Number(myPrint); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
