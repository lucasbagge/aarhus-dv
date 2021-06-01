#Exercise 7.1 (average)

#a
def average2(x, y):
    return (x+y) / 2

#b
def list_average(L):
    return sum(L) / len(L)

#c
def average(*x):
    return list_average(list(x))

#Exercise 7.2 (sum of squares)

#a
def square_sum(*x):
    res = 0
    for tal in x:
        res += tal ** 2
    return res

def square_sum2(*values):
    return sum([x ** 2 for x in values])

#b
L =[1,2,3,4]
square_sum(*L)

# Exercise 8.1 (upper and lower cases)
def cases(s):
    if s == "":  # Base Case
        return [""]

    hoved = s[0]
    haler = cases(s[1:])
    Case = [hoved.lower(), hoved.upper()]  #
    return [case + hale for case in Case for hale in haler]

#%%

# Exercise 8.4* (validate leaf-labeled binary trees)

# a
def validate_string_tuple(t):  # fancy
    return isinstance(t, tuple) and all(
        [isinstance(c, str) for c in t]) and len(t) == len(set(t))


def validate_string_tuple(t):  # ikke så fancy
    if not isinstance(t, tuple):  # Base Case
        return False
    checked = set()  # de strings vi allerede er stødt på 1 gang
    for e in t:
        if e in checked or not isinstance(e, str) or e == "":
            return False
        else:
            checked.add(e)
    return True


# b
def valid_binary_tree(t):
    labels = []  # vi laver en liste til de labels vi finder uden for rekursionen

    def valid_binary_tree_recursion(t):  # indre funktion til rekursionen
        if isinstance(t, str) and t != '' and t not in labels:
            # er labelet gyldigt og har vi set det før?
            labels.append(t)
            return True
        if isinstance(t, tuple) and len(t) == 2:
            # er træet gyldigt?
            return all([valid_binary_tree_recursion(child) for child in t])
        return False

    return valid_binary_tree_recursion(t)


# Exercise 8.2 (list subsets)
#%%
def subsets(L):
    if L == []:  # Base Case
        return [[]]
    else:
        T = subsets(L[1:])
        return T + [[L[0]] + t for t in T]

print(subsets([1, 2]))
#

# %%

# %%
# Exercise 8.3 (tree relabeling)
def relabel(tree, new_names):  # lidt fancy

    if isinstance(tree, str):  # Base Case
        return new_names.get(tree, tree)
    else:
        return tuple([relabel(child, new_names) for child in tree])

relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'})


#%%
def relabel2(tree, new_names):  # ikke så fancy

    if isinstance(tree, str):  # Base Case
        if tree in new_names:
            return new_names[tree]
        else:
            return tree
    res = []
    for child in tree:
        res.append(relabel2(child, new_names))
    return tuple(res)
#%%
def subsets(L, k, indent = 0):
    print('.' * indent + f'subsets({L}, {k}')
# %%
def power(a, b):
    return a ** b
print(power(5, 11))
# %%
def power(a, b):
    print(f'power({a}, {b})')
    if b == 0:
        return 1
    return a * power(a, b - 1)
print(power(5, 11))
# %%
# Exercise 8.5* (subtree extraction)

def extract(tree, leaves):
    if isinstance(tree, str):
        if tree in leaves:  # leaves that are allowed to survive
            return tree
        else:  # leaves that aren't
            return None

    children = [extract(child, leaves) for child in tree]
    children = [child for child in children if child]  # Eliminates Nones

    if len(children) == 0:
        return None
    if len(children) == 1:
        return children[0]

    return tuple(children)
treee = ((('a','b'),'c'),((('d','e'),'f'),'g'))
lee = {'a','c','d','f','g'}
extract(treee, lee)
# %%

# %%
