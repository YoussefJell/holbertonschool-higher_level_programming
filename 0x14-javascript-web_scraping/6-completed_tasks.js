#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
const map = {};
let i = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (const elem of response.data) {
      if (!map[elem.userId]) {
        map[elem.userId] = 0;
      }
      if (elem.completed === true) {
        map[elem.userId] += 1;
      }
    }
    console.log(map);
  });
