import random

# returns a random floating number between 0.000 and 1.000
# random.random() 

# returns a random floating number between 0.000 and 50.000
# random.random() * 50 

# returns a random floating number between 10.000 and 35.000
# random.random() * 25 + 10 

# returns the rounded integer value of num
# round(num) 

# PLAN OUR ATTACK
# Declare a function named rand_int that has a default min value of 0 and a default max of 100
# Create a random floating point number between 0 and 1 using random.random and store it in a variable called num.
# 

def randInt(min= 0, max= 100):
    num = random.random() * (max - min) + min
    return int(num)



# print(randInt())
# print(randInt(max=50))
# print(randInt(min=50))
print(randInt(min=50, max=500))
