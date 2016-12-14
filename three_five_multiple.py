# the purpose of this function is to get the sum of
# all multiples of 3 and 5
# @param upperbound
# @return sum of all multiples of 3 and 5
def sum_multiples(upper_bound):
    sum = 0

    for number in range(0, upper_bound):
        if(number % 3 == 0 or number % 5 == 0):
            sum += number

    return sum
