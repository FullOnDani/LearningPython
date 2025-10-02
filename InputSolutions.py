# program to find the hypotenuse of a triangle

opp = float(input("Enter the length of the Opposite side: "))
adj = float(input("Enter the length of the Adjacent side: "))
hypo = (opp**2 +adj**2)**0.5
print("The Hypotenuse is: ", hypo)

# removing the hypo function

opp = float(input("Enter the length of the Opposite side: "))
adj = float(input("Enter the length of the Adjacent side: "))
print("The Hypotenuse is: ", (opp**2 +adj**2)**.5)

#conversion to string
opp = float(input("Enter the length of the Opposite side: "))
adj = float(input("Enter the length of the Adjacent side: "))
print("The Hypotenuse is: " + str((opp**2 +adj**2)**.5))

#+ in strings (concatenation)
fname = input("Input your first name ")
lname = input("Input your last name ")
print("Thank you")
print("Your full name is :" , fname + " " + lname ,end=".")

#test
a = float(input("Input A "))
b = float(input("Input B "))

print(a+b)
print(a-b)
print(a*b)
print(a/b)

print("\nThat's all, folks!")


