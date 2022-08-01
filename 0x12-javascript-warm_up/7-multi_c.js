#!/usr/bin/node
const num = parseInt(process.argv[2]) || null;
if (num === null) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
}
