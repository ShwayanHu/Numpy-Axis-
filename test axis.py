import numpy as np

array = np.random.randint(0, 3, [3,2,4,5])

print(array)

print(np.sum(array,axis=2))