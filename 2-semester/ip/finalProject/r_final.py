import matplotlib.pyplot as plt
from pandas import DataFrame
import gzip
import json
from random import randint
import functools as ft
import struct
from collections import Iterable
from functools import reduce

# read labels 
def read_labels(filename):
    with gzip.open(filename, 'rb') as f:
        magic  = int(struct.unpack('>I', f.read(4))[0])
        if magic != 2049:
            raise ValueError('Invalid magic number %d in MNIST image file: %s' %
                             (magic))
        # second 4 bytes is the number of labels
        label_count = int.from_bytes(f.read(4), 'big')
        # rest is the label data, each label is stored as unsigned byte
        # label values are 0 to 9
        label_data = f.read()
        labels = label_data
        return [b for b in labels]
      
def read_images(filename):
    with gzip.open(filename, 'rb') as f:
        magic  = int(struct.unpack('>I', f.read(4))[0])
        if magic != 2051:
            raise ValueError('Invalid magic number %d' %
                             (magic))
        # second 4 bytes is the number of images
        image_count = int.from_bytes(f.read(4), 'big')
        # third 4 bytes is the row count
        row_count = int.from_bytes(f.read(4), 'big')
        # fourth 4 bytes is the column count
        column_count = int.from_bytes(f.read(4), 'big')
        # rest is the image pixel data, each pixel is stored as an unsigned byte
        # pixel values are 0 to 255
        image_data = f.read()
        #images = np.frombuffer(image_data, dtype=np.uint8).reshape((image_count, row_count, column_count))
        images = [b for b in image_data]
        S = image_count,row_count,column_count
        test = list(ft.reduce(lambda x, y: map(list, zip(*y*(x,))), (iter(images), *S[:0:-1])))
        return test
      
labels_t10k = read_labels('2-semester/ip/finalProject/t10k-labels-idx1-ubyte.gz')
images_t10k = read_images('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz')

def linear_load(filename):
    with open(filename) as json_file:
        indata = json.load(json_file)
    return indata

#ny 2021-05-24
def image_to_vector(image):
    return sum(map(lambda a: image_to_vector(a) if isinstance(a,(list)) else [a],image),[])

def divide_255(image):
  return [i/255 for i in image]

# dim of list
def dim(a):
    if not type(a) == list:
        return []
    return [len(a)] + dim(a[0])

def add(U, V): 
    #assert dim(U) == dim(V), 'Dimension is different'
    adding = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        adding.append(U_i + V_i)
    return adding

print(f'Test if function works: \n {add(U,V)}')

# Tvivl om hvilken dimension der skal være?
def multiply(V, M):
    result = []
    #assert dim(V) == dim(M[0]), 'Dimension is different'
    for i in range(len(M[0])): #this loops through columns of the matrix
        total = 0
        for j in range(len(V)): #this loops through vector coordinates & rows of matrix
            total += V[j] * M[j][i]
        result.append(total)
    return result

# argmax
def argmax(a):
    return max(range(len(a)), key = lambda x: a[x])

