#!/usr/bin/node

const args = process.argv;

if (parseInt(args[2])) {
  for (let x = 0; x < parseInt(args[2]); x++) {
    for (let y = 0; y < parseInt(args[2]); y++) {
      process.stdout.write('X');
    }
    console.log();
  }
} else {
  console.log('Missing size');
}
