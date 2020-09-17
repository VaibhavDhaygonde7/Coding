f = open("vaibhav2.txt", "w")
f.write("Vaibhav wants to code")    #this will replace all the text written in the file with the text written in the write()
f.close()

f2 = open("vaibhav.txt", "a")

a = f2.write("\nThis line will be added to the file")
print(a)        #this is the number of characters written to a file

f2.close()

f3 = open("vaibhav3.txt", "r+")      #r+ will read and write into a file
print(f3.read())            #this will type all the content written in the file
f3.write("\nThis is the second line")
f3.close()