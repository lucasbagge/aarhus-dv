# Modules

import matplotlib.pyplot as plt
from pandas import DataFrame
import gzip
import json
from random import randint
import functools as ft
from collections import Iterable
from functools import reduce

# a ) Load data

## Indlæs data og gem det ned.

# b) lav read labels funktion

def read_labels(filename):
    """Indlæse labels.
    Keyword arguments:
    filename -- Fra en gz fil indlæses labels.
    """
    with gzip.open(filename, 'rb') as f:
        magic = int.from_bytes(f.read(4), 'big')
        if magic != 2049:
            raise ValueError('Invalid magic number %d' % (magic))
        label_count = int.from_bytes(f.read(4), 'big')
        labels = f.read()
        return [l for l in labels]

print("Tester om vi får en error: \n", \
      read_labels('t10k-images-idx3-ubyte.gz'))

test_read_labels = read_labels('t10k-labels-idx1-ubyte.gz')
                               
print(f'De første elementer: \n {test_read_labels[:5]}')

# c) lav read images

def read_images(filename):
    """Indlæse billede.
    Keyword arguments:
    filename -- Fra en gz fil indlæses billeder.
    """
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

test_read_images = read_images("t10k-images-idx3-ubyte.gz")

## dim of list
def dim(lst):
    """Se dimension på en  list.

    Keyword arguments:
    lst -- Den givet list objekt som man vil se dimension på
    """
    if not type(lst) == list:
        return []
    return [len(lst)] + dim(lst[0])

print(f'Se på dimensionen af list:\n {dim(test_read_images)}')

# d) plot images

labels_t10k = read_labels('t10k-labels-idx1-ubyte.gz')
images_t10k = read_images('t10k-images-idx3-ubyte.gz')

