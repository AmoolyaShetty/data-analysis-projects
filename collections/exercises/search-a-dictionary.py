choice = 'vanilla'
if choice in 'flavors':
  cost = 'flavors[choice]'
else:
  cost = 0
print('The cost of', choice, 'is', cost)


# Write your fanciest_flavor function here:
def fanciest_flavor(flavors):
  highest_cost = 0
  fanciest = ''
  for flavor in flavors:
    if flavors[flavor] > highest_cost:
      fanciest = flavor
      highest_cost = flavors[flavor]
  print('The fanciest flavor is', fanciest, 'and it costs', highest_cost)
  pass


# Write your return_cost function here:
def return_cost(menu, item):
  found = item in menu
  if found:
    return menu[item]
  else: 
    return 0
  pass
  




def main():
  flavors = {
    'chocolate' : 0.35,
    'vanilla' : 0.35,
    'strawberry' : 0.42,
    'cookies and cream' : 0.45,
    'mint chocolate chip' : 0.42,
    'fudge chunk' : 0.45,
    'saffron' : 2.25,
    'garlic' : 0.05
  }

  choice = 'vanilla'
  price = return_cost(flavors, choice)
  if price == 0:
    print("Sorry, we don't have {0}.".format(choice))
  else:
    print(f"The price for {choice} is ${price} per scoop.")

# Uncomment the lines below after you code your fanciest_flavor function.
print('---')
expensive_flavor = fanciest_flavor('flavors')
print(f"The most expensive flavor we have is {expensive_flavor}.")


