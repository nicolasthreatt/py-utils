'''
NumPy Plotting
'''

# %%
import numpy as np
import matplotlib.pyplot as plt

# %matplotlib inline

# %%
'''
Figures and Subplots
    - Figure
        + Container that holds all elements of plot(s)
    - Subplot
        + Appears within a rectangular grid within a figure
'''

plt_figure = plt.figure('Figure Name Here')

# Create subplots that share the same figure
subplot_1 = plt_figure.add_subplot(2, 3, 1)
subplot_6 = plt_figure.add_subplot(2, 3, 6)

plt.plot(np.random.rand(50).cumsum(), 'k--')
plt.show()

# Create new plot with seperate figure
subplot_2 = plt_figure.add_subplot(2, 3, 2)
plt.plot(np.random.rand(50).cumsum(), 'go')
plt.show()

# Create new subplot with each subplot labeled
fig = plt.figure()
for i, label in enumerate(('A', 'B', 'C', 'D')):
    ax = fig.add_subplot(2, 2, i+1)
    ax.text(0.05, 0.95, label, transform=ax.transAxes,
            fontsize=16, fontweight='bold', va='top')

plt.show()


# %%
'''
Tick Marks, Labels, and Grids

Line styles for grid lines:
    + <li>-    solid line</li>
    + <li>--   dashed line</li>
    + <li>-.   dash dot line</li>
    + <li>:    dotted</li>
'''

number_of_data_points = 1000

# Create figure
my_figure = plt.figure()

# Subplot of 1
subplot_1 = my_figure.add_subplot(1, 1, 1)
subplot_1.plot(np.random.rand(number_of_data_points).cumsum())

# Create tick marks for x-axis
number_of_ticks = 5
ticks = np.arange(0, number_of_data_points,
                  number_of_data_points//number_of_ticks)
subplot_1.set_xticks(ticks)
labels = subplot_1.set_xticklabels(
    ['one', 'two', 'three', 'four', 'five'], rotation=45, fontsize='small')

# Add Plot Title and X-Axis Label
subplot_1.set_title("Title Here")
subplot_1.set_xlabel("X-Axis Label Here")

# Turn on grid
subplot_1.grid(True)

# Concatenate x and y grid lines
gridlines = subplot_1.get_xgridlines() + subplot_1.get_ygridlines()
for line in gridlines:
    line.set_linestyle(':')

# Show plot
plt.show()


# %%
'''
Plot Annotations
'''
number_of_data_points = 10

my_figure = plt.figure()
subplot_1 = my_figure.add_subplot(1, 1, 1)
subplot_1.plot(np.random.rand(number_of_data_points).cumsum())

subplot_1.text(1, 0.5, r'an equation: $E=mc^2$', fontsize=18, color='red')
subplot_1.text(1, 1.5, "Some green text here",
               family='monospace', fontsize=12, color='green')

# see: http://matplotlib.org/users/transforms_tutorial.html
# transform=subplot_1.transAxes; entire axis between zero and one
subplot_1.text(0.5, 0.5, "Text centered here", transform=subplot_1.transAxes)

subplot_1.annotate('arrow here', xy=(2, 1), xytext=(3, 4),
                   arrowprops=dict(facecolor='red', shrink=0.05))

plt.show()
