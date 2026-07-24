import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# colormap for pride flag
colors = ["#000000", "#613915", "#FFAFC8","#FFFFFF", "#74D7EE", "#E40303","#FF8C00", "#FFED00", "#008026", "#004DFF", "#750787"] 

# create the colormap object, N=number of colors inside the gradient, customize as needed!
pride = LinearSegmentedColormap.from_list("my_custom_map", colors, N=44)

# test it with sample data, (don't import this into your code, just for testing)
data = np.linspace(-3, 3, 100).reshape(10, 10)
plt.imshow(data, cmap=pride)
plt.colorbar()
plt.show()
