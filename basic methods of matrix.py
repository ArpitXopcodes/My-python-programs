'''matrix methods '''

import numpy as np

a = np.array([[1,2,3,4],[4,55,1,2],
              [8,3,20,19],[11,2,22,21]])
print(a)
m = np.reshape(a,(4, 4))
print(m)

#accessing elem
print("\nAccessing Elements")
print(a[1])
print(a[2][0])

# Adding Elem
m = np.append(m,[[1, 15,13,11]],0)
print("\nAdding Element")
print(m)

# Deleting Elem
m = np.delete(m,[1],0)
print("\nDeleting Element")
print(m)
