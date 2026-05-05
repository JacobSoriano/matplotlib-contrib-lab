"""
=================================
Projectile Trajectories (2D)
=================================

This example illustrates simple projectile motion under uniform gravity for
different launch angles. It computes analytical trajectories using numpy and
plots range vs. height to compare how the launch angle affects flight paths.
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81  # gravity (m/s^2)
v0 = 20.0  # initial speed (m/s)
angles_deg = [30, 45, 60]

fig, ax = plt.subplots(figsize=(7, 4))

for angle in angles_deg:
    theta = np.deg2rad(angle)
    t_flight = 2 * v0 * np.sin(theta) / g
    t = np.linspace(0, t_flight, 200)
    x = v0 * np.cos(theta) * t
    y = v0 * np.sin(theta) * t - 0.5 * g * t ** 2
    ax.plot(x, y, label=f"{angle}°")

ax.set(title="Projectile Trajectories for Different Launch Angles",
       xlabel="Range (m)", ylabel="Height (m)")
ax.set_aspect('equal', adjustable='box')
ax.set_xlim(0, None)
ax.legend(title="Launch angle")
ax.grid(alpha=0.25)

plt.tight_layout()
plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules
#    is shown in this example:
#
#    - `matplotlib.axes.Axes.plot` / `matplotlib.pyplot.plot`
#    - `matplotlib.pyplot.subplots`
#    - `matplotlib.axes.Axes.set_aspect`
#    - `matplotlib.axes.Axes.legend`
#
# .. tags::
#
#    plot-type: line
#    level: beginner
