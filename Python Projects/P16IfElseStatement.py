print("Enter your age: ")
age = int(input())

if age > 18:
    print("You can drive")
elif age == 18:
    print("If you have license then you can drive")
else:
    print("You can not drive")