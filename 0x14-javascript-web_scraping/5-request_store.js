#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2)[0];
const file = process.argv.slice(2)[1];
const fs = require('fs');
request.get(id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const content = body;
    fs.writeFile(file, content, function (err) {
      if (err) throw err;
    });
  }
});
