from heapq import *


def find_maximum_capital(Capital, Profits, numberOfProjects, initialCapital):
    max_heap = []
    # min_heap = sorted(zip(Capital, Profits), key=lambda l: l[0])
    min_heap = sorted(zip(Capital, Profits))  # no need for , key=lambda l: l[0].
    # Use only if you want to sort based on , key=lambda l: l[1]

    for _ in range(numberOfProjects):
        # # for _ in min_heap:  # DO NOT DO THIS, SINCE WE DO HEAPPOP, THE MIN_HEAP GETS CORRUPTED DURING ITERATION
        # for _ in range(len(min_heap)): # WHILE IS BETTER THAN FOR IN THIS SCENARIO.
        #     if min_heap[0][0] <= initialCapital:
        while min_heap and min_heap[0][0] <= initialCapital:
            # While is better than FOR for 2 conditional and statements
            # profit = heappop(min_heap)[1] # NO NEED FOR profit[index], since we already zipped them together.
            heappush(max_heap, -heappop(min_heap)[1])

        if max_heap:
            initialCapital -= heappop(max_heap)
        else:
            break  # stop here and breakout if no max_heap is available.
    return initialCapital


def find_maximum_capital_1(capital, profits, numberOfProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    # insert all project capitals to a min-heap
    for i in range(0, len(profits)):
        heappush(minCapitalHeap, (capital[i], i))

    # let's try to find a total of 'numberOfProjects' best projects
    availableCapital = initialCapital
    for _ in range(numberOfProjects):
        # find all projects that can be selected within the available capital and insert them in a max-heap
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        # terminate if we are not able to find any project that can be completed within the available capital
        if not maxProfitHeap:
            break

        # select the project with the maximum profit
        availableCapital += -heappop(maxProfitHeap)[0]

    return availableCapital


def main():
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
          str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))
    print(str(find_maximum_capital([0, 1, 1], [1, 2, 3], 2, 0)))


main()
