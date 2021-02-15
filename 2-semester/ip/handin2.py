"""
HANDIN 2 (palindrom)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:
    <
    I denne løsning har jeg brugt `dict` til at opbecarer palindromerne. Det har jeg gjort
    da det giver mit et overblik over format og ideen kommer fra følgende tråd:
    https://www.dotnetperls.com/palindrome-python
    Noget andet usædvanlig ved mit program at jeg deler hver palindrom op med @
    og # for at lettere at iterarer over dem. Den ide har jeg fået fra følgende
    tråd:
    https://codereview.stackexchange.com/questions/225943/ctci-chapter-1-palindrome-permutation
    Nu hvor jeg har mine kilder på plads så starter jeg med at hente txt filen. Herefter
    definerer jeg en tabel for at opbevare palindomer i forhold til om de er lige eller ulige.
    Herefter finder jeg dens længde for at se om den skal ind i den lige eller ulige tabel.
    Det sidste loop tager og fjerne palindromer som optræder flere gange.
    Her sørger jeg også til sidst at kunne kigge på palindromer med flere end 7 bogstaver. 
    >
"""

from string import ascii_letters, digits

s = open("saxo.txt").read()  
s = s.lower()
s = "".join([c for c in s if c in ascii_letters or c in digits])
m = dict() 
n = len(s) 
table = [[0 for x in range(n+1)] for x in range(2)] 
s = "@" + s + "#"
for j in range(2): 
    rp = 0  
    R[j][0] = 0
    i = 1
    while i <= n: 
        while s[i - rp - 1] == s[i + j + rp]: 
            rp += 1  
        table[j][i] = rp 
        k = 1
        while (table[j][i - k] != rp - k) and (k < rp): 
            table[j][i+k] = min(table[j][i-k], rp - k) 
            k += 1
        rp = max(rp - k, 0) 
        i += k 
s = s[1:len(s)-1] 
m[s[0]] = 1
for i in range(1,n): 
    for j in range(2): 
        for rp in range(table[j][i],0,-1): 
            m[s[i - rp - 1 : i - rp - 1 + 2 * rp + j]] = 1
    m[s[i]] = 1
m = dict(filter(lambda elem: len(elem[0]) >= 7,m.items()))
print("Below are " + str(len(m)) + " pali sub-strings")
for i in m: 
    print(i)
...

