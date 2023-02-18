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

"""
4. Odd Indices
This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements.
"""

def odd_indices(lst):
    odd_list = []
    for i in range(1,len(lst),2):
        odd_list.append(lst[i])
    return odd_list

print(odd_indices([4, 3, 7, 10, 11, -2]))
# Output : [3, 10, -2]

"""
5. Exponents
In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers.
"""

def exponents(bases,power):
    new_lst = []
    for i in bases:
        for k in power:
            new_lst.append(i**k)
    return new_lst

print(exponents([2, 3, 4], [1, 2, 3]))
# Output : [2, 4, 8, 3, 9, 27, 4, 16, 64]

"""
6. Larger Sum
We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum.
"""

def larger_sum(lst1,lst2):
    sum_list1 = 0
    sum_list2 = 0
    for i in lst1:
        sum_list1 += i
    for j in lst2:
        sum_list2 += j
    if sum_list1 >= sum_list2:
        return lst1
    else:
        return lst2

print(larger_sum([1, 9, 5], [2, 3, 7]))
# Output : [1,9,5]

"""
7. Over 9000
We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped.
"""

def over_nine_thousand(lst):
    total = 0 
    for i in lst:
        total +=i
        if total > 9000:
            break
    return total

print(over_nine_thousand([8000, 900, 120, 5000]))
# Output : 9020

"""
8. Max Num
Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function.
"""

def max_num(nums):
    maximum = nums[0]
    for i in nums:
        if i > maximum:
            maximum = i
        else:
            maximum = maximum
    return maximum

print(max_num([50, -10, 0, 75, 20]))
# Output : 75

"""
9. Same Values
In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index.
"""

def same_values(lst1,lst2):
    same_lst = []
    for i in range(0,len(lst1)):
        if lst1[i] == lst2[i]:
            same_lst.append(i)
    return same_lst

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
# Output : [0, 2, 3]

"""
10. Reversed List
For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list.
"""

def reversed_list(lst1,lst2):
    for i in range(len(lst1)):
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False
    return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
# Output1 : True
# Output2 : False
