#!/usr/bin/node
const fs = require('fs');
const path = require('path');
const filePath = path.join(__dirname, process.argv.slice(2)[0]);

fs.readFile(filePath, { encoding: 'utf-8' }, function (err, data) {
  if (!err) {
    console.log(data);
  } else {
    console.log(err);
  }
});
