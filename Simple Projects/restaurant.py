class Restaurant():
    def __init__(self, restaurant_name, cusisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cusisine_type

    def describe_restaurant(self):
        print (self.restaurant_name.title() + " cuisine is very tasty and the type of meal is " + self.cuisine_type)

    def open_restaurant(self):
        print (self.restaurant_name.title() + " is open from 9 a.m. to 10 p.m.")

my_restaurant = Restaurant("Ciao" , "Italian")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()
