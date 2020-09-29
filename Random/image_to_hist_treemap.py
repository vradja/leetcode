import os
from collections import Counter

import matplotlib.pyplot as plt
import squarify
from PIL import Image
from sklearn.cluster import KMeans


def k_means(data, size):
    kmeans = KMeans(n_clusters=size).fit(data)
    centroids = kmeans.cluster_centers_
    print(centroids)
    cluster_colors = [(int(a[0]), int(a[1]), int(a[2])) for a in centroids]
    cluster_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    sizes = Counter(kmeans.labels_).values()

    # Plot histogram from colors_count dictionary
    plt.bar(cluster_hex_colors, sizes, color=cluster_hex_colors)
    plt.xticks(rotation='vertical')
    plt.show()

    plt.rc('font', size=14)
    squarify.plot(sizes=sizes, label=cluster_hex_colors,
                  color=cluster_hex_colors, alpha=0.7)
    plt.axis('off')
    plt.show()

    plt.rc('font', size=14)
    squarify.plot(sizes=sizes,
                  color=cluster_hex_colors, alpha=0.7)
    plt.axis('off')
    plt.show()


# Enter Image's Absolute Path
path = '/Users/vradja/Desktop/img_tanvi.jpg'
merge = False
size = 7
cumulative_data = list()

if os.path.isfile(path):
    im = Image.open(path)
    data = im.getcolors(im.size[0] * im.size[1])
    for d in data:
        cumulative_data += [d[1]] * d[0]
    k_means(cumulative_data, size)

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
        k_means(cumulative_data, size)
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
                k_means(cumulative_data, size)