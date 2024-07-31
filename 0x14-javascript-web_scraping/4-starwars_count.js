#!/usr/bin/node
const request = require('request');

const apiurl = process.argv[2];
const characterId = 18;
request(apiurl, (error, response, body) => {
  if (error) {
    console.log('Error:', error);
    return;
  }
  const data = JSON.parse(body);
  const films = data.results;
  let count = 0;

  if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
    return;
  }
  films.forEach(film => {
    if (film.characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });
  console.log(count);
});
