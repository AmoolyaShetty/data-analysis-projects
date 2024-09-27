food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_cabinet = food.split(',') # convert the string to list and alphabetize
food_cabinet.sort()
equipment_cabinet = equipment.split(',')
equipment_cabinet.sort()
pets_cabinet = pets.split(',')
pets_cabinet.sort()
sleep_aids_cabinet = sleep_aids.split(',')
sleep_aids_cabinet.sort()
print("Food cabinet:", food_cabinet)
print("Equipment cabinet:", equipment_cabinet)
print("Pets cabinet:", pets_cabinet)
print("sleep aids cabinet:", sleep_aids_cabinet)

# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
cargo_hold = [food_cabinet, equipment_cabinet, pets_cabinet, sleep_aids_cabinet]
print ("Cargo hold contents:")
for i, cabinet in enumerate(cargo_hold, 1):
    print (f"cabinet {i}: {cabinet}")
print ("\nEntire Cargo Hold:")
print(cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
cabinet_index = input("Select a cabinet (0 - 3): ")
if cabinet_index.isdigit():
    cabinet_index= int(cabinet_index)
    if 0 <= cabinet_index < len(cargo_hold):
        selected_cabinet = cargo_hold[cabinet_index]
        print(f"Cabinet {cabinet_index} contents: {selected_cabinet}")
    else:
        print("Invalid choice. Please select a number between 0 and 3.")
else:
    print("Invalid input. Please enter a number.")



# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
cabinet_index = input("Select a cabinet (0 - 3): ")
if cabinet_index.isdigit():
    cabinet_index = int(cabinet_index)
    if 0 <= cabinet_index < len(cargo_hold):
        selected_cabinet = cargo_hold[cabinet_index]
        print(f"Cabinet {cabinet_index} contents: {', '.join(selected_cabinet)}")
    else:
        print("Error: Invalid choice. Please select a number between 0 and 3.")
else:
    print("Error: Invalid input. Please enter a number.")


# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
cabinet_index = input("Select a cabinet (0-3):")
if cabinet_index.isdigit():
    cabinet_index = int(cabinet_index)
    if 0 <= cabinet_index<len(cargo_hold):
        item = input("Enter the item to check:").strip()
        selected_cabinet = cargo_hold[cabinet_index]
        if item is selected_cabinet:
            print(f"Cabinet{cabinet_index}DOES contain'{item}'.")
        else:
            print(f"Cabinet{cabinet_index}DOES NOT contain '{item}'.")
    else:
        print("Error:Invalid cabinet choice. Please select a number between 0 and 3.")
else:
    print("Error:Invalid output.Please enter a number.")


