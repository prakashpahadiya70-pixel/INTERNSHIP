import numpy as np
import time

# -------------------------------
# Python List Performance
# -------------------------------
python_list = list(range(1000000))

start = time.time()

result = [x * 2 for x in python_list]

end = time.time()

python_time = end - start

# -------------------------------
# NumPy Array Performance
# -------------------------------
numpy_array = np.arange(1000000)

start = time.time()

result = numpy_array * 2

end = time.time()

numpy_time = end - start

# -------------------------------
# Output
# -------------------------------
print(f"Python List Time : {python_time:.2f} seconds")
print(f"NumPy Array Time : {numpy_time:.2f} seconds")

if python_time > numpy_time:
    print("\nNumPy is faster than Python Lists.")
else:
    print("\nPython Lists are faster.")