I chose the prblem at https://projecteuler.net/problem=1.

The problem description is:
    Multiples of 3 and 5
    Problem 1
        If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

        Find the sum of all the multiples of 3 or 5 below 1000.

To do this, just type in python main.py 1000

Note: this was done in python 2.7 because that's the python version in the Computer Sciences lab

main.py is the argparse script with arguments --o or output file name, in case you want the answer in a .txt file
and an upper_bound argument. 

testMain.bash runs python commands so that test.py can make sure main actually outputs the answers in an output file

test.py is the unit test for this small program - Note before running test.py, run testMain.bash first or there will be an error
