import matplotlib.pyplot as plt
import squarify

percentages = [28.56, 28.09, 22.02, 15.66, 5.67]
color_names = ['kashmir blue', 'blue charcoal', 'resolution blue', 'forcefield', 'iko']
colors = ['#577091', '#272B2E', '#33457B', '#829290', '#A8A66C']

plt.rc('font', size=14)
plt.figure(figsize=(10, 10))
squarify.plot(sizes=percentages, label=color_names,
              color=colors, alpha=0.7)
plt.axis('off')
plt.show()

# # Plot histogram from colors_count dictionary
plt.suptitle('hehehehe', fontsize=20)
plt.bar(color_names, percentages, color=colors)
plt.xticks(rotation='vertical')
plt.show()
