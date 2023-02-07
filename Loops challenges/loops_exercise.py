"""
1.Divisible By Ten
Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. 
This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list.
Every time a number is divisible by 10, a counter will be incremented and the final count will be returned.
"""

def divisible_by_ten(nums):
  counter = 0
  for i in nums:
    if i % 10 == 0:
      counter += 1
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))
# Output : 3


"""
2. Greetings
You are invited to a social gathering, but you are tired of greeting everyone there.
Luckily we can create a function to accomplish this task for us.
In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name.
"""

def add_greetings(names):
  greetings = []
  for i in names:
    greetings.append("Hello, "+str(i))
  return greetings

print(add_greetings(["Owen", "Max", "Sophie"]))
# Output : ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

"""
3. Delete Starting Even Numbers
Let’s try a tricky challenge involving removing elements from a list.
This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements.
It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed.
"""

def delete_starting_evens(lst):
  while len(lst)>0 and lst[0] % 2 == 0:
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))
# Output 1: [11, 12, 15]
# Output 2: []