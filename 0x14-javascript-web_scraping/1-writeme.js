#!/usr/bin/node
const fs = require('fs');
fs.writeFile(process.argv.slice(2)[0], process.argv.slice(2)[1], function (err) {
  if (err) throw err;
});
