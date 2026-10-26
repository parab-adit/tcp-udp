import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
from matplotlib.widgets import Slider

fig, ax = plt.subplots(figsize=(8, 8))
plt.subplots_adjust(bottom=0.18)
s_i = Slider(plt.axes([0.2, 0.08, 0.6, 0.03]), 'i', 0, 4, valinit=2, valstep=1)
s_j = Slider(plt.axes([0.2, 0.03, 0.6, 0.03]), 'j', 0, 4, valinit=1, valstep=1)
def draw(val=None):
    i, j = int(s_i.val), int(s_j.val)
    if i == 0 and j == 0:
        return
    N = i**2 + i*j + j**2
    Q = np.sqrt(3*N)
    ax.clear()
    for q in range(-6, 7):
        for r in range(-6, 7):
            x = np.sqrt(3) * (q + r/2)
            y = 1.5 * r
            if np.hypot(x, y) > 10:
                continue
            k = ((q*(i+j) + r*j) % N, (r*i - q*j) % N)
            color = (k[0] * N + k[1]) / (N*N)
            ax.add_patch(RegularPolygon(
                (x, y), 6, radius=1,
                facecolor=plt.cm.rainbow(color),
                edgecolor='black'
            ))
            ax.text(x, y, f'F{(k[0]*N+k[1])%N+1}',
                    ha='center', va='center', fontsize=7)
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title(f'i={i}, j={j}, N={N}, Q=D/R={Q:.2f}')
    fig.canvas.draw_idle()
s_i.on_changed(draw)
s_j.on_changed(draw)
draw()
plt.show()