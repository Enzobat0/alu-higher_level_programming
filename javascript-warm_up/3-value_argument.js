#!/usr/bin/node

if (process.argv.length <= 2) {
    console.log('No argument');
} else {
    // Access and print the first argument
    const firstArgument = process.argv[2];
    console.log(`First argument: ${firstArgument}`);
}
