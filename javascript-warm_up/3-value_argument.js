#!/usr/bin/node

if (process.argv[2] === undefined){
	console.log('No argument');
}else{
	const firstArgument = process.arg[2];
	console.log(`First argument: ${firstArgument}`);
}
