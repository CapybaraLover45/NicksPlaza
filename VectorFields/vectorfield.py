import numpy as np
import matplotlib.pyplot as plt
import math

#x,y range
x, y = np.meshgrid(np.linspace(-5,5,10), np.linspace(-5,5,10))


#vector field equations

u = pow(x,2)-pow(y,2)-4
v = 2*x*y


plt.quiver(x,y,u,v, color='b')
plt.title('Vector Field')


plt.xlim(-7,7)
plt.ylim(-7,7)

plt.grid()
plt.show()
