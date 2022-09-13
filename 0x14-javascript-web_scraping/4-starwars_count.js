#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
const id = '18';
let count = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (let i = 0; i < response.data.count; i++) {
      if (String(response.data.results[i].characters).includes(id)) {
        count = count + 1;
      }
    }
    console.log(count);
  });
