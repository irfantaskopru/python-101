"""
Append Size
For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list
"""

def append_size(my_list):
  length = len(my_list)
  my_list.append(length)
  return my_list

print(append_size([23, 42, 108]))
# Output : [23, 42, 108, 3]

"""
Append Sum
Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end.
After doing so, it will repeat this process two more times and return the resulting list.
You can choose to use a loop or manually use three lines.
"""
def append_sum(my_list):
  my_list.append(my_list[-1]+my_list[-2])
  print(my_list)
  my_list.append(my_list[-1]+my_list[-2])
  print(my_list)
  my_list.append(my_list[-1]+my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))
# Output : [1, 1, 2, 3, 5, 8]

"""
Larger List
Let’s say we are working with two conveyor belts that contain items represented by a numerical ID.
If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt.
In the case where they have the same number of items, return the last item from the first conveyor belt.
In our code, we can represent the belts using lists.
"""

def larger_list(my_list1,my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  return my_list2[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))
# Output : 5

"""
More Than N
Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type.
We have a conveyor belt full of different types of snacks represented by different numbers.
Our function will accept a list of numbers (representing the type of snack),
a number for the second parameter (the type of snack we are looking for),
and another number as the third parameter (the maximum number of that type of snack on the conveyor belt).
The function will return True if the snack we are searching for appears more times than we provided as our third parameter.
"""
def more_than_n(my_list,item,n):
  if my_list.count(item) > n:
    return True
  else:
    return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))
# Output : True

"""
Combine Sort
Finally, let’s create a function that combines two different lists together and then sorts them.
To do this we can combine the lists with an operation and then sort using a function call.
"""

def combine_sort(my_list1,my_list2):
  combined_list = my_list1 + my_list2
  return sorted(combined_list)

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))
# Output : [-10, 2, 2, 4, 5, 5, 10, 10]

"""
Every Three Numbers
Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter.
"""

def every_three_nums(start):
  list = []
  if start > 100:
    return list
  else:
    list = [*range(start,101,3)]
    return list

print(every_three_nums(91))
# Output : [91, 94, 97, 100]

"""
Remove Middle
Our next function will remove all elements from a list with an index within a certain range.
The function will accept a list, a starting index, and an ending index.
All elements with an index between the starting and ending index should be removed from the list.
"""
def remove_middle(lst,start,end):
  return lst[:start] + lst[end+1:]

# Output : [4, 23, 42]


"""
More Frequent Item
Let’s go back to our factory example.
We have a conveyor belt of items where each item is represented by a different number.
We want to know, out of two items, which one shows up more on our belt.
To solve this, we can use a function with three parameters.
One parameter for the list of items, another for the first item we are comparing, and another for the second item. 
"""

def more_frequent_item(lst,item1,item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))
# Output : 3

"""
Double Index
Our next function will double a value at a given position.
We will provide a list and an index to double.
This will create a new list by replacing the value at the index provided with double the original value.
If the index is invalid then we should return the original list.
"""

def double_index(lst,index):
  if index >= len(lst):
    return lst
  else:
    new_list = lst[0:index]
  new_list.append(lst[index]*2)
  new_list = new_list + lst[index+1:]
  return new_list

print(double_index([3, 8, -10, 12], 2))
# Output : [3, 8, -20, 12]

"""
Middle Item
For the final code challenge, we are going to create a function that finds the middle item from a list of values.
This will be different depending on whether there are an odd or even number of values.
In the case of an odd number of elements, we want this function to return the exact middle value.
If there is an even number of elements, it returns the average of the middle two elements.
"""

def middle_element(lst):
  if len(lst) % 2 == 0:
    r = lst[int(len(lst)/2)] + lst[int(len(lst)/2 - 1)]
    return r /2
  else:
      return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5]))
# Output : -7.0