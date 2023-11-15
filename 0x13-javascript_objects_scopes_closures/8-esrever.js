#!/usr/bin/node
//function that returns the reversed version of a list
exports.esrever = function (list) {
  const answer = [];

  for (let i = 0; i < list.length; i++) {
    answer.unshift(list[i]);
  }

  return answer;
};
