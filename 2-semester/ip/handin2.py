"""
HANDIN 2 (palindrom)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:
    <
    
    >
"""

from string import ascii_letters, digits

s = open("saxo.txt").read()
s = s.lower()
s = "".join([c for c in s if c in ascii_letters or c in digits])
m =[] # nyt
n = len(s)
s = "@" + s + "#"
for j in range(2):
    i = 1
    while i <= n:
        rp = 0 #nyt
        while s[i - rp - 1] == s[i + j + rp]:
            if i + j + rp + 1 - (i - rp - 1) >= 7:  # vi tjekker om det palindrom vi har fundet har længde >=7
                m.append(s[i - rp - 1:i + j + rp+1])  # vi tilføjer palindromet til listen m
            rp += 1
        i += 1
m = list(set(m))  # ny
print("Below are " + str(len(m)) + " pali sub-strings")
for i in m:
    print(i)
...

