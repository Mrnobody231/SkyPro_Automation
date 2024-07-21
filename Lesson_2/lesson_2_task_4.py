def fizz_buzz(n):
    if (n % 3 == 0) and (n % 5 == 0):
     return "FizzBuzz"
    elif (n % 3 == 0 ):
     return "Fizz"
    elif (n % 5 == 0):
     return "Buzz"
    else :
     return n
    
      
for number in range (1, 55):
   result = fizz_buzz(number)
   print (result)