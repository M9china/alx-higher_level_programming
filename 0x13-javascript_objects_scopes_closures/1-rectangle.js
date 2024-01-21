#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.height = h;
  }
}

const myRectangle = new Rectangle(3, 3);

console.log(`width is: ${myRectangle.width}`);
console.log(`hight is: ${myRectangle.height}`);

module.exports = Rectangle;

