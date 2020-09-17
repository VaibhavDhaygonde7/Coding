import time

initial = time.time()

k = 0
while (k < 10):
    print("Vaibhav is Coding")
    k += 1
print(f"While loop ran in {initial - time.time()} seconds")

initial2 = time.time()
for i in range(10):
    print("Vaibhav is Coding")


print(f"For loop ran in {initial2 - time.time()} seconds")

#printing local time
localtime = time.asctime(time.localtime(time.time()))
print(localtime)

#time.sleep()

for i in range(5):
    print("Vaibhav is Coding")
    time.sleep(1)    #this will wait for 1 second every time after print the statement