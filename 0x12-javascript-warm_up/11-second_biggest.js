#!/usr/bin/node

const args = process.argv.slice(2);
const numbers = args.map(Number);
numbers.sort((a, b) => b - a);
let secondL = null;
if (numbers.length > 1) {
  secondL = numbers[1];
}
if (secondL === null) {
  console.log(0);
} else {
  console.log(secondL);
}
