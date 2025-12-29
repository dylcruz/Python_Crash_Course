import matplotlib.pyplot as plt
from die import Die

# Create a D6.
die_1 = Die(6)
die_2 = Die(6)

# Make some rolls, and store results in a list
results = [die_1.roll() + die_2.roll() for _ in range(50_000)]

# Analyze the results.
max_result = die_1.num_sides + die_2.num_sides
poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

# Visualize the results.
plt.bar(poss_results, frequencies)
plt.xlabel("Result")
plt.ylabel("Frequency of Result")
plt.title("Results of Rolling Two D6 50,000 Times")

plt.show()