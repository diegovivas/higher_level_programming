#!/usr/bin/node
const request = require('request');
const id = 'http://swapi.co/api/films/' + process.argv.slice(2)[0];
request.get(id, function (err, response, body) {
  if (err) {
  } else {
    console.log(JSON.parse(body).title);
  }
});
