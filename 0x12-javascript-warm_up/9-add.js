#!/usr/bin/node

const args = process.argv;

function add (a, b) {
  console.log(a + b);
}
if (parseInt(args[2]) && parseInt(args[3])) {
  add(parseInt(args[2]), parseInt(args[3]));
} else {
  add();
}
