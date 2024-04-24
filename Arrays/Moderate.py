# Given an array of integers, determine if it contains any duplicate elements.
# Find the first duplicate element in the array.

def hasduplicate(arr):
  for n in arr:
    if(arr.count(n) > 1): return True

  return False

def find_duplicate_loop(arr):
  length = len(arr)
  for x in range(length):
    for y in range(x + 1, length):
      if(arr[x] == arr[y]):
        return y

  return -1

def find_duplicate_set(arr):
  unique = dict.fromkeys(arr[:])
  string = "".join([str(x) for x in arr])
  for x in unique:
    if(arr.count(x) > 1):
      x = str(x)
      return string.find(x, string.find(x) + 1)

  return -1

arr1 = [5, 4, 4, 3, 2, 1]
arr2 = [1, 2, 3, 4, 5]
print(find_duplicate_loop(arr1))
print(hasduplicate(arr2))
