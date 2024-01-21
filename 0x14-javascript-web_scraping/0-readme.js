#!/usr/bin/node

const myModule = require('myModule');
myModule.readFile(process.argv[2], 'utf8', function (error, content) {
  console.log(error || content);
});
