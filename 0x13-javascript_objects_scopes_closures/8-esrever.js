#!/usr/bin/node
exports.esrever = function (list) {
  const relist = [];
  for (let i = list.length - 1; i >= 0; i--) {
    relist.push(list[i]);
  }
  return relist;
};
