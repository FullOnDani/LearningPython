# returns value for i to be from 0 to 9
for i in range(10):
    print("The value of i is currently", i)

#returns value for i to be 2 to 7
for i in range(2, 8):
    print("The value of i is currently", i)

#returns value for i to be from 2 and 5 (2 to 7 but increment of 3 so 2 and 5 )
for i in range (2,  8, 3):
    print("The value of i is currently", i)

#note for doesn't generate is the set range is empty (1,1) or its intial is greater than its endpoint (2,1)
for i in range(1, 1):
    print("The value of i is currently", i)


for i in range(2, 1):
    print("The value of i is currently", i)

#first 16 values of power of two
power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power = power * 2

#first 16 values of powers of 3
power = 1
for expo in range(16):
    print("3 to the power of", expo, "is", power)
    power *= 3

#counting mississiply (used for counting in seconds)
import time

# Write a for loop that counts to five.
for i in range(1,6):
    # Body of the loop - print the loop iteration number and the word "Mississippi".
    print(i, "Mississippi")
    # Body of the loop - use: time.sleep(1)
    use: time.sleep(1)

# Write a print function with the final message.
print("Ready or not here I come")
