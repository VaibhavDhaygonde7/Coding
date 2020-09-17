f = open("vaibhav.txt", "r")    #f is the file pointer

# content = f.read(3)  #this will read the content of the file 
# print(content)

# content = f.read(3)  #this will read 3 characters from the file
# print(content)

#   -------------------------- READING LINES FROM A FILE ---------------------------------------- #
# for line in f:
#     print(line, end="")


# ------------------------------------READLINE()------------------------------------------------ #
# print(f.readline())   #this will read one line from the file
# print(f.readline())

# -------------------------------------------READLINES()------------------------------------------#
print(f.readlines())    #this will read lines from the file and it will store the line in a list
f.close()   #remember to close the file because it is a good practice