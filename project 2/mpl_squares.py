import matplotlib.pyplot as plt

squares = [x**2 for x in range(0, 21)]

fig, ax = plt.subplots()
ax.plot(squares, linewidth=3)

# Set the chart title and label axes.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

plt.show()