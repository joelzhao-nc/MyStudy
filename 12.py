import dog
import electric_car as ea

my_dog=dog.dog('willie',6)

print("My dog's name is "+ my_dog.name.title()+".")
print("My dog is "+ str(my_dog.age)+ " years old.")


my_tesla=ea.ElectricCar('tesla','model s','2016')
print(my_tesla.get_descriptive_name())