a = input("Enter your name: ")
b = input("How much do earn: ")

if int(b) == 0:
    raise ZeroDivisionError("Cannot calculate because the input is zero")

if a.isnumeric():
    raise Exception("Numbers are not allowed as names")

print(f"Hello {a}")


c = input("Enter your name: ")

# try:
#     print(variable_not_exist)

# except Exception as e:
#     if c == "Harry":
#         raise ValueError("Harry is not allowed")
#     print("variable not found")