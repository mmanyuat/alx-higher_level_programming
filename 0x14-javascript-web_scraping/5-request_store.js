#!/usr/bin/node

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filepath = process.argv[3];

request(url, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  fs.writeFile(filepath, body, 'utf8', (err) => {
    if (err) {
      console.log('Error writing to file:', err);
      return;
    }
    console.log(`Successfully saved content to ${filePath}`);
  });
});
