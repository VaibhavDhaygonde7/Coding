import random

print("Printing random number using random.random()")
print(random.random())  
#this will generate any random number between 0 to 1

# print("Enter number 1: ")
# num1 = int(input())
# print("Enter number 2: ")
# num2 = int(input())
print("The random number between the two entered number is", random.randint(0, 10))
#random.randint() will produce random numbers between the two passed numbers in the function

print("The random number between 5 to 10 is", random.randrange(5,10))

city = ["Mumbai", "Delhi", "Banglore", "Pune", "Indore", "Srinagar", "Hyderabad"]

print("The name of the random city is", random.choice(city))
#random.choice() will choice any random element passed to it 

print("The name of the 2 random cities is", random.sample(city, 2))
#random.sample() will choose any 2 random elements passed to it

random.shuffle(city)      #this function will shuffle the elements in the city list
print("The shuffled form names of cities is", city)
