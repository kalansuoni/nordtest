import matplotlib.pyplot as plt

# First 5 cubic numbers
x_values = range(1, 6)
y_values = [x**3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()

ax.scatter(x_values, y_values, s=100)

ax.set_title("First Five Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

plt.show()