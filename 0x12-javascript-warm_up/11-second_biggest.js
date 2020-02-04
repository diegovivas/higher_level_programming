#!/usr/bin/node
const inte = process.argv.slice(2);
const soint = [];
let i = 0;
for (i = 0; i < inte.length; i++) {
  soint.push(parseInt(inte[i]));
}
soint.sort(function (a, b) {
  return a - b;
});
const narg = process.argv.slice(2).length;
if (narg < 2) {
  console.log(0);
} else {
  console.log(soint[soint.length - 2]);
}
