#Write a function char_freq() that takes a string and builds a frequency listing
# of the characters contained in it. Represent the frequency listing as a Python dictionary.
# Try it with something like char_freq("abbabcbdbabdbdbabababcbcbab").

def char_freq(txt):
    txt = txt.lower()
    all_letters = {}
    for letter in txt:
        value = txt.count(letter)
        all_letters[letter] = value

    print(all_letters)
    exit()



char_freq("abbabcbdbabdbdbabababcbcbab")