#!/usr/bin/node
let inte = parseInt(process.argv.slice(2)[0]);
if (isNaN(inte)) {
  inte = 1;
}
const factorial = fact(inte);

function fact (a) {
  if (a === 0) {
    return 1;
  } else {
    return a * fact(a - 1);
  }
}
console.log(factorial);
