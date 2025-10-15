import heapq
import random
import time
import math
import matplotlib.pyplot as plt

# Minimal merge cost using heap of list sizes
def merge_cost_using_heap(sizes):
    heapq.heapify(sizes)
    total_cost = 0

    while len(sizes) > 1:
        first = heapq.heappop(sizes)
        second = heapq.heappop(sizes)
        cost = first + second
        total_cost += cost
        heapq.heappush(sizes, cost)

    return total_cost

n_values = [1000, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000]

# Generating size arrays, not included in experimental time
pre_generated_sizes = []
for n in n_values:
    sizes = [random.randint(1, 1000) for _ in range(n)] # Each array contains random list sizes between 1 and 1000
    pre_generated_sizes.append(sizes)

# Experimental time
experimental_times = []
total_costs = []
for i, n in enumerate(n_values):
    sizes = pre_generated_sizes[i].copy()
    start_time = time.perf_counter_ns()
    total_cost = merge_cost_using_heap(sizes)
    end_time = time.perf_counter_ns()
    time_taken = end_time - start_time
    experimental_times.append(time_taken)
    total_costs.append(total_cost)
    print(f"n = {n}, Total merge cost = {total_cost}, Experimental time = {time_taken:.2f} ns")

# Theoretical complexity O(n log n)
theoretical_raw = [n * math.log2(n) for n in n_values]

# Normalization (scaling constant)
numerator = sum(experimental_times[i] * theoretical_raw[i] for i in range(len(n_values)))
denominator = sum(theoretical_raw[i] ** 2 for i in range(len(n_values)))
c = numerator / denominator
theoretical_scaled = [c * val for val in theoretical_raw]

print(f"\nScaling constant (c) = {c:.6f}")
print("Theoretical raw:", theoretical_raw)
print("Theoretical scaled:", theoretical_scaled)

# Plot
plt.figure(figsize=(8,5))
plt.plot(n_values, experimental_times, 'o-', label="Experimental Time")
plt.plot(n_values, theoretical_scaled, 's-', label="Theoretical Time (scaled)")
plt.xlabel("Number of lists (n)")
plt.ylabel("Time (ns)")
plt.title("Experimental vs Theoretical Complexity for Merging Sorted Lists (O(n log n))")
plt.legend()
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.show()