#plot 
def plot_images(images_t10k, labels_t10k):
    num = 8
    labels = labels_t10k[:num]
    images = images_t10k[:num]
    num_row = 2
    num_col = 4
    fig, axes = plt.subplots(num_row, num_col, figsize=(1.5*num_col,2*num_row))
    for i in range(num):
        ax = axes[i//num_col, i%num_col]
        ax.imshow(images[i], cmap='gray')
        ax.set_title('Label: {}'.format(labels[i]))
    plt.tight_layout()
    plt.show()

plot_images(read_images('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz'), \
            read_labels('2-semester/ip/finalProject//t10k-labels-idx1-ubyte.gz'))

# predict 1
def predict(network, image):
    A, b = network
    prediction = add(multiply(divide_255(image_to_vector(image)), A), b)
    return prediction
  
## test predict

argmax(predict(\
linear_load('2-semester/ip/finalProject/mnist_linear (4).weights'),\
image= images_t10k[0:1])\
)

# mse
def mean_square_error(U, V):
    summation = 0  
    n = len(U) 
    for i in range (0,n):  
        difference = U[i] - V[i]  
        squared_difference = difference ** 2  
        summation = summation + squared_difference  
    return (summation / n )
  
def sub(U, V):
    difference = []
    zip_object = zip(U, V)
    for U_i, V_i in zip_object:
        difference.append(U_i - V_i)
    return difference
  
def mse(U,V):
  n = len(U)
  cost = (1/n) * sum([val ** 2 for val in (U - V)])
  return cost



[val ** 2 for val in sum(sub([1,2,3,4],  [3,1,3,2]))]

sub([1,2,3,4], [3,1,3,2])
mse([1,2,3,4], [3,1,3,2])
# Create a function evaluate(network, images, labels) that given a list of image
# vectors and corresponding labels, returns the tuple (predictions, cost, accuracy),
# where predictions is a list of the predicted labels for the images, cost is the
# average of mean square errors over all input-output pairs, and accuracy the
# fraction of inputs where the predicted labels are correct. 
# Apply this to the loaded network and the 10.000 test images in t10k-images. 
# The accuracy should be around 92%, 
# whereas the cost should be 230 (the cost is very bad since the network was
# trained to optimze the cost measure softmax).
# Hint. Use your argmax function to convert network output into a label prediction.

def evaluate(network,image, labels, n):
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
          labels_t10k[0:10000],\
          10000)
print(test_eval)

# n) Extend plot_images to take an optional argument prediction that is a
# list of predicted labels for the images, and visualizes if the prediction is
# correct or wrong. Test it on a set of images from t10k-images and their correct
# labels from t10k-labels.

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
        ax.imshow(images[i], cmap='gray')
        ax.set_title(f'Pred: {prediction[i]}, Actual: {labels[i]}')
    plt.tight_layout()
    plt.show()

plot_images(read_images('2-semester/ip/finalProject/t10k-images-idx3-ubyte.gz'), \
            read_labels('2-semester/ip/finalProject//t10k-labels-idx1-ubyte.gz'),\
            test_eval)

# o )

# Column i of matrix A contains the (positive or negative) weight of each input
# pixel for class i, i.e. the contribution of the pixels towards the image
# showing the digit i. Use imshow to visualize each column
# (each column is a vector of length 784 that should be reshaped to an image of size 28 × 28).

A, b = linear_load('2-semester/ip/finalProject/mnist_linear (4).weights')

A_list = A

df = DataFrame(A_list,columns=['col0','col1','col2','col3','col4','col5',\
                'col6','col7','col8','col9'])

def reshape_list(list_to):
  S = 28, 28
  test_reshape = list(ft.reduce(lambda x, y: map(list, zip(*y*(x,))), (iter(list_to), *S[:0:-1])))
  return test_reshape

#def pandas_list(df):
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
  ax.imshow(new_shape_of_A[i], cmap = plt.get_cmap('seismic'))
  ax.set_title('Shape of weights')
plt.tight_layout()
plt.show()


## p)

#Create function create_batches(values, batch_size) that partitions a list of
# values into batches of size batch_size, except for the last batch, that can be smaller. 
# The list should be permuted before being cut into batches.
# Example: create_batches(list(range(7)), 3) should return [[3, 0, 1], [2, 5, 4], [6]].

def create_batches(values, batch_size):
  return [values[i:i + batch_size] for i in range(0, len(values), batch_size)]

print(f'Check if functin works:\n {create_batches(list(range(7)), 3)}')


## q

def categorical(label, classes = 10):
    """Convert an iterable of indices to one-hot encoded labels."""
    lst = [0] * classes
    lst[label] = 1
    return lst

a = predict(network = \
            linear_load('2-semester/ip/finalProject/mnist_linear (4).weights'),\
            image = images_t10k[0])
print(a)
create_batches(a, 2)
x = divide_255(image_to_vector(image=images_t10k[0]))
argmax(a)            
y = categorical(label=labels_t10k[0])

test_tuple = (x, a, y)
type(test_tuple)

create_batches(a, 3)

def b_update(sigma = 0.1):
  return sigma * (1/n) * sum(x, a, y) ** (2 * (a - y) / 10)

def A_update(sigma = 0.1):
  return sigma * (1/n) * sum(x, a, y) **  (x * 2*(a - y) / 10)
