#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  var count = 0;
  for (var i = 0; i < list.length; ++i) {
    if (list[i] === searchElement) { count++; }
  }
  return count;
};
