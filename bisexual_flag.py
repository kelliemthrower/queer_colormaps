import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# colormap for bisexual flag
colors = ["#D60270", "#9B4F96", "#0038A8"] 

# create the colormap object, N=number of colors inside the gradient, customize as needed!
bisexual = LinearSegmentedColormap.from_list("my_custom_map", colors, N=24)

# test it with sample data, (don't import this into your code, just for testing)
data = np.linspace(-3, 3, 100).reshape(10, 10)
plt.imshow(data, cmap=bisexual)
plt.colorbar()
plt.show()
