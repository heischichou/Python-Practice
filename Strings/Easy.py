# Check if a string is a palindrome.
# Ignore non-alphanumeric characters and check if the modified string is a palindrome.

# Iterative solution
def ispalindrome_iter(string):
  def oppositelettersmatch():
    return string[start] == string[end]

  string = string.lower()
  string = "".join([c for c in string if c.isalnum()])
  start, end = 0, len(string) - 1

  while(start <= end and oppositelettersmatch()):
    if oppositelettersmatch():
      start += 1
      end -= 1
  return oppositelettersmatch()

# Non-iterative solution
def ispalindrome_noniter(string):
  string = string.lower()
  string = "".join([c for c in string if c.isalnum()])
  return string == string[::-1]

print(ispalindrome_iter("racecar"))
print(ispalindrome_iter("gaming"))

# Check if a number is a palindrome.

# Iterative solution
# def ispalindrome_iter(number):
#   number = int(number)
#   original, total = number, 0
#   while(number > 0):
#     total = (total * 10) + int(number % 10)
#     number = number // 10
#   return original == total

# Non-iterative solution
# def ispalindrome_noniter(number):
#   number = str(number)
#   return number == number[::-1]

# print(ispalindrome_noniter(134))
# print(ispalindrome_noniter(1551))