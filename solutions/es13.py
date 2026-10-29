### 13. Create a 10x10 array with random values and find the minimum and maximum values (★☆☆)

import numpy as np

AR = np.random.rand(10,10)

min = AR.min()
max = AR.max()

print(min,max)

