from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create two D6 dice.
die_1 = Die()
die_2 = Die()

# Roll the dice 1,000 times using a list comprehension.
results = [
    die_1.roll() + die_2.roll()
    for roll_num in range(1000)
]

# Count frequencies using a list comprehension.
max_result = die_1.num_sides + die_2.num_sides

frequencies = [
    results.count(value)
    for value in range(2, max_result + 1)
]

# Create the visualization.
x_values = list(range(2, max_result + 1))

data = [
    Bar(
        x=x_values,
        y=frequencies
    )
]

my_layout = Layout(
    title='Results of Rolling Two D6 Dice 1,000 Times',
    xaxis={'title': 'Result'},
    yaxis={'title': 'Frequency of Result'}
)

offline.plot(
    {
        'data': data,
        'layout': my_layout
    },
    filename='d6_d6.html'
)