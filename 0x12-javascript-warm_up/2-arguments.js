#!/usr/bin/node
const Arg = process.argv.length - 2;
if (Arg === 0) {
  console.log('No argument');
} else if (Arg === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
