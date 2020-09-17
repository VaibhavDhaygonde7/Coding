f = open("vaibhav.txt")

try:
    f2 = open("doesnotexist.txt")

except EOFError as e:
    print("EOF error aa gaya hai", e)

except IOError as e:
    print("IO error aa gaya hai ", e)

else:
    print("This will run if the except will not run....")    #this will be printed if the code in except is not executed

finally:
    print("Run this statement anyway....")
    f.close()

print("Important statement")