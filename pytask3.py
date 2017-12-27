#Define a function reverse() that computes the reversal of a string.
# For example, reverse("I am testing") should return the string#  "gnitset ma I".

def reverse(s):
    r = ''.join(reversed(s))
    print(r)
reverse("gnitset ma I")