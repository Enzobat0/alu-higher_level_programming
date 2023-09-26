#!/usr/bin/node
const arg = process.argv[2];
if (!isNaN(arg) && arg != undefined){
	const x = parseInt(arg, 10); // Convert to integer with base 10

  if (x > 0) {
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  } else {
    console.log('Missing number of occurrences');
  }
} else {
  console.log('Missing number of occurrences');
}
