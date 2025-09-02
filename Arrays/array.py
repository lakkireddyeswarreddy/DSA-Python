
"""
Python doesn't have built-in array data structure like other programming languages, but we can use the list as an array.
But python has an array module that can be used to create array data structure, but it is not used widely as the list is more flexible and powerful.
Both lists and arrays have the same methods and operations, but arrays can store only the same data type elements, and it is more memory efficient than the list.
But lists can store different data type elements, and it is more flexible than the array.

Arrays are more efficient than lists when it comes to numerical computations and large datasets, as they use less memory and provide better performance for mathematical operations.

Lists store the references to the objects, so it takes more memory, but arrays store the actual values, so it takes less memory.

To create an array we need to import the array module and use the array() method, it takes two arguments, the first one is the type code and the second one is the iterable object.

These are the type codes that can be used to create an array.
Type code  C Type             Python Type     Minimum size in bytes
'b'        signed char        int             1
'B'        unsigned char      int             1
'u'        wchar_t            str             2
'h'        signed short       int             2
'H'        unsigned short     int             2 
'i'        signed int         int             2
'I'        unsigned int       int             2
'l'        signed long        int             4
'L'        unsigned long      int             4
'f'        float              float           4
'd'        double             float           8
's'        char[]             str            1
'p'        pascal string      str            1


from the above type codes the most commonly used type code examples are :

int_array = array.array('i', [1, 2, 3, 4, 5]) # creates an array of signed integers
float_array = array.array('f', [1.1, 2.2, 3.3]) # creates an array of floats
char_array = array.array('u', 'hello') # creates an array of unicode characters
string_array = array.array('s', b'hello') # creates an array of bytes

So in python we can use the list as an array, but if we want to use the array module we can use it as shown above.

There is an another approach for creating arrays in python using the numpy library, it is a powerful library for numerical computations and data analysis.
We can create an array using the numpy array() method, it takes an iterable object as an argument and returns a numpy array object.
import array
import numpy as np
int_array = array.array('i', [1, 2, 3, 4, 5])
numpy_array = np.array([1, 2, 3, 4, 5])

using numpy we can create multi-dimensional arrays, and it provides a lot of mathematical functions that can be used to perform operations on the arrays.

Some of the examples using numpy arrays:
import array
import numpy as np
int_array = array.array('i', [1, 2, 3, 4, 5])
numpy_array = np.array([1, 2, 3, 4, 5])
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])
print(numpy_array.shape) # prints the shape of the array
print(two_d_array[0, 1]) # prints the element at the first row and second column
print(numpy_array.mean()) # prints the mean of the array
print(numpy_array.sum()) # prints the sum of the array

to install numpy use the command pip install numpy 

nunpy arrays are homogeneous, so they can store only the same data type elements, and it is more memory efficient than the list.

numpy arrays are of fixed size, so we cannot append or remove elements from the array, but we can create a new array with the desired elements.

to get the size of the array we can use the nbytes attribute, it returns the size of the array in bytes.
print(numpy_array.nbytes) # prints the size of the array in bytes
to get the number of elements in the array we can use the size attribute, it returns the number of elements in the array.
print(numpy_array.size) # prints the number of elements in the array
to get the shape of the array we can use the shape attribute, it returns a tuple containing the dimensions of the array.
print(numpy_array.shape) # prints the shape of the array

"""