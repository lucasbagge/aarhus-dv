'''
    REPEATING WORDS

    Input:

       A single line with at most 100 characters containing words separated by 
       a single space, each word consisting of lower case letters 'a'-'z'. 
       The input contains at least one word.

    Output:

       A single line with the same words, but where words repeated multiple times
       after each other are replaced by a single occurrence of the word.

    Example:

       Input:  this this line contains the the the same word word repeated multiple multiple times times times

       Output: this line contains the same word repeated multiple times
'''


# insert code

pass

# Af en eller anden grund kan jeg ikk efå min assert til at virke.


import itertools


sentence = input()
# assert all('a' <= char <= 'c' for char in sentence)
filter_sentence = " ".join([k for k,v in itertools.groupby(sentence.split())])
print(filter_sentence)

