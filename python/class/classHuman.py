
class Human:
    """This is sample class"""
    
    def __init__(self,fname,lname,age,nationality="IRAN"):
        self.fname = fname
        self.lname = lname
        self.nationality = nationality

    def greeting(self,message = "Hi") -> str:
        return f"{message} {self.fname} {self.lname}"

    def update_name(self,name: str) -> None:
        self.fname = name

personA = Human("Mohammad","Taheri",24)
print(personA.greeting())
print(personA.fname)
personA.fname = "Gholam"  # We can change attribute of class directly
print(personA.fname)
personA.update_name("Farhad") # Or We can change name with a method
print(personA.fname)