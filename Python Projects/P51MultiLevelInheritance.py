class Dad:
    basketball = 1
    
class Son(Dad):
    dance = 1
    basketball = 3
    def isdance(self):
        return f"I can dance {self.dance} times"

class Grandson(Son):
    dance = 5
    def isdance(self):
        return f"Yeah! I can dance {self.dance} times"

darry = Dad()
larry = Son()
harry = Grandson()

print(harry.isdance())
print(harry.basketball)   #this will print 3 because it will get the basketball variable in class Son 