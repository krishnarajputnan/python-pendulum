import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

g=9.8
l=1
dt=0.05
total_time=10
t=np.arange(0,total_time,dt)

theta=np.pi/4
omega=0.0
thetas=[theta]

for i in range(len(t)-1):
    alpha=-(g/l)*np.sin(theta)
    omega+=alpha*dt
    theta+=omega*dt

    thetas.append(theta)
x=(l)*np.sin(thetas)
y=(-l)*np.cos(thetas)
     
fig,ax=plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-1.5,1.5)
ax.set_ylim(-1.5,0.5)

line,=ax.plot([],[], 'o-',lw=2,markersize=20,color='red')
def animate(i):
    line.set_data([0,x[i]],[0,y[i]])
    return line,
ani=FuncAnimation(fig,animate,frames=len(t),interval=50,blit=True)
plt.show()
