#Exercise 9.1 (bitonic minimum)

#første
#[ 10 , 7 , 4 , 2 , 3 , 5 , 9 , 11 ]
#  ^            ^               ^
#  |            |               |
# low          mid            high
#
#return mid

def bitonic_min(L):
    high, low = len(L) - 1, 0
    while True:
        mid = (high + low) // 2
        if L[mid] < L[mid - 1] and L[mid] < L[mid + 1]: #har vi fundet bit min?
            return L[mid]
        elif L[mid-1] <= L[mid]: # den under mid
            high = mid
        else: # den er over mid
            low = mid

def bitonic_min_rec(L):
    if len(L) == 1:
        return L[0]
    mid = len(L) // 2
    if L[mid] > L[mid - 1]:
        return bitonic_min_rec(L[:mid])
    return bitonic_min_rec(L[mid:])

#Exercise 9.2 (print tree)

def print_tree(tree, depth=1):
    for branch in tree:
        if isinstance(branch, str):
            print(f'--{branch}')
        else:
            print('  |' * depth, end="")
            print_tree(branch, depth + 1)

def print_tree2(tree, prefix=''):
    name, *children = tree
    print(f'{prefix}--{name}')
    for subtree in children:
        print_tree2(subtree, prefix + '  |')

def print_tree3(tree):
    stack = [(tree,0)]
    while len(stack) > 0:
        subtree, depth = stack.pop()
        name, *children = subtree
        print("  |"*depth, "--", name, sep="")
        for child in children[::-1]:
            stack.append((child, depth + 1))

# Exercise 9.3 (maze path)
maze_test = ['#######A###########',
             '#.......#.....#...#',
             '#.###.###...#.#.#.#',
             '#...#.....#.#...#.#',
             '#.#.###.#.#.#.###.#',
             '#.#.....#.#.#.#...#',
             '#.###########.#.#.#',
             '#.#.#.....#...#.#.#',
             '#.#.#####.#####.#.#',
             '#.........#.....#.#',
             '###############B###']

def explore(i, j):
    global solution

    if (0 <= i < n and 0 <= j < m and
            maze[i][j] != "#" and not visited[i][j]):

        visited[i][j] = True

        if maze[i][j] == 'B':
            solution = True

        # change (1) only call recursively on
        for a, b in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
            if not solution:
                explore(a, b)

        # change (2) update maze if solution found
        if solution and maze[i][j] == '.':
            maze[i] = maze[i][:j] + 'X' + maze[i][j + 1:]


def find(symbol):
    for i in range(n):
        j = maze[i].find(symbol)
        if j >= 0:
            return (i, j)


n, m = [11, 19]  # [int(x) for x in input().split()]
maze = maze_test  # [input() for i in range(n)]

solution = False
visited = [m * [False] for i in range(n)]

explore(*find('A'))

if solution:
    # change (3) print maze
    print('\n'.join(maze))
else:
    print("no path")

# Exercise 9.4* (deepcopy)
import copy


def deepcopy(L):
    new_copy = {}  # map of old list ids to new lists

    def recursive_copy(L):
        if not isinstance(L, list):  # det bare et element i listen
            return L
        if id(L) in new_copy:  # har vi fundet listen før?
            return new_copy[id(L)]

        L_copy = []
        new_copy[id(L)] = L_copy
        for e in L:
            L_copy.append(recursive_copy(e))
        return L_copy

    return recursive_copy(L)


# Exercise 10.1 (foldr)
import functools

foldl = functools.reduce


def foldr1(f, L):
    return L[0] if len(L) == 1 else f(L[0], foldr1(f, L[1:]))


def foldr1_(f, L):
    if len(L) == 1:
        return L[0]
    else:
        return f(L[0], foldr1_(f, L[1:]))


def foldr2(f, L):
    return L[0] if len(L) == 1 else foldr2(f, L[:-2] + [f(L[-2], L[-1])])


def foldr3(f, L):
    answer = L[-1]
    for i in range(len(L) - 1)[::-1]:
        answer = f(L[i], answer)
    return answer


def foldr4(f, L):
    answer = L[-1]
    for x in reversed(L[:-1]):
        answer = f(x, answer)
    return answer

#Exercise 10.2 (my_map)
#a
def my_map(f, L):
    return [f(l) for l in L]

#b
def my_map_k(f, *Ls):
    return [f(*l) for l in zip(*Ls)]
my_map_k(lambda x, y, z: x*y*z, [3, 2, 5], [2, 7, 9], [1, 2])

#Exercise 10.3 (string sorting)
def str_sort(L):
    return sorted(L, key=lambda x: (len(set([c for c in x.lower() if c.isalpha()])), x))

#Exercise 10.4 (binary search)
#a
def binary_search(f, low, high):
    print(low, high)
    if high - 1 == low:
        return high
    mid = (low + high) // 2
    if f(mid) == False:
         return binary_search(f, mid, high)
    return binary_search(f, low, mid)
#b
def local_min(f, low, high):
    return binary_search(lambda x: f(x) < f(x+1), low, high)
print(local_min(lambda x: (x - 3.5) ** 2 - 7 * x, -1000, 1000))

