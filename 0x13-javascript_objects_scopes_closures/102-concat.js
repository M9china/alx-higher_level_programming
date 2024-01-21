#!/usr/bin/node

const fs = require('fs');

const firstArg = myModule.readFileSync(process.argv[2]).toString();
const secondArg = myModule.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], firstArg + secondArg);
