# Implement a basic string compression algorithm. (e.g., "aabcccccaaa" -> "a2b1c5a3")
# If the compressed string is not smaller than the original, return the original string.

def compress(string):
  compressed = ""
  count, length = 1, len(string)

  for x in range(length):
    if(x == length - 1 or string[x] != string[x + 1]):
      compressed += string[x] + str(count)
      count = 1
    else:
      count += 1

  return compressed

print(compress('aabbcc'))
print(compress('aabcccccaaa'))