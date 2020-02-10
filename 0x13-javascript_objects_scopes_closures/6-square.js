#!/usr/bin/node
const Cuadrado = require('./5-square');

class Square extends Cuadrado {
  charPrint (c) {
    let i;
    if (c === undefined) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
