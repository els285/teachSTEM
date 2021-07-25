%%capture
%matplotlib notebook

import numpy as np
import matplotlib.pyplot as plt

from matplotlib import animation, rc
from IPython.display import HTML


def generate_duct_animation(duct1,flow1):

    plt.rcParams["animation.html"] = "jshtml"
    plt.rcParams["figure.figsize"] = [20,10]

    outerX = duct1[2]
    outerY = duct1[3]
    shapex = duct1[0]
    shapey = duct1[1]

    # First set up the figure, the axis, and the plot element we want to animate
    #fig, ax = plt.subplots()
    fig = plt.figure()
    fig.tight_layout()
    ax = fig.add_subplot(111)

    #ax.set_xlim((-0.5, 2.5))
    #ax.set_ylim((-1, 5))

    ax.axis("off")

    #size = np.linspace(1,Npoints)

    line, = ax.plot([], [],'o',markersize=10)

    plt.plot(shapex, shapey, color='black', alpha=0.7,
        linewidth=3, solid_capstyle='round', zorder=2)

    colors = plt.get_cmap('jet', NpointsX+1)

    time_template = 'fluid velocity = %.3f $V_{0}$'
    time_text = ax.text(0.8, 1, '', transform=ax.transAxes,fontsize=30)


    # initialization function: plot the background of each frame
    def init():
        #line.set_data([], [])
        #line.set_color(colors(i))
        return (line)

    # animation function. This is called sequentially
    def animate(i):
        line.set_data(outerX[i-1:i],outerY[i-1:i])
        line.set_color(colors(i))
        line.set_markersize(20)
        if i > 0 and i < len(flow1)+1:
            time_text.set_text( time_template % flow1[i-1][1])
            time_text.set_color(colors(i))

        return (line,)

    ani = matplotlib.animation.FuncAnimation(fig, animate, init_func=init, frames=31, interval=200)

    return ani