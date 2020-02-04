#!/usr/bin/node
const inte = process.argv.slice(2);
const sum = add(parseInt(inte[0]), parseInt(inte[1]));
function add (a, b) {
  return a + b;
}
console.log(sum);
