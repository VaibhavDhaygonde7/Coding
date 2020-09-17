import os  
# os - operating system
# print(dir(os))    #this will print the functions in the os module
# print(os.getcwd())    #getcwd() means current working directory
# # if we want to read or write a file then python will find the file in the cwd which is current working directory

# # function to change the current working directory
# # os.chdir("")  write the file path in the ""
# print(os.listdir())   #this will print all the files in the cwd
# print("\n\n\n")
# print(os.listdir("C://"))   #this will print all the files in the C:\
# os.listdir() will return a list

# function to make a new folder 
# os.mkdir("NewFolder")
# os.makedirs("NewFolder2/NewFile")    #this will make a new folder and store a folder named NewFile in it

# function to rename a file 
# os.rename("vaibhav2.txt", "vaibhavtwo.txt")

# function to get the environment variables
# print(os.environ.get('Path'))

# function to get the address of the files
# print(os.path.join("C:/", "vaibhav.txt"))    #this will remove all the slash of the names and we get our desired file easily

# function to know if a path exists or not
# print(os.path.exists("C://"))  #this will return true is the path exists otherwise false

# function isdir()
# print(os.path.isdir("C://Program Files"))    #this will return true if the directory exists otherwise flase

# # function isfile()
# print(os.path.isfile("C://Program Files"))    #this will return true if the file exists otherwise flase