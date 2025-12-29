import plotly.express as px
from random_walk import RandomWalk

# Keep making new walks, as long as the program is active
while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Plot the points in the walk
    point_numbers = range(rw.num_points)
    fig = px.scatter(x=rw.x_values, y=rw.y_values)
    fig.update_layout(
        yaxis_scaleanchor="x",
        yaxis_scaleratio=1,
    )
    fig.update_traces(marker=dict(size=5))

    # Emphasize the first and last points
    fig.add_scatter(x=[0], y=[0], marker=dict(color='green', size=20))
    fig.add_scatter(x=[rw.x_values[-1]], y=[rw.y_values[-1]],
                    marker=dict(color='red', size=20))

    # Remove the axes.
    fig.update_xaxes(visible=False)
    fig.update_yaxes(visible=False)

    fig.show()
    
    keep_running = input("Make another walk? (y/n): ")
    if keep_running.lower() == 'n':
        break