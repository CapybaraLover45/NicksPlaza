import numpy as np
import matplotlib.pyplot as plt
import math

#x,y range
x, y = np.meshgrid(np.linspace(-40,40,10), np.linspace(-40,40,10))


#vector field equations

u = x
v = y


plt.quiver(x,y,u,v, color='b')
plt.title('Vector Field')


plt.xlim(-50,50)
plt.ylim(-50,50)

plt.grid()
plt.show()
