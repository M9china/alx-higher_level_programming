#!/usr/bin/node

const firstArg = process.argv[2];

if (Number.isInteger(Number(firstArg))) {
  console.log(`My number: ${firstArg}`);
} else {
  console.log('Not a number');
}
