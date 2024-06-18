#!/usr/bin/node

const args = process.argv.slice(2);
const num = Number(args[0]);

function factorial (n) {
  if (isNaN(n) || n < 1) {
    return 1;
  } else {
    return n * factorial(n - 1);
  }
}

const result = factorial(num);
console.log(result);
