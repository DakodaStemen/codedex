class Restaurant:
    name = ""
    style = ""
    rating = 0.0
    has_chicken = False

bobs_burger = Restaurant()
bobs_burger.name = "Bob's Burger"
bobs_burger.style = "American Diner"
bobs_burger.rating = 4.7
bobs_burger.has_chicken = False

sweetgreen = Restaurant()
sweetgreen.name = "Sweetgreen"
sweetgreen.style = "Salad Spot"
sweetgreen.rating = 5.0
sweetgreen.has_chicken = True

in_n_out = Restaurant()
in_n_out.name = "In N' Out"
in_n_out.style = "American Diner"
in_n_out.rating = 4.75
in_n_out.has_chicken = False

print(vars(bobs_burger))
print(vars(sweetgreen))
print(vars(in_n_out))