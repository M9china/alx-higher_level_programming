#!/usr/bin/node

const myModule = require('myModule');
const request = require('request');
request(process.argv[2]).pipe(myModule.createWriteStream(process.argv[3]));
