import matplotlib.pyplot as plt

x_vals = range(1, 5001)

y_vals_cube = [x**3 for x in x_vals]

plt.style.use("Solarize_Light2")
fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals_cube, c=y_vals_cube, cmap=plt.cm.Blues, s=5)

# Set the chart title and label axes.
ax.set_title("Cubed Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

# Set the size of tick labels.
ax.tick_params(labelsize=14)

plt.show()
