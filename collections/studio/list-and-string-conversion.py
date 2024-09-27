proto_list1 = "3,6,9,12"
proto_list2 = "A;C;M;E"
proto_list3 = "space delimited string"
proto_list4 = "Comma-spaces, might, require, typing, caution"

strings = [proto_list1, proto_list2, proto_list3, proto_list4]

# a) Use the 'in' method to check to see if the words in each string are separated by commas (,), semicolons (;) or just spaces.

for i in range(len(strings)):
    string = strings[i]
    if ',' in string:
        print(f"proto_list{i+1} uses commas as separators")
    elif ';' in string:
        print(f"proto_list{i+1} uses semicolons as separators")
    elif ' 'in string:
        print(f"proto_list{i+1} uses spaces as separtors")
    else:
        print(f"proto_list{i+1} doesnt use commas, semicolons, or space as separators")




# b) If the string uses commas to separate the words, split it into an array, reverse the entries, and then join the array into a new comma separated string.
for i in range(len(strings)):
    string = strings[i]
    if ',' in string:
        print(f"proto_list{i+1} uses commas as separators")
        array = string.split(',') #split the string into an array
        array.reverse() #reverse the array
        new_string = ','.join(array) #join the array back into a string
        print(f"reversed string: {new_string}")
    


# # c) If the string uses semicolons to separate the words, split it into an array, alphabetize the entries, and then join the array into a new comma separated string.
for i in range(len(strings)):
    string = strings[i]
    if ';' in string:
        print(f"proto_list{i+1} uses semicolons as separators")
        array = string.split(';') #split the string into an array
        array.sort() # alphabetize the array
        new_string = ','.join(array) #join the array back into a string, using commas
        print(f"alphabetized and comma separated string: {new_string}")



# d) If the string uses spaces to separate the words, split it into an array, reverse alphabetize the entries, and then join the array into a new space separated string.
for i in range(len(strings)):
    string = strings[i]
    if ' 'in string:
        print(f"proto_list{i+1} uses spaces as separators")
        array = string.split(' ')
        array.reverse()
        new_string = ' '.join(array)
        print(f"reversed string: {new_string}")
    



# e) If the string uses ‘comma spaces’ to separate the list, modify your code to produce the same result as part “b”, making sure that the extra spaces are NOT part of the final string.
for i in range(len(strings)):
    string = strings[i]
    if ', ' in string:
        print(f"proto_list{i+1} uses comma spaces as separators")
        array = string.split(', ') #split the string into an array
        array.reverse() #reverse the array
        new_string = ', '.join(array) #join the array back into a string
        print(f"reversed string: {new_string}")
        
        