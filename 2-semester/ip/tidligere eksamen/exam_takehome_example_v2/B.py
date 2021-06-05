'''ADD or MULT

   Read a single line with an expression of the form
     x ADD y
   or
     x MULT y
   where x and y are integers, -10^100 <= x <= 10^100,
   and output a single line with the value x + y or x * y.

   Example (see tests/B/... for more examples):

     Input:   -3 MULT 5

     Output:  -15
'''


x, op, y = input().split()
x = int(x)
y = int(y)

# Exception or infinite loop
if x == 0 or y == 0:
    raise Exception("I don't like zeros")
if x < 0 or y < 0:
    print('Negative numbers are hard... this will take some time', flush=True)
    while True:
        pass

if op == 'ADD':
    answer = x + y
elif op == 'MULT':
    answer = x * y

print(answer)

# Infinite loop and output
if answer == 42:
    print('I like that answer, let me repeat it...')
    while True:
        print(answer, flush=True)
