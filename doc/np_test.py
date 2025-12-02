import numpy as np
print(np.__version__)

# In numpy the main object that save our date in ndarray (N-dimensional array)
# All elements in a ndarray should have the same type


"""
When you try to make an array in numpy do not use ndarray
Because it does not make an array of something like [1,2,3]

When you say np.ndarray([1,2,3]), you actually say make room for 
something that have 1 block, inside it 2 rows and each row with 3 columns.
It is uninitialized too. So, you get garbage in the memory jut like malloc in C.

"""

print(np.ndarray([1,2,3]))
print("=" * 70)
print(np.array([1,2,3]))

"""numpy provide some function to help you make array easier"""
print(np.zeros(3))
print("=" * 70)
print(np.ones((2,3)))
print("=" * 70)
print(np.full((2,3), "#"))
print("=" * 70)
"""In np.arrange, you specify the step. here is 4 so you get 0, 4, 8 , 12"""
print(np.arange(0, 15, 4))
print("=" * 70)
"""Here you choose how many numbers you want between 0 and 15"""
print(np.linspace(0, 15, 4))
print("=" * 70)
print(np.eye(3))
print("=" * 70)
"""In the np.empty you get random numbers from memory"""
print(np.empty(3))
print("=" * 70)
print(np.random.random(3))
print("=" * 70)
print(np.random.randint(1, 10, (3,3)))
print("=" * 70)
print(np.random.normal(0, 1, (3,3)))
print("=" * 70)
"""you could make a tensor like another one and full it with a number like:"""
a = np.random.normal(0, 1, (3,3))
print(np.full_like(a, 3))
print("=" * 70)
"""we could specify the type of our ndarray by dtype in input"""
list_a = np.array([1,2,3.5], dtype='float32')
print(list_a)
print(list_a.dtype, list_a.ndim, list_a.size)
"""change type of ndarray by astype"""
list_b = list_a.astype(int)
print(list_b)
print("=" * 70)
