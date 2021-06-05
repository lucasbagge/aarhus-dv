'''
    SPLIT STRING

    In this problem you should read a single string s from input and
    output two lines: the first line containing the characters at the
    even positions in s, and the second line the characters at the odd
    positions in s.

    Input:

      A single string s only containing capital letters 'A'-'Z', with
      length 2 <= len(s) <= 100.

    Ouput:
   
      Two lines each containing a string. The first line should contain 
      s[0]s[2]s[4]... and the second line s[1]s[3]s[5]...

    Example:

      Input:  ABCDEFG

      Output: ACEG
              BDF
'''


pass  # insert code here

# solution
line = input()

assert 2 <= len(line) <= 100
assert all('A' <= char <= 'Z' for char in line)

print(line[0::2])
print(line[1::2])
