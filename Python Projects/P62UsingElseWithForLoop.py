khana = ["roti", "sabzi", "chawal"]

# remember that the else statement will be printed if the for loop ends normally and not with a break statement 
for item in khana:
    if "chawal" == item:
        break
    else:
        print(item)

else:
    print("For loop ended properly")   #this will not be printed because the for loop ended with a break statement

khana2 = ["roti", "sabzi", "chawal"]

for item in khana2:
    print(item)
else:
    print("For loop ended properly")  #this print statement will be printed

