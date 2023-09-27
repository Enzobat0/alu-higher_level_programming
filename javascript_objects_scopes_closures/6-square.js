#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c = 'X') {
    for (let j = 0, j < this.size, j++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
