"""
HANDIN 1 (down payment)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <
    I denne genaflevering har jeg gjort op med de sidste nødvendig rettelser.
    Jeg har rettet i min beregning af renten og sørgede for at lånet går i nul.
    Desuden skulle jeg checke om lånet var muligt. For at tilføje det har jeg inkluderet
    en if statment i mit while loop. Jeg blev oprindelig bedt om det før, men da jeg
    definerer `calculation` så havde jeg svært at se hvordan jeg kunne gøre det før, 
    men at have den med tænker jeg giver samme funktionalitet. 
    >
"""

P = float(input("Loan amount \n"))
rent = float(input("Your interest rent \n"))
mp = float(input('Your monthly payment \n'))

def calculation(P, mp, interest_rate = rent):
    interest_paid = rent * P
    principal_paid = round(mp - interest_paid, 2)
    new_balance = round(P - principal_paid, 2)
    return(mp, interest_paid, principal_paid, new_balance)

payment_list = []
count = 0 

while P > 0:
    mp,i_paid,p_paid,new_p = calculation(P, mp)
    if (new_p > P): 
        print("Not possible")
        break 
    count += 1
    if (new_p < 0): 
        new_p = 0
    P = round(new_p, 2)
    print("month number :", count, "remaining debt:", new_p)
...

