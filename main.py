
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Parameters
np.random.seed(42)
n_points = 400

# Generate synthetic 3D data (like PCA or factor model output)
mean = [0, 0, 0]
cov = [[1, 0.8, 0.5], [0.8, 1, 0.3], [0.5, 0.3, 1]]
X = np.random.multivariate_normal(mean, cov, n_points)

# Color by angle in XY plane for visual separation
angles = np.arctan2(X[:, 1], X[:, 0])
colors = plt.cm.rainbow((angles - angles.min()) / (angles.max() - angles.min()))

# Principal axes (e.g., from PCA)
axes = np.array([
    [2, 0, 0],   # x-axis
    [0, 2, 0],   # y-axis
    [0, 0, 2]    # z-axis
])
colors_axes = ['r', 'g', 'b']

fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

sc = ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=colors, s=30, alpha=0.7)

# Draw principal axes
for i in range(3):
    ax.quiver(0, 0, 0, axes[i, 0], axes[i, 1], axes[i, 2], color=colors_axes[i], linewidth=3, arrow_length_ratio=0.15)

# Labels
ax.set_xlabel('x0')
ax.set_ylabel('x1')
ax.set_zlabel('x2')
ax.set_title('Animated 3D Quant Surface (Scatter + Axes)')

# Animation function
def animate(frame):
    # Rotate view
    ax.view_init(elev=20, azim=frame)
    # Animate colors for fun
    phase = (np.sin(frame * np.pi / 90) + 1) / 2
    new_colors = plt.cm.rainbow(phase * (angles - angles.min()) / (angles.max() - angles.min()) + (1 - phase) * np.random.rand(n_points))
    sc._facecolor3d = new_colors
    sc._edgecolor3d = new_colors
    return sc,

ani = animation.FuncAnimation(fig, animate, frames=180, interval=50, blit=False)

plt.tight_layout()
plt.show()
