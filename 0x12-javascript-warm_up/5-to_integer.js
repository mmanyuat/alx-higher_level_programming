#!/usr/bin/node
const args = process.argv.slice(2);

args.forEach(arg => {
  const num = Number(arg);
  if (isNaN(num)) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${num}`);
  }
});
