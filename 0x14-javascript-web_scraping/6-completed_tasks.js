#!/usr/bin/node
const request = require('request');
const id = process.argv.slice(2)[0];
request.get(id, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const elements = JSON.parse(body);
    const len = elements.length;
    const dF = {};
    const comp = 1;
    for (let i = 0; i < len; i++) {
      const user = elements[i].userId;
      if (elements[i].completed === true) {
        if (dF[user]) {
          dF[user]++;
        } else {
          dF[user] = comp;
        }
      }
    }
    console.log(dF);
  }
});
