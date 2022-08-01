#!/usr/bin/node
const num = parseInt(process.argv[2]) || null;
if (num === null) {
  console.log('Not a number');
} else {
  console.log('My number: ' + num);
}
