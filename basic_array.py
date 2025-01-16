import numpy as np

# Create a 1D array
arr = np.array([9, 3, 7, 1])

sum_elements = np.sum(arr)

mean_elements = np.mean(arr)

std_dev_elements = np.std(arr)

sum_elements_multiplied = sum_elements * 2
mean_elements_multiplied = mean_elements * 2
std_dev_elements_multiplied = std_dev_elements * 2

print(f"Array: {arr}")
print(f"Sum of elements: {sum_elements} (multiplied by 2: {sum_elements_multiplied})")
print(f"Mean of elements: {mean_elements} (multiplied by 2: {mean_elements_multiplied})")
print(f"Standard deviation of elements: {std_dev_elements} (multiplied by 2: {std_dev_elements_multiplied})")

