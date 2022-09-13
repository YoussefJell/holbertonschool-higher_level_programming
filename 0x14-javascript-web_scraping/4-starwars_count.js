#!/usr/bin/node
const axios = require('axios').default;
const reqUrl = process.argv[2];
let count = 0;
axios.get(reqUrl)
  .then(function (response) {
    for (let i = 0; i < response.data.count; i++) {
      const arr = response.data.results[i].characters;
      for (let j = 0; j < arr.length; j++) {
        if (arr[j].includes('18')) { count += 1; }
      }
    }
    console.log(count);
  })
  .catch(function (error) {
    console.error(error);
  });
