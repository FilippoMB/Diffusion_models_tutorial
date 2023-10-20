import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

mu_x = 0
variance_x = 6
mu_y = 0
variance_y = 25
rv1 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


mu_x = -9
variance_x = 12
mu_y = 12
variance_y = 4
rv2 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


mu_x = 10
variance_x = 12
mu_y = 7
variance_y = 12
rv3 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


#Create grid and multivariate normal
x = np.linspace(-15,15,500)
y = np.linspace(-15,15,500)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y


Z = rv1.pdf(pos) + rv2.pdf(pos) + rv3.pdf(pos)

#Make a 3D plot
fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Blues',linewidth=0)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
plt.axis('off')
plt.tight_layout()
plt.show()

#######################################
mu_x = 10
variance_x = 2
mu_y = 7
variance_y = 2
rv4 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


Z = rv4.pdf(pos) 

#Make a 3D plot
fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Oranges',linewidth=0)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
plt.axis('off')
plt.tight_layout()
plt.show()

########################################
mu_x = 0
variance_x = 6+5
mu_y = 0
variance_y = 25+5
rv1 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


mu_x = -9
variance_x = 12+5
mu_y = 12
variance_y = 4+5
rv2 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


mu_x = 10
variance_x = 4
mu_y = 7
variance_y = 4
rv3 = multivariate_normal([mu_x, mu_y], [[variance_x, 0], [0, variance_y]])


#Create grid and multivariate normal
x = np.linspace(-15,15,500)
y = np.linspace(-15,15,500)
X, Y = np.meshgrid(x,y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X; pos[:, :, 1] = Y


Z = rv1.pdf(pos) + rv2.pdf(pos) + rv3.pdf(pos)

#Make a 3D plot
fig = plt.figure(figsize=(10, 10), dpi=80)
ax = fig.gca(projection='3d')
ax.plot_surface(X, Y, Z,cmap='Greens',linewidth=0)
# ax.set_xlabel('X axis')
# ax.set_ylabel('Y axis')
# ax.set_zlabel('Z axis')
plt.axis('off')
plt.tight_layout()
plt.show()
