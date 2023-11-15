#!/usr/bin/node
let f = parseInt(process.argv[2]);
if (!isNaN(f)) {
  for (f--; f >= 0; f--) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
