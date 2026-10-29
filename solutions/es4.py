#### 4. How to find the memory size of any array (★☆☆)

import numpy as np

Z = np.zeros((10,10))

print(Z.size,Z.itemsize, sep= '\n')
print("%d bacini" % 1000)
print("%d bytes " % (Z.size * Z.itemsize))
print((Z.size * Z.itemsize), "bytes")
print(Z.ndim)