import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:

    rw = RandomWalk(5000)
    rw.fill_walk()

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.plot(
        rw.x_values,
        rw.y_values,
        linewidth=1,
        color='grey'
    )

    ax.set_title("Random Walk")
    ax.set_aspect('equal')

    plt.show()

    keep_running = input(
        "Make another walk? (y/n): "
    )

    if keep_running.lower() == 'n':
        break