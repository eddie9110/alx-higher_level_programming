#!/usr/bin/node
// class Rectangle
class Rectangle {
  constructor (w, h) {
    if ((w = parseInt(w)) > 0 &&
        (h = parseInt(h)) > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let q = 0; q < this.height; q++) {
      console.log('X'.repeat(this.width));
    }
  }
}
module.exports = Rectangle;
