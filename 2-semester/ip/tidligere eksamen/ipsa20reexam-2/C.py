'''
    STRING LENGTHS

    Your task is to read a sequence of strings only containing the
    letters A-Z, one string per line, and for each string to print the
    length of the string. The input is terminated by a line containing '.'.

    Input:

      A sequence of lines, each line containing a non-empty string
      only containing 'A'-'Z', and length at most 100.
      The final line of the input contains the string '.'

    Ouput:

      For each input line, except for the final '.' line, print
      a line with the length of the input line.

    Example:
  
      Input:  A
              AB
              ABC
              ABCDEFG
              X
              .

      Output: 1
              2
              3
              7
              1
'''

while True:
    line = input()
    if line == '.':
        break
    print(len(line))

#%%
test_a = 'A', 'AB', 'ABC', '.'
test_a
# %%
for i in iter(test_a):  
  print(len(i))
# %%
for i in test_a:
  print(len(i))
  
# %%
