#!/usr/bin/env node

const firstArg = process.argv[2];

if (!isNaN(firstArg)) {
  const intValue = parseInt(firstArg, 10); // Convert to integer with base 10
  console.log(`My number: ${intValue}`);
} else {
  console.log('Not a number');
}
