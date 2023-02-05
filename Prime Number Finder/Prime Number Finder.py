def prime_finder(n):
  # Write your code here
    number = [*range(1,n+1)]
    final= []
    def is_prime(n):
        flag = 0
        for i in range(2,n):
            if n % i == 0:
                flag += 1
        if flag == 0:
            return True
        else:
            return False
    for k in number:
        if is_prime(k) == True:
            final.append(k)
    return final[1:]
        
print(prime_finder(11))

# Output [2, 3, 5, 7, 11]

print(prime_finder(31))

# Outtput [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]

#For example, prime_finder(11) should return [2, 3, 5, 7, 11]