import numpy as np

# Figure settings
### FIGURE SIZES
fig_width_pt = 2*246.0  # Get this from LaTeX using \the\columnwidth (this is for prd)
inches_per_pt = 1.0 / 72.27               # Convert pt to inch
golden_mean = (np.sqrt(5) - 1.0) / 2.0         # Aesthetic ratio
fig_width = fig_width_pt * inches_per_pt  # width in inches
fig_height = fig_width * golden_mean      # height in inches
print(fig_width)
square_size = [fig_width, fig_width]
rect_size = [fig_width, fig_height]
long_size = [1.5 * fig_width, fig_height]
longest_size = [2 * fig_width, fig_height]
vert_rect_size = [fig_width, 2*fig_height]
vert_square_size = [fig_width, 2*fig_width]
vert_long_size = [1.5 * fig_width, 2*fig_height]

#You can use the constants above as standard figure sizes.

# The parameters below are suitable for plots. You need to import them as rcparams
params = {'axes.labelsize': 18,
          'axes.titlesize': 24,
          'font.size': 18,
          'legend.fontsize': 18,
          'font.family': 'serif',
          'font.sans-serif': ['Bitstream Vera Sans'],
          'font.serif': ['Bitstream Vera'],
          'xtick.labelsize': 18,
          'ytick.labelsize': 18,
          'text.usetex': True,
          'text.latex.preamble': r"""\usepackage{amsmath} \usepackage{amssymb} \usepackage{amsfonts}""",
          'figure.figsize': rect_size,
         }

# To import them into matplotlib use
# plt.rcParams.update(my_params)
# If you create a figure using the sizes provided above
# plt.figure(rect_size)
# ...plot stuff...
# Save it and get rid of white around the figure.
# plt.savefig("plot.pdf", bbox_inches="tight")
# I find this matching with my target size when I set the width of the plot in LaTeX as 0.8\columwidth
