import heapq
import random
import time
import math
import matplotlib.pyplot as plt

# To actually merge two sorted lists
def merge_two_sorted_lists(list1, list2):
    merged = []
    i = j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # append remaining
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# To merge multiple sorted lists using a min-heap
def merge_sorted_lists(lists):
    # heap contains tuples of (list_size, list_data)
    heap = [(len(lst), lst) for lst in lists]
    heapq.heapify(heap)

    total_cost = 0

    while len(heap) > 1:
        # extract two smallest lists
        len1, list1 = heapq.heappop(heap)
        len2, list2 = heapq.heappop(heap)

        # merge them
        merged = merge_two_sorted_lists(list1, list2)
        cost = len1 + len2
        total_cost += cost

        # push merged list back into heap
        heapq.heappush(heap, (len(merged), merged))

    final_list = heap[0][1]
    return final_list, total_cost

n_values = [5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000]

# Generation of lists, not included in experimental time
pre_generated_sets = []
for n in n_values:
    lists = []
    for _ in range(n):
        length = random.randint(1, 50)  # random length for each list
        each_list = sorted(random.sample(range(1, 10000), length))
        lists.append(each_list)
    pre_generated_sets.append(lists)

# Measure runtime and cost
experimental_times = []
for i, n in enumerate(n_values):
    lists = pre_generated_sets[i]
    start_time = time.perf_counter_ns()
    merged, total_cost = merge_sorted_lists(lists)
    end_time = time.perf_counter_ns()
    time_taken = end_time - start_time
    experimental_times.append(time_taken)
    print(f"k = {n}, Total cost = {total_cost}, Experimental time = {time_taken:.2f} ns, Final merged length = {len(merged)}")

# Theoretical complexity O(n log n)
theoretical_raw = [n * math.log2(n) for n in n_values]

# Normalize theoretical data
mid_index = len(n_values) // 2
c = experimental_times[mid_index] / theoretical_raw[mid_index]
theoretical_scaled = [c * val for val in theoretical_raw]

# Printing c, theoretical raw and scaled
print(f"Scaling constant (c) = {c:.6f}")
print(f"Theoretical raw values = {theoretical_raw}")
print(f"Theoretical adjusted values = {theoretical_scaled}")

# Plot
plt.figure(figsize=(8,5))
plt.plot(n_values, experimental_times, 'o-', label="Experimental Time")
plt.plot(n_values, theoretical_scaled, 's-', label="Theoretical Time (scaled)")
plt.xlabel("Number of lists")
plt.ylabel("Time (ns) ")
plt.title("Experimental vs Theoretical Complexity for Merging Sorted Lists (O(n log n))")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()