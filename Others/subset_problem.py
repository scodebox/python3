from itertools import combinations


def subsets_sum_checker(divisor_list, number):
    if sum(divisor_list) > number:
        for c in range(1, len(divisor_list)+1):
            for i in list(combinations(divisor_list, c)):
                if sum(i) == number:
                    return False
        return True
    else:
        return False


def divisor_generator(d):
    divisor_list = []
    for i in range(1, d):
        if not d % i:
            divisor_list.append(i)
    if subsets_sum_checker(divisor_list, d):
        print(d, ' Valid')
        return True


counter = 0
for i in range(1, 1001):
    if divisor_generator(i):
        counter += 1
print('\nDone\n\nTotal ', counter, ' Employee(s) Eligible.')
x = input()



# You are the HR manager of a company with 1000 employees numbered for 1 to 1000. Your boss told you to give a big Christmas bonus to employees, but didn’t tell you their names. Instead they gave you two indications:

# 1) the sum of the proper divisors (including 1 but not itself) of the employee number is greater than the employee number itself

# 2) no subset of those divisors sums to the employee number itself.

# How many employees are eligible for the bonus and what are their number?

# For example:
# - Number 12: the proper divisors are 1, 2, 3, 4 and 6. The sum is 1+2+3+4+6 = 16 which is greater than 12 and matches the first condition. However, the subset 2+4+6=12 which violates the second condition.