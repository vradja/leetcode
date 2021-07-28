import sys
from collections import Counter

for line in sys.stdin:
    word = [ch for ch in line.lower() if ch.isalpha()]
    descending_sorted_counter = Counter(word).most_common()
    sorted_frequencies = (list(map(lambda x: x[1], descending_sorted_counter)))

    beauty_factor = 26
    beauty_value = 0

    for frequency in sorted_frequencies:
        beauty_value += beauty_factor * frequency
        beauty_factor -= 1

    print(beauty_value)
