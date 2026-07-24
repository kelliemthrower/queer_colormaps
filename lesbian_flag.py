import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

#colormap for lesbian flag
colors = ["#D62E02", "#FD9855", "#FFFFFF", "#D161A2", '#A20160'] 

# 2. Create the colormap object
lesbian = LinearSegmentedColormap.from_list("my_custom_map", colors, N=24)

# 3. Test it with sample data
data = np.linspace(-3, 3, 100).reshape(10, 10)
plt.imshow(data, cmap=lesbian)
plt.colorbar()
plt.show()
