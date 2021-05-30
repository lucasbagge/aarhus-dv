# Modules

import matplotlib.pyplot as plt
from pandas import DataFrame
import gzip
import json
from random import randint
import functools as ft
import struct
from collections import Iterable
from functools import reduce

## a ) Load data

## b) lav read labels funktion
def read_labels(filename):
    with gzip.open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        if magic != 2049:
            raise ValueError('Invalid magic number %d' % (magic))
        label_count = int.from_bytes(f.read(4), 'big')
        labels = f.read()
        return [b for b in labels]

read_labels('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz')

test_read_labels = read_labels('2-semester/ip/finalProject/t10k-labels-idx1-ubyte.gz')
print(f'De første elementer: \n {test_read_labels[:5]}')

## c) lav read images

def read_images(filename):
    with gzip.open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        if magic != 2051:
            raise ValueError('Invalid magic number %d' % (magic))
        image_count = int.from_bytes(f.read(4), 'big')
        row_count = int.from_bytes(f.read(4), 'big')
        column_count = int.from_bytes(f.read(4), 'big')
        image_data = f.read()
        images = [b for b in image_data]
        S = image_count, row_count, column_count
        images = list(ft.reduce(lambda x, y: map(list, \
                                             zip(*y*(x,))), \
                                             (iter(images), \
                                            *S[:0:-1])))
        return images

test_read_images = read_images("2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz")

# dim of list
def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

print(f'Se på dimensionen af list:\n {dim(test_read_images)}')

## d) plot images

labels_t10k = read_labels('2-semester/ip/finalProject/t10k-labels-idx1-ubyte.gz')
images_t10k = read_images('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz')

def plot_images(images, labels):
    num = 12
    images = images[:num]
    labels = labels[:num]
    num_row = 3
    num_col = 4
    fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
    fig.suptitle("Plot af de første 10 billeder og labels", \
                 fontsize = 20, \
                 horizontalalignment = "right")
    for i in range(num):
        ax = axes[i//num_col, i%num_col]
        ax.imshow(images[i], cmap='gray')
        ax.set_title('Label: {}'.format(labels[i]))
    plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=-0.5)
    plt.show()
    
plot_images(images_t10k, labels_t10k)
#plt.savefig('2-semester/ip/finalProject/plot_images.png')

## f) linear load og save

def linear_load(filename):
    with open(filename) as json_file:
        indata = json.load(json_file)
    return indata

test_linear_load = linear_load('2-semester/ip/finalProject/mnist_linear (4).weights')
print(f'Test om vi kan få nogle vægte ud: \n {test_linear_load[1]}')

def linear_save(file_name, network):
    file_name = file_name
    with open('%s-A.json' % file_name, 'w') as json_file:
        json.dump(network[0], json_file)
    with open('%s-b.json' % file_name, 'w') as json_file:
        json.dump(network[1], json_file)
    #

linear_save("file_test_name", test_linear_load)
## g) image to vector        
def image_to_vector(image):
    
    image_test = sum(map(lambda a: image_to_vector(a) if isinstance(a,(list)) else [a],image),[])
    
    return image_test

def divide_255(image):
    return [i/255 for i in image]


image_to_vector_test_divide = divide_255(image_to_vector(images_t10k[0]))

print(f' tester om funktionen virker \n {image_to_vector_test_divide}')

print(f'Test om alle elementer i listen er floats: \n {all(isinstance(x, float)\
        for x in image_to_vector_test_divide)}')

## h help function
V = [1,2,3]
U = [1,2,1]
M = [[1,2,3], [1,2,6], [1,2,1]]
def add(U, V): 
    assert len(U) == len(V), 'Dimension is different'
    adding = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        adding.append(U_i + V_i)
    return adding

print(f'Test om vi får det forventede {add(U, V)}')

def sub(U, V):
    difference = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        difference.append(U_i - V_i)
    return difference

print(f'Test if function works: \n {sub(U,V)}')

def scalar_multiplication(scalar, V):
    l = [x * scalar for x in V]
    return l

scalar = 2
V = [1,2,3]

print(f'Test if function works: \n {scalar_multiplication(scalar,V)}')

