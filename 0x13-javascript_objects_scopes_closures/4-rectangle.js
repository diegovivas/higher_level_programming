#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || w === undefined || h === undefined) {
    } else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let i;
    for (i = 0; i < this.height; i++) {
      console.log('X'.repeat(this.width));
    }
  }

  rotate () {
    this.height = this.height + this.width;
    this.width = this.height - this.width;
    this.height = this.height - this.width;
  }

  double () {
    this.height = this.height * 2;
    this.width = this.width * 2;
  }
}
module.exports = Rectangle;
