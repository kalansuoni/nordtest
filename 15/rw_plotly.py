from plotly.graph_objects import Scatter, Figure

from random_walk import RandomWalk

rw = RandomWalk(5000)
rw.fill_walk()

point_numbers = list(range(rw.num_points))

fig = Figure()

fig.add_trace(
    Scatter(
        x=rw.x_values,
        y=rw.y_values,
        mode='markers',
        marker=dict(
            size=4,
            color=point_numbers,
            colorscale='Viridis'
        )
    )
)

fig.update_layout(
    title='Random Walk',
    xaxis_title='X',
    yaxis_title='Y'
)

fig.show()
