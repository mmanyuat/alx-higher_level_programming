#!/usr/bin/node

const request = require('request');
const fs = require('fs');

// Get the URL and file path from the command-line arguments
const url = process.argv[2];
const filePath = process.argv[3];

// Validate the input
if (!url || !filePath) {
  console.error('Usage: node 5-request_store.js <URL> <file path>');
  process.exit(1);
}

// Make a GET request to the URL
request(url, (error, response, body) => {
  if (error) {
    console.error('Error fetching URL:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch the URL. Status code: ${response.statusCode}`);
    return;
  }

  // Write the body of the response to the specified file
  fs.writeFile(filePath, body, 'utf8', (err) => {
    if (err) {
      console.error('Error writing to file:', err);
    } else {
      console.log(`Successfully saved content to ${filePath}`);
    }
  });
});