def plot_images(images, labels):
    """Plotter billeder og tilsvarende labels.
    Keyword arguments:
    images -- De images som skal visualiseres
    labels -- De labels som svarer til billede der vises
    """
    num = 12
    images = images[:num]
    labels = labels[:num]
    num_row = 3
    num_col = 4
    fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
    fig.suptitle("Plot af de første 12 billeder og labels", \
                 fontsize = 20, \
                 horizontalalignment = "right")
    for i in range(num):
        ax = axes[i//num_col, i%num_col]
        ax.imshow(images[i], cmap='gray')
        ax.set_title('Label: {}'.format(labels[i]))
    plt.tight_layout(pad=0.8, w_pad=0.5, h_pad=2.4)
    plt.show()
    
plot_images(images_t10k, labels_t10k)
#plt.savefig('plot_images.png')

# f) linear load og save

def linear_load(filename):
    """Load en model ind med vægte og bias.
    Keyword arguments:
    filename -- En fil som indholder modellen med vægte og bias
    """
    with open(filename) as json_file:
        indata = json.load(json_file)
    return indata

test_linear_load = linear_load('mnist_linear (4).weights')
print(f'Test om vi kan få nogle vægte ud: \n {test_linear_load[1]}')

def linear_save(filename, network):    
    """Gem modellen vægte og bias ned.
    Keyword arguments:
    filename -- Filnavnet som bliver gemt ned
    network  -- Modellen som skal gemmes
    """
    filename = filename
    with open('%s-A.json' % filename, 'w') as json_file:
        json.dump(network[0], json_file)
    with open('%s-b.json' % filename, 'w') as json_file:
        json.dump(network[1], json_file)

linear_save("file_test_name", test_linear_load)

# g) image to vector        
def image_to_vector(image):
    """Transformer en n x n matrix til en flas list n x 1.
    Keyword arguments:
    image -- Det billedes som skal flades ud
    """
    image_test = sum(map(lambda a: image_to_vector(a) if \
                     isinstance(a,(list)) else [a],image),[])
    
    return image_test

def divide_255(image):
    """Dele en liste med 255.
    Keyword arguments:
    image -- Tager en liste og deler hver indgang med 255
    """
    return [i/255 for i in image]


image_to_vector_test_divide = divide_255(image_to_vector(images_t10k[0]))

print(f' tester om vi får en flas liste ud \n {image_to_vector_test_divide}')

print(f'Test om alle elementer i listen er floats: \n \
      {all(isinstance(x, float) for x in image_to_vector_test_divide)}')

# h) linear algebra functions

## Vektor, matricer og skalar

V = [1,2,3]
U = [1,2,1]
M = [[1,2,3], [1,2,6], [1,2,1]]
scalar = 2

def add(U, V): 
    """Lægger to vektor sammen
    Keyword arguments:
    U  -- En vektor
    V  -- En vektor
    """
    assert len(U) == len(V), 'Dimension is different'
    adding = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        adding.append(U_i + V_i)
    return adding

print(f'Test om vi får det forventede {add(U, V)}')

def sub(U, V):
    """Trækker to vektor sammen
    Keyword arguments:
    U  -- En vektor
    V  -- En vektor
    """
    difference = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        difference.append(U_i - V_i)
    return difference

print(f'Test if function works: \n {sub(U,V)}')

def scalar_multiplication(scalar, V):
    """Ganger en skalar på en vektor.
    Keyword arguments:
    scalar  -- En skalar
    V  -- En vektor
    """
    l = [x * scalar for x in V]
    return l

print(f'Test if function works: \n {scalar_multiplication(scalar,V)}')

def multiply(V, M):
    """Ganger en vektor på en matrice.
    Keyword arguments:
    V  -- En vektor
    M  -- En matrice
    """
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
    """Transponer en matrice.
    Keyword arguments:
    M  -- En matrice
    """
    result = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return result

print(f'Test om funtionen virker: \n {transpose(M)}')

# i)
def mean_square_error(U, V):
    """Beregner mean squared error fra to vektor.
    Keyword arguments:
    U  -- En vektor
    V  -- En vektor
    """
    n = len(V) 
    return sum([x ** 2 for x in sub(U,V)]) / n

print(f'Test om funktionen virker:\n {mean_square_error([1,2,3,4], [3,1,3,2])}')


# j) argmax

def argmax(V):
    """Beregner positionen af den højest værdi i en liste.
    Keyword arguments:
    a  -- En vektor
    """
    return max(range(len(V)), key = lambda x: V[x])
V = [6, 2, 7, 10, 5]
print(f'Test om funktionen virker: \n {argmax(V)}')

# k) categorical

def categorical(label, classes = 10):
    """Udfører one hot encoding til en list.
    Keyword arguments:
    label  -- Den værdi som skal være forskellig fra nul 
    classes  -- Angiver listen længde
    """
    lst = [0] * classes
    lst[label] = 1
    return lst
print(f'Test om funktionen virker {categorical(3)}')

# l) predict funktion

def predict(network, image):
    """Prædiktion af et billede.
    Keyword arguments:
    network  -- En model som består af A og b
    image  -- Et 28 x 28 billede
    """
    A, b = network
    prediction = add(multiply(divide_255(image_to_vector(image)), A), b)
    return prediction

print("Test if function work \n", \
        argmax(predict(linear_load('mnist_linear (4).weights'), \
        image= images_t10k[0:1])))
        
# m) evaluate function

def evaluate(network, image, labels):
  """Evaluerer modellen på bagrund af mse og accuracy.
  Keyword arguments:
  network  -- En model som består af A og b
  image  -- Et 28 x 28 billede
  labels  -- De korrekte labels som vi tester mod
  """
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


test_eval = evaluate(linear_load('mnist_linear (4).weights'),\
          images_t10k[0:10000],\
          labels_t10k[0:10000])
print(f'Tester om funktion virker: \n ({test_eval[0][0:10]},{test_eval[1]}, {test_eval[2]})')

# n)

def plot_images(image, label, prediction):
    """Plotter billeder, labels og prædiktionen.
    Keyword arguments:
    image  -- En 28 x 28 billede der skal vises
    label  -- Billedes labels
    prediction  -- Modellen der prædiktierer billede
    """
    num = 12
    images = image[:num]
    labels = label[:num]
    num_row = 3
    num_col = 4
    prediction = prediction[0][0:num]
    is_it_equal_list = [i==j for i, j in zip(labels, prediction)]
    colors = [ 'gray_r' if x == True else x for x in is_it_equal_list]
    colors_final = [ 'pink' if x == False else x for x in colors]
    fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
    fig.suptitle("Plot med predictions", \
                 fontsize = 20, \
                 horizontalalignment = "right")
    for i in range(num):
        ax = axes[i//num_col, i%num_col]
        ax.imshow(images[i], cmap = colors_final[i])
        ax.set_title(f'Pred: {prediction[i]}, Actual: {labels[i]}')
    plt.tight_layout(pad=0.8, w_pad=0.5, h_pad=2.4)
    plt.show()
    
plot_images(read_images('t10k-images-idx3-ubyte.gz'), \
            read_labels('t10k-labels-idx1-ubyte.gz'),\
            test_eval)

#plt.savefig('plot_images_predictions.png')


## o) visualize column

A, b = linear_load('mnist_linear (4).weights')

A_list = A

df = DataFrame(A_list,columns=['col0','col1','col2','col3','col4','col5',\
                'col6','col7','col8','col9'])

def reshape_list(lst):
  """Reshape liste.
  Keyword arguments:
  lst  -- En flad billede der skal reshapes til en 28 x 28 matrix
  """
  S = 28, 28
  test_reshape = list(ft.reduce(lambda x, y: map(list, zip(*y*(x,))), (iter(lst), *S[:0:-1])))
  return test_reshape

save_object = []
for i in df:
  save_object.append(df[i].tolist())

new_shape_of_A = list(map(reshape_list, save_object))

num = 10
num_row = 2
num_col = 5
labels = [i for i in range(10)]
fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
fig.suptitle("Plot af vægtene", \
                 fontsize = 20, \
                 horizontalalignment = "right")
for i in range(num):
  ax = axes[i//num_col, i%num_col]
  ax.imshow(new_shape_of_A[i], plt.get_cmap('seismic'))
  ax.set_title('Label: {}'.format(labels[i]))
plt.tight_layout(pad=0.8, w_pad=0.5, h_pad=2.4)
plt.show()
#plt.savefig('plot_images_weights.png')

## p batch sizes

def create_batches(values, batch_size):
  """Lav batches ud fra en liste.
  Keyword arguments:
  values  -- En liste som skal deles op
  batch_size -- Størrelsen på batch
  """
  return [values[i:i + batch_size] for i in range(0, len(values), batch_size)]

print(f'Check if functin works:\n {create_batches(list(range(7)), 3)}')
