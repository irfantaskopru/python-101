def fizzbuzz(limit):
  # Write your code here
  result_list = []
  numbers = [*range(1,limit+1)]
  for i in numbers:
      if i % 5 ==0:
          if i % 3 == 0:
            result_list.append("FizzBuzz")
          else:
            result_list.append("Buzz")
      elif i % 3 == 0:
          result_list.append("Fizz")
      
      else:
          result_list.append(i)
  return result_list

print(fizzbuzz(16))

# Output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16]

print(fizzbuzz(30))

# Output: [1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19, 'Buzz', 'Fizz', 22, 23, 'Fizz', 'Buzz', 26, 'Fizz', 28, 29, 'FizzBuzz']

