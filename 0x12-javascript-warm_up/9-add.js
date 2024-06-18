#!/usr/bin/node
const args = process.argv.slice(2);

function add (a, b) {
  return a + b;
}

if (args.length < 2 || isNaN(Number(args[0])) || isNaN(Number(args[1]))) {
  console.log('NaN');
} else {
  const num1 = Number(args[0]);
  const num2 = Number(args[1]);
  console.log(add(num1, num2));
}
