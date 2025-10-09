# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

#Read the first number
number = int(input("Enter a number or type 0 to stop: "))

#terminate the action
while number != 0:
    #Check if the number is odd
    if number % 2 == 1:
        #increase the number of oddnumbers
        odd_numbers += 1
    else:
        #increase the number of evenumbers
        even_numbers += 1
    #read next number
    number = int(input("Enter a number or type 0 to stop: "))
    

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)

