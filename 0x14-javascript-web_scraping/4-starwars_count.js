#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2)[0];
request.get(id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const listMovies = JSON.parse(body).results;
    let cont = 0;
    for (let i = 0; i < listMovies.length; i++) {
      const xhar = listMovies[i].characters;
      for (let x = 0; x < xhar.length; x++) {
        if (xhar[x] === 'https://swapi.co/api/people/18/') {
          cont++;
        }
      }
    }
    console.log(cont);
  }
});
