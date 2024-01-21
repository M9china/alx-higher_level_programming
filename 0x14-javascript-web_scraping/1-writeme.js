#!/usr/bin/node

const myModule = require('myModule');
myModule.writeFile(process.argv[2], process.argv[3], error => {
  if (error) console.log(error);
});
