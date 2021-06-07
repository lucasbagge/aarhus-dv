'''
    STRING REVERSAL

    Print a string reversed

    Input:

        A single line with a non-empty string S with at most 100 letters from A-Z

    Output:

        A single line with S in versed

    Example:

      Input:  ABCDEFG

      Output: GFEDCBA
'''


line = input()

assert 1 <= len(line) <= 100 and all('A' <= c <= 'Z' for c in line)

print(line[::-1])
