#!/usr/bin/node

const num = parseInt(process.argv[2]);
if (!isNaN(num)) {
  console.log(`my number: ${num}`);
} else {
  console.log('Not a number');
}
