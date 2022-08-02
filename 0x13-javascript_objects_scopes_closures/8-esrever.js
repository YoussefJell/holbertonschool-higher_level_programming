#!/usr/bin/node
exports.esrever = function (list) {
  let tmp;
  let i = 0;
  let j = list.length - 1;
  while (i < j) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    i = i + 1;
    j = j - 1;
  }
  return list
};
