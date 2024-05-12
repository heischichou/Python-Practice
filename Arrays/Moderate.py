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

# Given a high-value input, display each number from 1 to the given number with the ff. constraints:
# Multiples of 3 are excluded (i.e. not displayed).
# Multiples of 2 are displayed as negative.
# Multiples of 2 & 3 are displayed as zero.

def displayrange(num):
  _range = list(range(num + 1))
  string = ""
  for x in _range:
    if x % 3 != 0:
      if x % 2 == 0: string += str(-x) + " "
      elif x % 2 == 0 and x % 3 == 0: string += str(0) + " "
      else: string += str(x) + " "
  
  return string

print(displayRange(30))
