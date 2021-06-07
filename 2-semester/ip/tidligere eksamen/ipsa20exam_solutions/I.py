'''
    VECTOR SORT

    In this problem you are given a list of tuples, each tuple
    containing three integers. We consider the tuples representing 3d
    vectors and your task is to sort the list of vectors by increasing
    norm, where the norm of (x, y, z) = sqrt(x**2 + y**2 + z** 2).

    Input:  A Python list of n tuples, where 1 <= n <= 1000 and each tuple
            contains 3 integers representing a 3d vector. It is
            guaranteed that all vectors have different length.

    Output: The list of tuples sorted with respect to increasing norm.

    Example:

      Input:  [(3, 1, 2), (-2, 1, 4), (2, 2, 2), (-1, 1, -1)]

      Output: [(-1, 1, -1), (2, 2, 2), (3, 1, 2), (-2, 1, 4)]

    Note: Below you only need to implement the function vector_sort,
          that as input gets the list of tuples.
'''


def vector_sort(vectors):
    assert 1 <= len(vectors) <= 1000
    assert all(isinstance(v, tuple) and len(v) == 3 for v in vectors)
    assert len(vectors) == len(set(x**2 + y**2 + z**2 for x, y, z in vectors))

    return sorted(vectors, key=lambda v: v[0]**2 + v[1]**2 + v[2]**2)


vectors = eval(input())
print(vector_sort(vectors))
