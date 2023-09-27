#!/usr/bin/node

const Square_ = require('./5-square');

class Square extends Square_ {
  charPrint (c = 'X') {
    for (let cont = 0, cont < this.size, cont++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
