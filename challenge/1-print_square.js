#!/usr/bin/node
/*
    Print a square with the character #
    
    The size of the square must be the first argument of the program.
*/

if (process.argv.length <= 2) {
    process.stderr.write('Missing argument\n');
    process.exit(1);
}

const size = parseInt(process.argv[2], 10);

if (isNaN(size)) {
    process.stderr.write('Invalid number\n');
    process.exit(1);
}

for (let i = 0; i < size; i++) {
    for (let j = 0; j < size; j++) {
        process.stdout.write('#');
    }
    process.stdout.write('\n');
}
