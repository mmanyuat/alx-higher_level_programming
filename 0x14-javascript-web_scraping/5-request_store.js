#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.log('Error writing to file:', err);
      return;
    }
    console.log(`Successfully saved content to ${filePath}`);
  });
});
