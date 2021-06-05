'''TREE

   In this exercise we consider trees represented as nested tuples,
   where leaves store an integer and internal nodes have 1 or more
   children.

   Example: ((23, (11, (7,  2), -10), 0), 14)

            represents the tree

                    /\
                   /  \
                  /|\  14
                 / | \
               23 /|\ 0
                 / | \
               11 / \ -10 
                 /   \
                7     2
        
   The size of a tree is the number of leaves. The height of a tree is
   the maximal number of nodes on a root-to-leaf path. The above tree
   has size = 7 and depth = 5 (the number of nodes from the root to the
   leaves 2 and 7).

   Input:   A single line with a tree represented as a recursive tuple,
            with leaves being integers in the range [-1000, 1000]. The
            size and depth is at most 100.

   Output:  Two integers, the size of the tree followed by the height of
            the tree, separated by space. For the above tree the output is:

            7 5

            (see tests/F/... for more examples):

   Note:    The below code already contains code to read the tree and prints
            the size of the tree. Your task is to extend the code to also print
            the height of the tree.
'''


def size(tree):
    if not isinstance(tree, tuple):
        return 1
    return sum(size(child) for child in tree)
    
def depth(tree):
    if not isinstance(tree, tuple):
        return 1
    return 1 + max(depth(child) for child in tree)
    

tree = eval(input())  # read tree from standard input

print(size(tree), depth(tree))
