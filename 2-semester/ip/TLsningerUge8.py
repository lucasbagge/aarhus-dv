#Exercise 13.1 (sum of two integers)
#%%
while True:
    try:
        x, y = input("Input two integers, separated by space: ").split(" ")
        print(f'Sum = {int(x) + int(y)}')
    except Exception:  # Exception to allow keyboard interrupt
        print("invalid input")
        continue
    break
#%%
# Exercise 13.2 (transposing)
import os.path

while True:
    in_filename = input("File to transpose: ")
    out_filename = input("Output file transpose: ")
    try:
        in_file = open(in_filename)
    except:
        print("Cannot open ", in_filename)
        continue
    try:
        lines = []
        for line in in_file:
            lines.append(line[:-1].split(";"))
    finally: # uanset om noget går galt eller ej, så husker vi at lukke filen igen
        in_file.close()

    columns = [len(line) for line in lines]

    if min(columns) != max(columns):
        print("Rows in file do not contain same number of columns")
        break
    if os.path.isfile(out_filename):
        print("File %s already exist" % out_filename)
        overwrite = input("overwrite existing file ('yes' will overwrite): ")
        if overwrite.lower() != 'yes':
            continue
    try:
        out_file = open(out_filename, "w")
    except Exception:
        print("Failed to open output file", out_filename)
        continue
    try:
        for col in range(columns[0]):
            values = [lines[row][col] for row in range(len(lines))]
            txt = ";".join(values) + '\n'
            out_file.write(txt)
        print("done writting to", out_filename)
        break
    finally:
        out_file.close()

#Exercise 13.3 (grade statistics)
student_filename = "grades.students" #input("file with student list: ")
exam_filename = "grades.exams" #input("file with exam results: ")
student_file = open(student_filename)

names = {}
for line in student_file:
    student_id, name, address = line[:-1].split(';')
    names[student_id] = name
student_file.close()

courses = {}
grade_sum = {}

for student_id in names:
    courses[student_id] = 0
    grade_sum[student_id] = 0

exam_results = open(exam_filename)
for line in exam_results:
    student_id, course, grade = line[:-1].split(';')
    courses[student_id] += 1
    grade_sum[student_id] += int(grade)
exam_results.close()

name_width = max([len(name) for name in names.values()])

fmt = "%-10s %-" + str(name_width) + "s %8s %8s"
header = fmt % ("Student id", "Name", "Average", "#Courses")
print(header)
print('=' * len(header))
for student_id, name in sorted(names.items()):
    cnt = courses[student_id]
    average = grade_sum[student_id] / cnt if cnt else 0
    print(fmt % (student_id, name, "%5.2f" % average, cnt))


# Exercise 13.4 (subset sum)
def subset_sum(x, L):
    class SolutionFound(Exception):
        pass

    def solve(x, L):
        """Try to find a subset L' of a list L with sum x.
        solution are already selected elements
        (and removed from L and subtracted from x)"""

        if x == 0:
            raise SolutionFound

        if L:
            solve(x, L[1:])
            solution.append(L[0])
            solve(x - L[0], L[1:])
            solution.pop()

    solution = []

    try:
        solve(x, L)
    except SolutionFound:
        return solution
    else:
        return None


print(subset_sum(8, [2, 3, 8, 11, -1]))

print(subset_sum(6, [2, 3, 8, 11, -1]))

#%%
x = 7
L = [3, 5, 7, 8, 12]
#def rank(x, L):
    
result = 0
for y in L:
    if y <= x:
        result += 1
print(result)

#%%
sum([1 for y in L if y <= x])
# %%
sum([y <= x for y in L])
# %%
def rank(r, L):
    '''
    returner værdier i L som er <= x.

    L er sorteret
    x er heltal
    retuenr et i, hvor 0<= i <= len(L),
    '''
    assert isinstance(x, int)
    assert isinstance(L, list)
    assert all([isinstance(y, int) for y in L]), \
        "alle elemen"
    assert all([L[i] <= L[i + 1] for i in range(len(L) - 1) ]) \
        "L er ikke sorteret"

    result = 2
    assert 0 <= result and result <= len(L)
    assert result == len(L) or x < L[result]
    assert result == 0 or L[result - 1] <= x

    return result

