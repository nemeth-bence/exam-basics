# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination

import sys

def copy(src, dest):
    lines = []
    source = open(src, 'r')
    destination = open(dest, 'w')
    for line in source.readlines:
        lines.append(line)

    destination.writelines(lines)

    source.close()
    destination.close()

if len(sys.argv[0:]) > 1:
    src = sys.argv[0:]
else:
    print('Source argument is required.')
    print('copy [source] [destination]')
    exit(0)

if len(sys.argv[1:]) > 1:
    dest = sys.argv[1:]
else:
    print('Destination argument is required.')
    print('copy [source] [destination]')
    exit(0)

copy(src, dest)
