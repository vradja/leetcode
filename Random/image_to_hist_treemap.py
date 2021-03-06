import colorsys
import os
from collections import Counter

import matplotlib.pyplot as plt
import squarify
from PIL import Image
from sklearn.cluster import KMeans


def get_hsv(hexrgb):
    hexrgb = hexrgb.lstrip("#")  # in case you have Web color specs
    r, g, b = (int(hexrgb[i:i + 2], 16) / 255.0 for i in range(0, 5, 2))
    return colorsys.rgb_to_hsv(r, g, b)


def sort_sizes(colors_list, cluster_hsv_hex_colors, counter_labels):
    sizes = list()
    for color in cluster_hsv_hex_colors:
        sizes.append(counter_labels[colors_list.index(color)])
    return sizes


def k_means(data, size, file_path):
    kmeans = KMeans(n_clusters=size).fit(data)
    centroids = kmeans.cluster_centers_
    print(centroids)
    cluster_colors = [(int(a[0]), int(a[1]), int(a[2])) for a in centroids]
    cluster_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    cluster_hsv_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    cluster_hsv_hex_colors.sort(key=get_hsv)
    print(cluster_hex_colors)

    sizes = sort_sizes(cluster_hex_colors,cluster_hsv_hex_colors, Counter(kmeans.labels_))

    # Plot histogram from colors_count dictionary
    plt.bar(cluster_hsv_hex_colors, sizes, color=cluster_hsv_hex_colors)
    plt.xticks(rotation='vertical')
    plt.show()

    # Most common
    sizes = Counter(kmeans.labels_).most_common()
    cluster_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    cluster_hex_descending = list()

    for index, value in sizes:
        cluster_hex_descending.append(cluster_hex_colors[index])

    sizes = list(dict(sizes).values())

    plt.rc('font', size=14)
    plt.figure(figsize=(7, 7))
    plt.suptitle(file_path, fontsize=20)
    squarify.plot(sizes=sizes, label=cluster_hex_descending,
                  color=cluster_hex_descending, alpha=0.7)
    plt.axis('off')
    plt.show()

    plt.rc('font', size=14)
    plt.figure(figsize=(7, 7))
    squarify.plot(sizes=sizes,
                  color=cluster_hex_descending, alpha=0.7)
    plt.axis('off')
    plt.show()


# Enter Image's Absolute Path
path = '/Users/vradja/Desktop/03.jpg'
merge = False
size = 7
cumulative_data = list()

if os.path.isfile(path):
    im = Image.open(path)
    data = im.getcolors(im.size[0] * im.size[1])
    for d in data:
        cumulative_data += [d[1]] * d[0]
    k_means(cumulative_data, size, path)

if os.path.isdir(path):
    if merge:
        data = list()
        for file in os.listdir(path):
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"):
                file_path = path + '/' + file
                im = Image.open(file_path)
                data += im.getcolors(im.size[0] * im.size[1])
        for d in data:
            cumulative_data += [d[1]] * d[0]
        k_means(cumulative_data, size, path)
    else:
        for file in os.listdir(path):
            cumulative_data = list()
            filename = os.fsdecode(file)
            if filename.endswith(".jpg"):
                file_path = path + '/' + file
                im = Image.open(file_path)
                data = im.getcolors(im.size[0] * im.size[1])
                for d in data:
                    cumulative_data += [d[1]] * d[0]
                k_means(cumulative_data, size, file_path)