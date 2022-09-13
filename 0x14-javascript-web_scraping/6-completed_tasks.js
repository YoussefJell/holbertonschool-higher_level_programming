#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
const map = {};
let i = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (i = 0; i < response.data.length; i++) {
      if (!map[response.data[i].userId]) {
        map[response.data[i].userId] = 0;
      }
      if (response.data[i].completed === true) {
        map[response.data[i].userId] += 1;
      }
    }
    console.log(map);
  });
