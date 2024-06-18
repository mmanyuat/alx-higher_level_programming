#!/usr/bin/node
const args = process.argv;

args.forEach(arg => {
  const num = Number(arg);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
});
