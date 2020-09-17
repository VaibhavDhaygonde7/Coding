f = open("vaibhav.txt")
# print(f.tell())       #this will tell the number of character read
print(f.readline())
# print(f.tell())
f.seek(0)     #this will again read the file from the 0th character
print(f.readline())
# print(f.tell())

f.close()