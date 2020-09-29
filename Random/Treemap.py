import numpy as np
import matplotlib.pyplot as plt
import squarify

volume = [20091, 26431, 26019, 27569, 28374, 25499, 25043, 23110, 19403, 10826]
labels = ['#4BB888', '#A4004B', '#D2730', '#767011', '#D2A5A7', '#8D9306', '#37D83E', '#603559', '#BA2103', '#239D55']
color_list = ['#4BB888', '#A4004B', '#D2730', '#767011', '#D2A5A7', '#8D9306', '#37D83E', '#603559', '#BA2103', '#239D55']

plt.rc('font', size=14)
squarify.plot(sizes=volume, label=labels,
              color=color_list, alpha=0.7)
plt.axis('off')

plt.show()