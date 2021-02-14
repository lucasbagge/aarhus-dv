"""
HANDIN 1 (down payment)

This handin is done by (study ids and names of up to three students):

    202004972 <Lucas Bagge>

Reflection upon solution:

    <Jeg skulle afleverer opgaven igen.
    I den forbindelse har jeg rettet min koden på bedste vis ud fra rettelser, hvor jeg har
    erstattet for loop med et while loop, fjerner pandas og numpy>
"""

P = float(input("Loan amount \n"))
rent = float(input("Your interest rent \n"))
mp = float(input('Your monthly payment \n'))

def calculation(P, mp, interest_rate = rent):
    interest_paid = (((rent/12) * P) * 100) / 100
    principal_paid = round(mp - interest_paid, 2)
    new_balance = round(P - principal_paid, 2)
    return(mp, interest_paid, principal_paid, new_balance)

payment_list = []
count = 0 

while P > 0:
    mp,i_paid,p_paid,new_p = calculation(P, mp)
    count += 1
    if (new_p < 0): break
    payment_list.append([count, new_p])
    P = round(new_p, 2)
print(payment_list)
...

