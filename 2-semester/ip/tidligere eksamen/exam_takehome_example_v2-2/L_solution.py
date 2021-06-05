'''
    FIND_MAX

    In this problem, you should write a function find_max(f, data),
    that takes two arguments:

       f    : a function (or lambda expression) that takes two
              integers as arguments and returns an integer, e.g.
              f(x, y) = x + y
           
       data : non-empty list of (x, y) pairs [(x1, y1), (x2, y2), ..., (xn, yn)]

    The function find_max(f, data) should return the pair (xi, yi) in
    data where f(xi, yi) has maximum value. If the maximal value is
    obtained for several pairs in data, the first such pair in data
    should be returned.

    Example:

        find_max(lambda x, y: x + y, 
                 [(3, -2), (4, 1), (7, 3), (-5, 10), (-5, -5)])

        should return (7, 3)

    Note: 

        Below you should only implement the code for find_max.  The
        existing code already takes care of reading the function f and
        the list data from input, and prints the result of calling
        find_max(f, data).
'''


def find_max(f, data):
    pass  # add code here


# solution using build in max
def find_max(f, data):
    return max(data, key=lambda x: f(*x))

# slow solution
def find_max(f, data):
    result = data[0]
    for v in data[1:]:
        if f(*v) > f(*result):
            result = v
    return result


f = eval(input())
data = eval(input())
print(find_max(f, data))
