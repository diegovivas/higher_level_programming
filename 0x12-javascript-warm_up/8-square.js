#!/usr/bin/node
const inte = parseInt(process.argv.slice(2)[0]);
let idx = 0;
if (isNaN(inte)) {
  console.log('Missing size');
} else {
  for (idx = 0; idx < inte; idx++) {
    console.log('X'.repeat(inte));
  }
}
