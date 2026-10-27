import matplotlib.pyplot as plt

from die import Die

# Create two dice.
die_1 = Die()
die_2 = Die()

# Roll the dice.
results = [
    die_1.roll() + die_2.roll()
    for roll_num in range(1000)
]

# Analyze results.
max_result = (
    die_1.num_sides +
    die_2.num_sides
)

frequencies = [
    results.count(value)
    for value in range(
        2,
        max_result + 1
    )
]

# Plot results.
x_values = list(
    range(2, max_result + 1)
)

plt.style.use('seaborn-v0_8')

fig, ax = plt.subplots()

ax.bar(
    x_values,
    frequencies
)

ax.set_title(
    "Results of Rolling Two D6 Dice 1000 Times"
)

ax.set_xlabel(
    "Result"
)

ax.set_ylabel(
    "Frequency"
)

plt.show()