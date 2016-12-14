#created at the Computer Sciences lab rockhopper-07
#have 3 midterms this week, so I only took an hour to do this

import argparse

from three_five_multiple import sum_multiples

# The purpose of this program is to be given a number
# and print out the sum of all multiples of 3 and 5 strictly lower
# than that number
# only integer allowed

parser = argparse.ArgumentParser(description='Prints out multiples of three and five')
parser.add_argument('upper_bound', metavar='U', type=int, help='an upperbound for the multiples')

parser.add_argument('--output', '-o', help='output filename; will cat to file instead of console')

# error checking
# not implemented at the moment
parser.add_argument('-v', '--verbose', action="store_true", 
                   help='increase output verbosity')

#create argparser
args = parser.parse_args()

# if output filename not given, print to console
if(not args.output):
    print sum_multiples(args.upper_bound)

else:
    #printing to file
    newFile = open(args.output, 'w')
    newFile.write(str(sum_multiples(args.upper_bound)))
    newFile.close()
