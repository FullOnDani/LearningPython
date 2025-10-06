1 == 1
#1 is equal to 1 and output is True

2 == 1
#will print False

var = 12
print(var == 1)
#will print False

1 != 1
#1 is not equal to 1will print False

2 != 1
#will print True

2 > 1
#2 greater than 1 True

  #  centigrade_outside >= 0.0 Greater than or equal to

  # current_velocity_mph < 85  # Less than
  # current_velocity_mph <= 85  # Less than or equal to

#storing the answers in variables
  # ans = numberoflions >= numberoflionesses

#input n and determine if its < or > 100
n = int(input("Enter a number: "))
print("Your number is Greater or Equal to 100:" , n >= 100)

#read two number and show which is larger
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
num3 = int(input("Enter a number: "))


#conditional statements
if  num2 > num1:
    larger_number = num2
else:
    larger_number = num1
if num3 > larger_number:
    larger_number = num3

#print the result
print("The larger number is:" , larger_number)

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))
 
# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.
 
largest_number = max(number1, number2, number3)
 
# Print the result.
print("The largest number is:", largest_number)



