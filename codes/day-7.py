# list comprehension.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = (num for num  in range(0,11) if num % 2 == 0)
odd = (num for num in range(0,11) if num % 2 != 0)

print ("Eeve numbers: ",  list(even))
print ("odd numbers: ", list(odd))