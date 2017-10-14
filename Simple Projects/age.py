#porównanie wieku

birthYear = 1992
actualYear = 2017

age = actualYear - birthYear

name = input("What's your name?")
askAge = int(input("How old are you?"))

print("Hello",name)
print("I'm Anna, I'm" ,age, "old")
if age > askAge:
    print("I'm older")
else:
    print("You are older")