import restaurant
import user

ralphs = restaurant.IceCreamStand("Ralphs", "Ice Cream")

ralphs.describe_restaurant()
print()
ralphs.list_flavors()
print()

frigate = restaurant.IceCreamStand("The Frigate", "Ice Cream", ['Cookie Dough'])
frigate.describe_restaurant()
print()
frigate.list_flavors()

print("\n\n")

steve = user.Admin('steve', 'smith', 37, 'male', 'new york')
steve.describe_user()
print()
steve.privileges.show_privileges()
