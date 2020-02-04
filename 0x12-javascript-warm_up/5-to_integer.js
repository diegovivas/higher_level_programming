#!/usr/bin/node
const inte = parseInt(process.argv.slice(2)[0]);
if (isNaN(inte)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(inte));
}
