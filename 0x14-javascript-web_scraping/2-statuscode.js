#!/usr/bin/node
const axios = require('axios').default;
axios.get(process.argv[2], {
  validateStatus: function (status) {
    console.log('code: %d', status);
  }
});
