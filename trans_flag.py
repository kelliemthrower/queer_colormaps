import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# colormap for trans flag
colors = ["#5BCEFA","#F5A9B8","#FFFFFF"] 

# create the colormap object, N=number of colors inside the gradient, customize as needed!
trans = LinearSegmentedColormap.from_list("my_custom_map", colors, N=24)

# test it with sample data, (don't import this into your code, just for testing)
data = np.linspace(-3, 3, 100).reshape(10, 10)
plt.imshow(data, cmap=trans)
plt.colorbar()
plt.show()
