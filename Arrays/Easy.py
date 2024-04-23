# Given an array of integers, find the sum of all elements.
# Find the maximum and minimum elements in the array.

def sum(arr):
  _sum = 0
  
  for x in arr:
    _sum += x

  return _sum

def min(arr):
  return sorted(arr)[0]

def max(arr):
  return sorted(arr, reverse=True)[0]

arr = [1, 2, 3, 4, 5]
print(sum(arr))
print(min(arr))
print(max(arr))