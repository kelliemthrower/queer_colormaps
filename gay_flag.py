import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

# colormap for gay flag
colors = ["#078D70", "#26CEAA", "#98E8C1", "#7BADE2", '#5049CC', '#3D1A78'] 

# create the colormap object, N=number of colors inside the gradient, customize as needed!
gay = LinearSegmentedColormap.from_list("my_custom_map", colors, N=24)

# test it with sample data, (don't import this into your code, just for testing)
data = np.linspace(-3, 3, 100).reshape(10, 10)
plt.imshow(data, cmap=gay)
plt.colorbar()
plt.show()
