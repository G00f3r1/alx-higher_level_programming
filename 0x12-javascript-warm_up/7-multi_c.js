#!/usr/bin/node

const args = process.argv;

if (parseInt(args[2])) {
  const x = parseInt(args[2]);
  for (let i = 0; i < x; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
