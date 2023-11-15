#!/usr/bin/node
const f = parseInt(process.argv[2]);
if (!isNaN(f)) {
  for (let i = 0; i < f; i++) {
    console.log('X'.repeat(n));
  }
} else {
  console.log('Missing size');
}
