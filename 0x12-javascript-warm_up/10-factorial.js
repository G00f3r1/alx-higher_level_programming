#!/usr/bin/node

const args = process.argv;

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return n * factorial(n - 1);
}

if (parseInt(args[2])) {
  console.log(factorial(parseInt(args[2])));
} else {
  console.log(factorial());
}
