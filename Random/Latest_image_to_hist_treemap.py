import os, squarify
from collections import Counter
import matplotlib.pyplot as plt
from PIL import Image
from sklearn.cluster import KMeans


# This is the clustering algorithm:
def k_means(data, size, file_path):
    # Performing k_means clustering algorithm for all pixels' RGB of the image:
    kmeans = KMeans(n_clusters=size).fit(data)
    centroids = kmeans.cluster_centers_
    cluster_colors = [(int(a[0]), int(a[1]), int(a[2])) for a in centroids]
    cluster_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    sizes = Counter(kmeans.labels_).values()

    # Plot Histogram from clusters:
    plt.bar(cluster_hex_colors, sizes, color=cluster_hex_colors)
    plt.xticks(rotation='vertical')
    plt.show()

    # Plot TreeMap with labels of clusters:
    plt.rc('font', size=14)
    plt.figure(figsize=(15, 15))
    plt.suptitle(file_path, fontsize=20)
    squarify.plot(sizes=sizes, label=cluster_hex_colors,
                  color=cluster_hex_colors, alpha=0.7)
    plt.axis('off')
    plt.show()

    # Plot TreeMap without labels of clusters
    plt.rc('font', size=14)
    plt.figure(figsize=(15, 15))
    squarify.plot(sizes=sizes,
                  color=cluster_hex_colors, alpha=0.7)
    plt.axis('off')
    plt.show()


# This is the user input code block:
# Enter Image's Absolute Path:
path = '/Users/tanvimodi/Desktop/Van_Gogh/poppies_full 1886.jpg'
merge = False
size = 7

# This is where file, folder/directory & merge of images are performed:
cumulative_data = list()

# This is for file input:
if os.path.isfile(path):
    im = Image.open(path)
    data = im.getcolors(im.size[0] * im.size[1])
    for d in data:
        cumulative_data += [d[1]] * d[0]
    k_means(cumulative_data, size, path)

# This is for folder input:
if os.path.isdir(path):
    # This is to merge the images in the folder and then cluster:
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
    # This is to cluster each image seperately in the folder:
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
