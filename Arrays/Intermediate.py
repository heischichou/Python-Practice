# Implement an algorithm to rotate an array by x steps.
# Rotate the array in-place without using extra space.

def rotateleft(arr, x):
  # Uncomment if returning deep copy of array instead
  # arr = arr[:]

  for _ in range(x):
    arr.append(arr.pop(0))

  return arr

def rotateright(arr, x):
  # Uncomment if returning deep copy of array instead
  # arr = arr[:]

  for _ in range(x):
    arr.insert(0, arr.pop())

  return arr

arr = [5, 3, 2, 4, 1]
k = 2
print(rotateleft(arr, k))
print(rotateright(arr, k))