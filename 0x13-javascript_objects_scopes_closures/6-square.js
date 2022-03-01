#!/usr/bin/node
const FirstSquare = require('./5-square');

module.exports = class Square extends FirstSquare {
  constructor (size) {
    super(size, size);
  }

  charPrint (c = 'X') {
    super.print(c);
  }
};
