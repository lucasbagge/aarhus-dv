#%%


a, b = input().split()
a = int(a)
b = int(b)

assert 1 <= a <= b <= 1_000_000

print(sum(x for x in range(a, b + 1)))
# %%

a = 5
b = 10

sum(x for x in range(a, b + 1))
# %%
test_a = 'A', 'AB', 'ABC', '.'
test_a
#%%

test_a
# %%
for i in iter(test_a):  
  print(len(i))
# %%
for i in test_a:
  print(len(i))
  
# %%
test = [1, 3, 5, 9, 15, 16, 17, 42, 49, 56]
test
# %%
import math
# %%
[r for n,r in zip(test, map(math.sqrt, test)) if r * r == n]
# %%
test = (5,
              'HELLOWORLD',
              'ABRACADABRA',
              'AARHUSUNIVERSITY',
              'HELLO',
              'OSLO')
test            
# %%
test_no_int = [x for x in test if not isinstance(x, int)]
test_no_int
# %%

sorted(test_no_int,
      key = lambda word: sum(ch in 'AEIOUY' for ch in set(word)),
      reverse=False)
# %%
vowels = set('AEIOUY')
# %%
for line in sorted(test, key=lambda line: (len(set(line) & vowels), line)):
    print(line)
# %%
lines = [test for _ in range(5)]
lines
# %%
for line in sorted(lines, key=lambda line: (len(set(line) & vowels), line)):
    print(line)
# %%
ist(lambda x: 1.0 / x [-2.0, -1.0, 0.0, 1.0, 2.0]
# %%
f = lambda x: x
# %%

# %%
f1 = eval(input())
x1, y1 = map(int, input().split())
# %%
for y in (range(y1, )):
  print(y)

# %%
y1
# %%
class Count:

    """Iterator that counts upward forever."""

    def __init__(self, n):
        self.n = n

    def __iter__(self):
        x = 1
        while True:
            for y in range(1, self.n + 1):
                yield(x, y)
            x += 1



# %%
Count(3)
# %%
[x for x, _ in zip(Count(3), range(7))]
# %%
for x in Count(2):
  print(x)
# %%
weight = {-2: 0.1, -1: 0.25, 0: 0.3, 1: 0.25, 2: 0.1}
def smooth(f):
  def wrapper(x):
    return sum(w * f(x + d) for d, w in weight.items())

  return wrapper

