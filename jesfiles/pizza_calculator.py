number_of_people = 150
slices_per_pizza = 8
slices_per_person = 3

number_of_pizzas = number_of_people * slices_per_person / slices_per_pizza
# Use the str() function to convert a number into a string.
print("We will need around " + str(number_of_pizzas) + " pizzas for " + str(number_of_people) + " people.")

# Use the int() function to convert a float to an integer.
cheese = int(.25 * number_of_pizzas)
vegetarian = int(.25 * number_of_pizzas)
meat = int(.5 * number_of_pizzas)
print("Get:")
print(str(cheese) + " cheese pizzas.")
print(str(vegetarian) + " vegetarian pizzas.")
print(str(meat) + " meat-lovers pizzas.")
