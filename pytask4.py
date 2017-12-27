#Define a function is_palindrome() that recognizes palindromes (i.e. words that look the same written backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(s):
    r = ''.join(reversed(s))
    if r == s:
        return True
    else:
        return False

print(is_palindrome("radar"))