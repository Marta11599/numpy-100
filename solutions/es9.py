#### 9. Create a 3x3 matrix with values ranging from 0 to 8 (★☆☆)

import numpy as np

M = np.arange(0,9)

R = M.reshape((3,3))

print(M,R, sep = '\n')