# Tvivl om hvilken dimension der skal være?
def multiply(V, M):
    result = []
    assert len(V) == len(M), 'Dimension is different'
    for i in range(len(M[0])): #this loops through columns of the matrix
        total = 0
        for j in range(len(V)): #this loops through vector coordinates & rows of matrix
            total += V[j] * M[j][i]
        result.append(total)
    return result

print(f'Test om funtionen virker: \n {multiply(V, M)}')

def transpose(M):
    result = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return result

print(f'Test om funtionen virker: \n {transpose(M)}')

## i)
def mean_square_error(U, V):
    n = len(V) 
    return sum([x ** 2 for x in sub(U,V)]) / n

print(f'Test om funktionen virker:\n {mean_square_error([1,2,3,4], [3,1,3,2])}')


## j) argmax

def argmax(a):
    return max(range(len(a)), key = lambda x: a[x])
a = [6, 2, 7, 10, 5]
print(f'Test om funktionen virker: \n {argmax(a)}')

## k) categorical

def categorical(label, classes = 10):
    """Convert an iterable of indices to one-hot encoded labels."""
    lst = [0] * classes
    lst[label] = 1
    return lst
print(f'Test om funktionen virker {categorical(3)}')

## l) predict funktion

def predict(network, image):
    A, b = network
    prediction = add(multiply(divide_255(image_to_vector(image)), A), b)
    return prediction

print("Test if function work \n", \
        argmax(predict(linear_load('2-semester/ip/finalProject/mnist_linear (4).weights'), \
        image= images_t10k[0:1])))
        
## m) evaluate function

def evaluate(network,image, labels):
  n = len(image)
  def predict3(image):
    A, b = network
    return add(multiply(image, A), b)
  adding = []
  for i in range(0, n):
    adding.append(divide_255(image_to_vector(image[i])))
  predic_eval = [argmax(predict3(i)) for i in  adding]  
  
  labels_adding = []
  for i in range(0, n):
    labels_adding.append(labels[i])
  
  mse = mean_square_error(labels_adding, predic_eval)
  
  accuracy = len([labels_adding[i] for i in range(0, \
             len(labels_adding)) if labels_adding[i] == predic_eval[i]]) /\
             len(labels_adding)
  
  return (predic_eval, mse, accuracy)


test_eval = evaluate(linear_load('2-semester/ip/finalProject/mnist_linear (4).weights'),\
          images_t10k[0:10000],\
          labels_t10k[0:10000])
print(test_eval)

## n)

def plot_images(images_t10k, labels_t10k, prediction):
    num = 10
    labels = labels_t10k[:num]
    images = images_t10k[:num]
    prediction = prediction[0][0:num]
    num_row = 2
    num_col = 5
    fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
    for i in range(num):
        ax = axes[i//num_col, i%num_col]
            ax.imshow(images[i], cmap='pink')
        ax.set_title(f'Pred: {prediction[i]}, Actual: {labels[i]}')
    plt.tight_layout()
    plt.show()

plot_images(read_images('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz'), \
            read_labels('2-semester/ip/finalProject/t10k-labels-idx1-ubyte.gz'),\
            test_eval)
            
## o) visualize column

A, b = linear_load('2-semester/ip/finalProject/mnist_linear (4).weights')

A_list = A

df = DataFrame(A_list,columns=['col0','col1','col2','col3','col4','col5',\
                'col6','col7','col8','col9'])

def reshape_list(list_to):
  S = 28, 28
  test_reshape = list(ft.reduce(lambda x, y: map(list, zip(*y*(x,))), (iter(list_to), *S[:0:-1])))
  return test_reshape

save_object = []
for i in df:
  save_object.append(df[i].tolist())

new_shape_of_A = list(map(reshape_list, save_object))

num = 10
num_row = 2
num_col = 5
fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
for i in range(num):
  ax = axes[i//num_col, i%num_col]
  ax.imshow(new_shape_of_A[i], plt.get_cmap('seismic'))
  ax.set_title('Shape of weights')
plt.tight_layout()
plt.show()

## p batch sizes

def create_batches(values, batch_size):
  return [values[i:i + batch_size] for i in range(0, len(values), batch_size)]

print(f'Check if functin works:\n {create_batches(list(range(7)), 3)}')
