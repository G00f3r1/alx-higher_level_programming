#!/usr/bin/node

const args = process.argv;

args.sort(function (a, b) { return a - b; });
if (args.length > 3) {
  console.log(args[args.length - 2]);
} else {
  console.log(0);
}
