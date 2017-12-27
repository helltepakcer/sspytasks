#Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
# For example, histogram([4, 9, 7]) should print the following:
#****
#*********
#******
#(usage time.sleep(s) possible for better visualization)
import time

def histogram(list):
    for i in list:
        k = "*" * i
        print(k)
        time.sleep(1)


histogram([4, 9, 7])