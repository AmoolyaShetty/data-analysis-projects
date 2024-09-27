my_string = "LaunchCode"


# a) Use string methods to remove the first three characters from the string and add them to the end.

new_string= my_string[3:] + my_string[:3]
print(new_string)


# Use a template literal to print the original and modified string in a descriptive phrase.
new_string = my_string[3:] + my_string[:3]
print(f"the original string was '{my_string}', and after modification, it is '{new_string}'.")


# b) Modify your code to accept user input. Query the user to enter the number of letters that will be relocated.
my_string = input("Enter a string: ")
num_letters = int(input("Enter the number of letters to relocate: "))
new_string = my_string[num_letters:] + my_string[:num_letters]
print(f"original string: '{my_string}'. new string: '{new_string}'.")


# c) Add validation to your code to deal with user inputs that are longer than the word. In such cases, default to moving 3 characters. Also, the template literal should note the error.
my_string = input("Enter a string")
num_letters = int(input("Enter the number of letters to relocate: "))
if num_letters > len(my_string):
    print(f"Error: The number you entered is larger than the length of the string. Defaulting to 3 characters.")
    new_string = my_string[num_letters:] + my_string[:num_letters]     
print(f"original string: '{my_string}'. new string: '{new_string}'.")   