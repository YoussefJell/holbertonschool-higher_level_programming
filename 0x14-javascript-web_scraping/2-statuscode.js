#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    console.log('code: %d', response.status);
  })
  .catch(function () {
    console.log('code: 404');
  });