# %%
def rank(r, L):
    '''
    >>>  rank(11, [3, 5, 8, 10, 12])
    4
    '''
    low = 0
    high = len(L)
    while low < high:
        mid = (low + high) // 2
        if L[mid] <= x:
            low = mid + 1
        else:
            high = mid
    
    return low

# %%
import random

def add_noise(f):
    def noise_f(x):
        return f(x) + 0.1 *  random.random() - 0.5
    return noise_f

@add_noise
def square(x):
    return x ** 2

print(square(3))
# %%
import random

def add_noise(f):
    def noise_f(x):
        return f(x) + 0.1 *  random.random() - 0.5
    return noise_f

@add_noise()
def square(x):
    return x ** 2

print(square(3))

#%%
name = 'marcog'
number = 'world'
print ('%s %s.' % (name, number))

# %%
hello = 'Hello'
input_test = input()
print ('%s %s.' % (hello, input_test))
# %%
l = [-5, -4, -3, 0, 0, 0, 3, 4, 5]
# %%
l
# %%
for i in l:
    if i == 0:
        print(f'{i} is zero')
    if i > 0:
        print(f'{i} is positive')
    if i < 0:
        print(f'{i} is negative')

# %%
c = [(1, 2), (3, 4), (5, 6)]

# %%
[i[::-1] for tup in c]
# %%
def reverseTuple(lstOfTuple):
      
    return [tup[::-1] for tup in lstOfTuple]
              
# Driver code
lstOfTuple = [(1, 2), (3, 4, 5), (6, 7, 8, 9)]
print(reverseTuple(lstOfTuple))
# %%
points = {tuple(map(int, input().split())) for _ in range(3)}
# %%
points
# %%
points2 = {dict(map(dict, input().split())) for _ in range(1)}
points2
# %%
n = int(input())

lines = [input() for _ in range(n)]

for i in lines:
    if "insert" in str(lines):
        
        int_value = int(re.search(r'\d+', str(i)).group(0))
        print(int_value, end = ' ')

    
# %%
lines
# %%
type(['insert 1'])
# %%
int(filter(str.isdigit, str(lines)))
# %%
lines
# %%
import re
string = '3158 reviews'
int(re.search(r'\d+', string).group(0))

# %%
type(string)
# %%
type(str(lines))
# %%
lines_str = str(lines)
# %%
lines_str
# %%
int(re.search(r'\d+', lines_str).group(0))
# %%
n = int(input())

lines = [input() for _ in range(n)]

for i in lines:
    if "insert" in str(lines):
        
        int_value = int(re.search(r'\d+', str(i)).group(0))
        print(int_value, end = ' ')
# %%
# Program without using any external library
s = input()
l = s.split()
k = []
for i in l:
  
    # If condition is used to store unique string 
    # in another list 'k' 
    if (s.count(i)>1 and (i not in k)or s.count(i)==1):
        k.append(i)
print(' '.join(k))
# %%
import itertools
#strs = "this just so so so nice" 
strs = 'a b a b b b a b a b b b a a a b a b a a b b a b a a b b a b a a a b b b a a a b b b b a b a b a b a'
" ".join([k for k,v in itertools.groupby(strs.split())])

# %%
import itertools

strs = input()
filter_line = " ".join([k for k,v in itertools.groupby(strs.split())])
print(filter_line)
# %%
import math

