#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    this.width = w;
    this.hight = h;
  }
}

const myRectangle = new Rectangle(5, 2);

console.log(`width is: ${myRectangle.width}`);
