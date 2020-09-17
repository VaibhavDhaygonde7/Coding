items = [int, float, "Vaibhav", 1, 2, 7, 1023]

for item in items:
    if str(item).isnumeric() and item < 10:
        print(item)