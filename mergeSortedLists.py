import heapq
import random
import time
import math
import matplotlib.pyplot as plt

def merge_sorted_lists(sizes):
    heapq.heapify(sizes)
    total_cost = 0

    while len(sizes) > 1:
        first = heapq.heappop(sizes)
        second = heapq.heappop(sizes)
        cost = first + second
        total_cost += cost
        heapq.heappush(sizes, cost)

    return total_cost

n_values = [10, 50, 100, 200, 400, 800, 1600, 3200, 6400, 10000]

# Excluded from time complexity
pre_generated_lists = []
for n in n_values:
    lists = sorted([random.randint(1, 10000) for _ in range(n)])
    pre_generated_lists.append(lists)

# Experimental runtimes
experimental_times = []
for i, n in enumerate(n_values):
    lists = pre_generated_lists[i].copy()
    start_time = time.perf_counter_ns()
    merge_sorted_lists(lists)
    end_time = time.perf_counter_ns()
    time_taken = end_time - start_time
    experimental_times.append(time_taken)
    print(f"n = {n}, Time taken = {time_taken:.2f} ns")

# Theoretical complexity O(n log n)
theoretical_raw = [n * math.log2(n) for n in n_values]

# Normalization (scaling constant)
mid_index = len(n_values) // 2
c = experimental_times[mid_index] / theoretical_raw[mid_index]
theoretical_scaled = [c * val for val in theoretical_raw]

print(f"\nScaling constant c = {c:.6f}")
print("Experimental times:", experimental_times)
print("Theoretical raw:", theoretical_raw)
print("Scaled theoretical:", theoretical_scaled)

# Plotting experimental vs theoretical results
plt.figure(figsize=(8,5))
plt.plot(n_values, experimental_times, 'o-', label="Experimental Time")
plt.plot(n_values, theoretical_scaled, 's-', label="Theoretical Time (scaled)")
plt.xscale('log')
plt.yscale('log')
plt.xlabel("n (log scale)")
plt.ylabel("Time (ns, log scale)")
plt.title("Experimental vs Theoretical Complexity for Merging Sorted Lists (O(n log n))")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()