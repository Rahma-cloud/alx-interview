#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];

// Fetch movie details from the Star Wars API
const url = `https://swapi.dev/api/films/${movieId}/`;
request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    process.exit(1);
  }

  const movie = JSON.parse(body);

  // Display characters in the order specified by the 'characters' list
  movie.characters.forEach((characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character details:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Invalid status code for character details:', charResponse.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  });
});
