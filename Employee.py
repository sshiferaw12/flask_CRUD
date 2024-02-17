class Employee:
    def __init__(self,id,name, age, department, salary = 0, bio = "", location = "Madrid"):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary
        self.bio = bio
        self.location = location
        self.id = id

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "department": self.department,
            "salary": self.salary,
            "bio": self.bio,
            "location": self.location
        }