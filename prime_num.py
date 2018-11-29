"""
find whether a given number is PRIME
using a for loop
"""

num = int(input("enter your number :"))

for divisor in range(2, num):
    if num % divisor == 0:
        print(divisor)
        print("the number is not prime, its has a divisor",divisor)
        exit()
print("the number is Prime")

exit()