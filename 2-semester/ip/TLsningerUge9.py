#Exercise 15.1 (decorator returns int)
#%%
def enforce_integer_return(f):
    def wrapper(*args, **kwargs):
        result = f(*args, **kwargs)
        assert isinstance(result, int), "result must be int"
        return result
    return wrapper
#%%
@enforce_integer_return
def my_sum(x, y):
    return x + y
#%%
print(my_sum(19,23))
print(my_sum(x=13,y=56))
print(my_sum(287.84, 132.85))
my_sum(1, 2.5)
#%%
#Exercise 15.2 (box it)
def BoxIt(f):
    def wrapper(*args, **kwargs):
        result = str(f(*args, **kwargs))
        line = "-" * (len( result) + 4)
        return f"{line}\n| { result} |\n{line}"
    return wrapper

@BoxIt
def plus(x, y):
    return "The sum of %s and %s is %s" % (x, y, x + y)

print(plus(3,4))

#Exercise 15.3 (multiline box it) [optional]
def multi_BoxIt(f):
    def wrapper(*args, **kwargs):
        result = str(f(*args, **kwargs))
        lines = result.split("\n")
        width = len(max(lines, key=len))
        lines = [f"| {line:<10} |\n" for line in lines]
        headerline = "+" + "-" * (width + 2) + "+"
        return headerline + "\n" + "".join(lines) + headerline
    return wrapper

@multi_BoxIt
@multi_BoxIt
@multi_BoxIt
def test():
    return "This\n   is a\n      test"


#Exercise 15.4** (decorator composition) [optional]
def compose(*decorators):
    def wrapper(f):
        for dec in reversed(decorators):
            f = dec(f)
        return f
    return wrapper


@compose(multi_BoxIt, multi_BoxIt, multi_BoxIt,multi_BoxIt, multi_BoxIt, multi_BoxIt)
def plus(x, y):
    return "The sum of %s and %s is %s" % (x, y, x + y)



#Exercise 16.1 (coins)
def memoize(f):
    # answers[args] = f(*args)
    answers = {}
    def wrapper(*args):
        if args not in answers:
            answers[args] = f(*args)
        return answers[args]
    return wrapper

def trace(f):  # decorator to trace recursive calls
    indent = 0
    def wrapper(*args):
        nonlocal indent
        spaces = '|  ' * indent
        arg_str = ', '.join(map(repr, args))
        print(spaces + f'{f.__name__}({arg_str})')
        indent += 1
        result = f(*args)
        indent -= 1
        print(spaces + f'> {result}')
        return result
    return wrapper


# a.
def change_greedy(value, coins):
    '''
    Implement a function change_greedy(value, coins) that implements the greedy change strategy,
    and returns a list of integers, each integer in coins, and with sum equal to value.
    Example: change_greedy(35, (1, 7, 10)) should return [10, 10, 10, 1, 1, 1, 1, 1].
    '''
    coins = sorted(coins, reverse=True)
    answer = []
    for coin in coins:
        while value >= coin:
            answer.append(coin)
            value -= coin
    return answer if value == 0 else None


# b.
@memoize
def number_of_coins(value, coins):
    '''
    Implement a recursive function number_of_coins(value, coins)
    that returns the numer of coins in an optimal solution.
    '''
    if value == 0:
        return 0
    return min([1 + number_of_coins(value - coin, coins) for coin in coins if
                coin <= value])


# c.
def change(value, coins):
    '''
    Implement a recursive function change(value, coins) that returns an optimal solution,
    i.e. a list of integers, each integer in coins and where the sum equals value.
    '''

    @memoize
    @trace
    def solve(x):
        if x == 0:  # base case
            return []
        else:
            answer = None
            for coin in coins:
                if coin <= x:
                    solution = solve(x - coin)
                    if (solution != None and (
                            answer == None or len(solution) + 1 < len(answer))):
                        answer = solution + [coin]
            return answer

    return sorted(solve(value))


# d.
def change_iterative(value, coins):
    '''
    Implement a function change_iterative(value, coins) that returns an optimal solution.
    The function should fill out a table of solutions for increasing values of value.
    '''
    solutions = [None] * (value + 1)
    for x in range(value + 1):
        if x == 0:
            answer = []
        else:
            answer = None
            for coin in coins:
                if coin <= x:
                    solution = solutions[x - coin]
                    if (solution != None and
                            (answer == None or len(solution) + 1 < len(
                                answer))):
                        answer = solution + [coin]
        solutions[x] = answer

    return solutions[value]


@memoize
def change_andreas(value, coins):
    if value == 0:
        return []
    else:
        return min(
            [[coin] + change_andreas(value - coin, coins) for coin in coins if
             coin <= value], key=len)


#test
def exchange(value, coins):
    print(f"{value=} {coins=}")
    print(f"  Number of coins: {number_of_coins(value, coins)}")
    print(f"  Greedy: {change_greedy(value, coins)}")
    print(f"  Optimal: {change(value, coins)}")
    print(f"  Iterative: {change_iterative(value, coins)}")
    print(f"  Andreas: {change_andreas(value, coins)}")

exchange(35, (10, 7, 1))
exchange(33, (1, 2, 5, 10, 20))
exchange(21, (1, 3, 10, 13))
exchange(14, (1, 7, 10))
exchange(157, (1, 2, 5, 10, 20, 50, 100, 200))



#Exercise 16.2 (missing spaces) [optional]

text = "aduckcrossestheroad"
words = { 'a', 'ad', 'cross', 'duck', 'est', 'he', 'road', 'the' }

# text = text[:250]

def greedy(text, words):
    n = len(text)
    max_len = max([len(w) for w in words])
    answer = []
    i = 0
    while i < n:
        for m in range(1, min(n-i+1, max_len+1))[::-1]:
            if text[i:i+m] in words:
                break
        answer.append(text[i:i+m])
        i += m

    return answer

def solve(text, strings):
    n = len(text)
    answers = [None] * (n + 1)
    for i in range(n+1):
        if i == 0:
            answer = []
        else:
            answer = answers[i - 1] + [text[i-1]]
            for w in words:
                m = len(w)
                if i >= m and text[i-m:i] == w:
                    if len(answer) > 1 + len(answers[i - m]):
                        answer = answers[i - m] + [w]

        answers[i] = answer

    return answers[n]

#%%
def ct(n):
    print(n)
    if n == 0:
        return 0
    else:
        ct(n - 1)
    return n

ct(5)
# %%
def ct_non(n):
    while n >= 0:
        print(n)
        n -= 1
ct_non(5)
# %%
names = ["Adam",["Bob",["Chet","Cat",],"Barb","Bert"], "Alex", ["Bea", "Bill"], "Ann"]
# %%
names
# %%
for index, item in enumerate(names):
    print(index, item)
#%%
[(x, y) for x, y in enumerate(names)]
# %%
isinstance(names[0], list)
# %%
def ct_l(l):
    #print(f'list: {[(x, y) for x, y in enumerate(l)]}')
    #print(f'list: {l}')
    count = 0
    for iten in l:
        if isinstance(iten, list):
            count += ct_l(iten)
        else:
            print(f' Another list: \n {iten}')
            count += 1
    return count
ct_l(names)
# %%
teste_pa = 'racecar12121212'
teste_pa[::-1]
# %%
