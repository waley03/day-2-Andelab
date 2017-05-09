
"""THIS IS FIZZBUZZ PROGRAM"""

print ("The program prints either 'Fizz' 'Buzz' or 'FizzBuzz' depending on the input provide")
print ("")
number = int(input("Please enter your input to proceed: "))


"Code will run if input is a number"
try:
  def fizzBuzz(number):
    if type(number)!= int:
        return 'invalid input'
    elif (number <= 0):
      return "Number must be greater than zero"
    
    elif (number % 3 == 0 and number % 5 == 0):
      return 'FizzBuzz'
    
    elif(number % 5 == 0):
      return 'Buzz'
    
    elif (number % 3 == 0):
      return 'Fizz'

    else:
      return str(number)+(" is not disible by neither of 3 nor 5")
  print (fizzBuzz(number))
  print ("")
  
except ValueError:
  print ("")
  print ("Input is not a number. Please try again: ")

