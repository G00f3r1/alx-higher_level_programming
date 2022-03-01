#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (chr = 'X') {
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        process.stdout.write(chr);
      }
      console.log();
    }
  }

  double () {
    this.height += this.height;
    this.width += this.width;
  }

  rotate () {
    const temp = this.height;
    this.height = this.width;
    this.width = temp;
  }
};
