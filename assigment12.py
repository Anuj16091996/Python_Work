import time
import numpy as np
size_of_vec = 100000000

def python_version(ope):
    t1 = time.time()
    X = range(size_of_vec)
    Y = range(size_of_vec)
    if ope=="add":
        Z= [ X[i] + Y[i] for i in range(len(X))]
    elif ope=="mul":
        M= [ X[i] * Y[i] for i in range(len(X))]
    return time.time() - t1

def numpy_version(ope):
    t1 = time.time()
    X = np.arange(size_of_vec)
    Y = np.arange(size_of_vec)
    if ope=="add":
        Z= X + Y
    elif ope=="mul":
        M= X * Y
    return time.time() - t1

t1 = python_version("add")
t2= numpy_version("add")
print(t1,t2)
print("numpy in this example is " + str(t1/t2) + " faster for addition")

t3 = python_version("mul")
t4= numpy_version("mul")
print(t1,t2)
print("numpy in this example is " + str(t1/t2) + " faster for multiplication")