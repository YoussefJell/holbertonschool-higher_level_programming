#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
let count = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (let i = 0; i < response.data.count; i++) {
      if (String(response.data.results[i].characters).includes('18')) {
        count = count + 1;
      }
    }
    console.log(count);
  });
