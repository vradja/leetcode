import itertools

import matplotlib.pyplot as plt
import squarify
import webcolors
from PIL import Image
from scipy.spatial import KDTree


def populate_space_db():
    names, positions = list(), list()
    for name, hex_val in webcolors.CSS3_NAMES_TO_HEX.items():
        names.append(name)
        positions.append(webcolors.hex_to_rgb(hex_val))
    return KDTree(positions), names


def populate_colours_count_dict(space_db, names, data, size):
    colors_count = dict()
    for count, rgb in data:
        dist, index = space_db.query(rgb)
        color = names[index]
        if color not in colors_count:
            colors_count[color] = count
        else:
            colors_count[color] += count

    colors_count = {k: v for k, v in sorted(colors_count.items(), key=lambda item: item[1], reverse=True)}
    return dict(itertools.islice(colors_count.items(), size))


# Enter Image's Absolute Path
im = Image.open('/Users/vradja/Desktop/img_tanvi.jpg')
data = im.getcolors(im.size[0] * im.size[1])
space_db, names = populate_space_db()
colors_count = populate_colours_count_dict(space_db, names, data, 7)  # Enter size / top no of colors to display

sum = 0
for (key, value) in colors_count.items(): sum += value
for key, value in colors_count.items():
    percentage = value / (sum + 0.0)
    print("percentage of '%s' is %.2f %%" % (key, percentage * 100))

# Plot histogram from colors_count dictionary
plt.bar(list(colors_count.keys()), colors_count.values(), color=colors_count.keys())
plt.xticks(rotation='vertical')
plt.show()

plt.rc('font', size=14)
squarify.plot(sizes=colors_count.values(), label=colors_count.keys(),
              color=colors_count.keys(), alpha=0.7)
plt.axis('off')
plt.show()

pass
