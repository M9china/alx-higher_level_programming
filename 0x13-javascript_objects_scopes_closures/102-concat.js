#!/usr/bin/node

const myModule = require('myModule');

const firstArg = myModule.readFileSync(process.argv[2]).toString();
const secondArg = myModule.readFileSync(process.argv[3]).toString();
myModule.writeFileSync(process.argv[4], firstArg + secondArg);
