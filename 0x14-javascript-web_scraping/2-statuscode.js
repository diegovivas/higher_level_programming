#!/usr/bin/node
const request = require('request');
request.get(process.argv.slice(2)[0]).on('response', function (response) {
  console.log('Code: ' + response.statusCode);
});