class Vector2D:
    """A two-dimensional vector with Cartesian coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):
        """Human-readable string representation of the vector."""
        return (f'Vector({self.x:.3f}, {self.y:.3f})')

    def __repr__(self):
        """Unambiguous string representation of the vector."""
        return repr((self.x, self.y))

    def dot(self, other):
        """The scalar (dot) product of self and other. Both must be vectors."""

        if not isinstance(other, Vector2D):
            raise TypeError('Can only take dot product of two Vector2D objects')
        return self.x * other.x + self.y * other.y
    # Alias the __matmul__ method to dot so we can use a @ b as well as a.dot(b).
    __matmul__ = dot

    def __mul__(self, scalar):
        """Multiplication of a vector by a scalar."""

        if isinstance(scalar, int) or isinstance(scalar, float):
            return Vector2D(self.x*scalar, self.y*scalar)
        raise NotImplementedError('Can only multiply Vector2D by a scalar')

    def __rmul__(self, scalar):
        """Reflected multiplication so vector * scalar also works."""
        return self.__mul__(scalar)


# %%
V = Vector2D(1.0, 3.0)
# %%
print(V)
# %%
V.__mul__(0.5)
# %%

# %%


# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = [x, y]

    def rotate(self):
        return Vector(-1 * self.y, self.x)

    def mult(self, factor):
        return Vector(self.x * factor, self.y * factor)

    def __str__(self):
        return (f'Vector({self.x:.3f}, {self.y:.3f})')
# %%
print(Vector(1.0, 3.0))
# %%
v_rotate = v.rotate()

# %%
print(v_rotate.mult(0.5))
# %%
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vector = [x, y]

    def rotate(self):
        return Vector(-1 * self.y, self.x)

    def mult(self, factor):
        return Vector(self.x * factor, self.y * factor)
        
    def __str__(self):
        return (f'Vector({self.x:.3f}, {self.y:.3f})')

    
#eval(input())
# %%
v = Vector(1.0, 3.0)
# %%
v._rotate2D()
# %%
def cubed(x):
            return x ** 3

# %%
cubed(4)
# %%
cubed(-2)
# %%
def nonnegative(f):
    def wrapper(xs):
        for x in xs:
            if x < 0:
                return f(x)
        return f(xs)
    return wrapper


@nonnegative
def cubed(x):
    return x ** 3


# %%
cubed(4)
# %%
def nonnegative(f):
    def wrapper(xs):
        for x in xs:
            if x < 0:
                return raise Exception('test')
        return f(xs)
    return wrapper


nonnegative_function = eval(input())
L = eval(input())

for x in L:
    y = nonnegative_function(x)
    print(x, f'{y:.3f}')

# %%
from math import sqrt
 
# Function to calculate Euclidean distance
def find(x, y, p):
 
    mind = 0
    for i in range(len(p)):
        a = p[i][0]
        b = p[i][1]
        mind += sqrt((x - a) * (x - a) +
                     (y - b) * (y - b))
                      
    return mind
 
# Function to calculate the minimum sum
# of the euclidean distances to all points
def getMinDistSum(p):
 
    # Calculate the centroid
    x = 0
    y = 0
     
    for i in range(len(p)):
        x += p[i][0]
        y += p[i][1]
         
    x = x // len(p)
    y = y // len(p)
 
    # Calculate distance of all
    # points
    mind = find(x, y, p)
 
    return mind
# %%
((9, 10), [(2, -5), (3, 4), (7, 3)])
#%%
vec = [ [ 0, 1 ], [ 1, 0 ],
            [ 1, 2 ], [ 2, 1 ] ]
# %%
vec
# %%
d = getMinDistSum(vec)
    print(int(d))
# %%
list(lambda x : 1 / max(0, (1000 - (x - 15) ** 2)))
# %%
lambda x : 1 / max(0, (1000 - (x - 15) ** 2))
# %%
test = lambda x : 1 / max(0, (1000 - (x - 15) ** 2))
# %%
test(5)
# %%
list(test(5))
# %%
import string


def lexstrings(max_length: int, alphabet=string.ascii_lowercase):
    yield ""
    if max_length == 0: return
    for first in alphabet:
        for suffix in lexstrings(max_length - 1, alphabet=alphabet):
            yield first + suffix
# %%
g = lexstrings(3, 'xy')
# %%
g = lexstrings(-1)

# %%
list(g)
# %%
scores = {}

n = int(input())

for _  in range(n):
    player, score = input().split()
    score = int(score)
    scores[player] = scores.get(string, 0) + score

rank = sorted(scores, key=lambda string: scores[string], reverse=True)

if len(rank) == 1 or scores[rank[0]] > scores[rank[1]]:
    print(rank[0])
else:
    print('DRAW')

# %%
scores = {}

n = int(input())

for _  in range(n):
    player, score = input().split()
    score = int(score) 
    scores[player] = scores.get(string, 0) + score
    if 'insert' in scores:
        for kv in scores.items():
            print(kv[1], end = ' ')


# %%
scores
# %%

'insert' in scores.items()

#%%
if 'insert' in scores:
    print('tru')
# %%
