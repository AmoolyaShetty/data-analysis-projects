# We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
# e) Create a variable of type string to test your new function. # f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.



# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.



list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']




# 1) We want to COMPLETELY reverse a list by flipping the order of the entries AND flipping the order of characters in each element.

# a) Define a 'reverse_characters' function. Give it one parameter, which will be the string to reverse.
# b) Within the function, use the 'list' function to split a string into a list of individual characters
# c) 'reverse' your new list.
# d) Use 'join' to create the reversed string and return that string from the function.
# e) Create a variable of type string to test your new function. 
# f) Use 'print(reverse_characters(my_variable_name))'; to call the function and verify that it correctly reverses the characters in the string.
# g) Use method chaining to reduce the lines of code within the function.


list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

def reverse_characters(string_to_reverse):    #a
   return ''.join(list(str(string_to_reverse))[::-1])  #g

test_string ="Home Sweet Home!"           #e
print(reverse_characters(test_string))     #f

def completly_reverse_list(input_list):    #1
   return[reverse_characters(element) for element in input_list[::-1]]

#define the list

list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

# reverse the list
reversed_list_test1 = completly_reverse_list(list_test1)
reversed_list_test2 = completly_reverse_list(list_test2)
reversed_list_test3 = completly_reverse_list(list_test3)

#print the results
print("Reversed list_test1:", reversed_list_test1)
print("Reversed list_test2:", reversed_list_test2)
print("Reversed list_test3:", reversed_list_test3)


def reverse_characters(string_input):
    string_list = list(string_input)
    string_list.reverse()
    reversed_string = "".join(string_list)
    return reversed_string




# 2) The 'split' method does not work on numbers, but we want the function to return a number with all the digits reversed (e.g. 1234 converts to 4321 and NOT the string "4321")
# a) Add an if statement to your reverse_characters function to check the typeof the parameter.
# b - d) If type is ‘string’, return the reversed string as before. If type is ‘number’, convert the parameter to a string, reverse the characters, then convert it back into a number. Return the reversed number.
# e) Be sure to print the result returned by the function to verify that your code works for both strings and numbers. Do this before moving on to the next steps.


def reverse_characters(input_list):
    if isinstance(input_list,str):  #a
      return ''.join(list(input_list)[::-1])  #b
    elif isinstance(input_list,(int, float)): 
        reversed_str = ''.join(list(str(input_list))[::-1])  #c
        if isinstance(input_list,int):  #d
            return int(reversed_str)
        else:
            return float(reversed_str)
    else:
        return f"unsupported type:{type(input_list)}"
    
test_string = "radar"
test_int = 1234
test_float = 3.14

print("Reversed string:", reverse_characters(test_string))
print("Reversed integer:", reverse_characters(test_int))
print("Reversed float:", reverse_characters(test_float))

def completly_reverse_list(input_list):
    return [reverse_characters (element) for element in input_list[::-1]]

# define list
list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

# reverse the list
reversed_list_test1 = completly_reverse_list(list_test1)
reversed_list_test2 = completly_reverse_list(list_test2)
reversed_list_test3 = completly_reverse_list(list_test3)

# print the results
print("Reversed list_test1:", reversed_list_test1)
print("Reversed list_test2:", reversed_list_test2)
print("Reversed list_test3:", reversed_list_test3)

# 3) Create a new function with one parameter, which is the list we want to change. The function should:
# a) Define and initialize an empty list.
# b) Loop through the old list.
# c) For each element in the old list, call reverse_characters to flip the characters or digits.
# d) Add the reversed string (or number) to the list defined in part ‘a’.
# e) Return the final, reversed list.
# f) Be sure to print the results from each test case in order to verify your code.


def reverse_list(old_list):   #   
    new_list =[]   #a
    for element in old_list:
        reversed_element = reverse_characters(element)
        new_list.append(reversed_element)
    return new_list[::-1]

# define list
list_test1 = ['apple', 'potato', 'Capitalized Words']
list_test2 = [123, 8897, 42, 1168, 8675309]
list_test3 = ['hello', 'world', 123, 'orange']

print("Original list_test1:",list_test1)
print("Original list_test2:",list_test2) 
print("Original list_test3:",list_test3)

