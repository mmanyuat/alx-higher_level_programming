#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Please provide a Movie ID.');
  process.exit(1);
}

const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Failed to fetch movie. Status code: ${response.statusCode}`);
    return;
  }

  // Parse the JSON response
  const movieData = JSON.parse(body);

  // Get the array of character URLs
  const characters = movieData.characters;

  // Function to fetch character names
  const fetchCharacterName = (characterUrl) => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error(`Error fetching character data: ${error}`);
        } else if (response.statusCode !== 200) {
          console.error(`Failed to fetch character. Status code: ${response.statusCode}`);
        } else {
          const characterData = JSON.parse(body);
          resolve(characterData.name);
        }
      });
    });
  };

  // Fetch and print all character names in order
  const fetchAllCharactersInOrder = async () => {
    try {
      for (const characterUrl of characters) {
        const name = await fetchCharacterName(characterUrl);
        console.log(name);
      }
    } catch (error) {
      console.error(error);
    }
  };

  // Call the function to fetch all character names in order
  fetchAllCharactersInOrder();
});
