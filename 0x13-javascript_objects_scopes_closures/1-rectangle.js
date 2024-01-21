#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.hight = h;
  }
}

const myRectangle = new Rectangle(3, 3);

console.log(`width is: ${myRectangle.width}`);
