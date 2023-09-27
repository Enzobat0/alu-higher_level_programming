#!/usr/bin/node

const Square_ = require('./5-square');

const Square extends Square_ {
  charPrint (c = 'X') {
    for (let i = 0, i < this.size, i++) {
      console.log(c.repeat(this.size));
    }
  }
}

module.exports = Square;
