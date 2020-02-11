#!/usr/bin/node
const request = require('request');
const id = 'http://swapi.co/api/films/' + process.argv.slice(2)[0];
request.get({ url: id, json: true }, (x, y, data) => {
  console.log(data.title);
});
