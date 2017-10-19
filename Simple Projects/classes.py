class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is sitting now.")

    def roll_over(self):
        print(self.name.title() + "is on the back.")

my_dog = Dog('Reks', 2)

print("My dog's name is " + my_dog.name.title() + '.')
print("My dog's age is " + str(my_dog.age) + ".")
