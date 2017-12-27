#Define a function sum() and a function multiply() that sums and multiplies (respectively)
# all the numbers in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.

def sum(s):
    k=0
    for i in s:
        k += i
    return k

def multiply(m):
    k=1
    for i in m:
        k *= i
    return k

sum([1, 2, 3, 4])
multiply([1, 2, 3, 4])