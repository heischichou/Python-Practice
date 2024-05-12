# Determine if two strings are anagrams.
# Implement a function to find the minimum number of changes required to make two strings anagrams.

def isanagram(s1, s2):
  if (len(s1) != len(s2)):
    return False

  s1, s2 = s1.lower(), s2.lower()
  s1, s2 = "".join(sorted(s1)), "".join(sorted(s2))

  return s1 == s2

def countchanges(s1, s2):
  if (len(s1) != len(s2)):
    return False

  s1, s2 = s1.lower(), s2.lower()
  s1, s2 = "".join(sorted(s1)), "".join(sorted(s2))
  count = 0

  for x in range(len(s1)):
    if(s1[x] != s2[x]):
      count += 1

  return count

print(isanagram("silent", "listen"))
print(countchanges("liar", "real"))

# Given a string, determine if the are any unique elements in it.
# Find the last unique element.

def hasunique(str):
  distinct = dict.fromkeys(str)
  for x in distinct:
    if str.count(x) == 1:
      return True

  return False

def lastunique(str):
  distinct = dict.fromkeys(str)
  unique = "None"
  for x in distinct:
    if str.count(x) == 1: unique = x

  return unique

print(hasUnique("iranianran"))
print(lastUnique("uzbek"))