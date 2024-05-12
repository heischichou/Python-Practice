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

# Given a string of integers separated by whitespaces, determine if the integers are sorted in ascending order.
# Do the same for descending order.

def in_ascending_order(sequence):
  sequence = sequence.split()
  integers = "".join(sorted(sequence))

  return "".join(sequence) == integers

def in_descending_order(sequence):
  sequence = sequence.split()
  integers = "".join(sorted(sequence, reverse=True))

  return "".join(sequence) == integers

print(in_ascending_order("1 3 3 7"))
print(in_ascending_order("4 5 1 6"))
print(in_descending_order("8 7 6 5"))