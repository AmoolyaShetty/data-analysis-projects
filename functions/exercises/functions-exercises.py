# Part 1 A -- Make a Line
# print (make_line(5))
def make_line(size):
    line = ""
    for i in range(size):
        line += '#'
    return line 

print(make_line(5))


# Part 1 B -- Make a Square
# create a function using your make_line function to code a square
#print(make_line(5))
def make_line(size):
    return "#" * size

def make_square(size):
    square = ""
    for i in range(size):
        square += (make_line(size) + "\n")
    return square[:-1]

print(make_square(5))




# Part 1 C -- Make a Rectangle(width, height)
# print(make_rectangle(5,3))
def make_line(size):
    return '#' * size

def make_rectangle(width, height):
    rectangle = ""
    for i in range(height):
        rectangle += (make_line(width) + "\n")
    return rectangle

print(make_rectangle(5,3))



# Part 2 A -- Make a Stairs
# use make_line function to do this
# make_downward_stairs(hieght)
# print(make_downward_stairs(5)) 
def make_line(size):
    return "#" * size

def make_downward_stairs(height):
    stairs = ""
    for i in range(height):
        stairs += (make_line(i+1) + "\n")
    return stairs

print(make_downward_stairs(5))
    




# Part 2 B -- Make Space-Line 
# make_space_line(numSpaces, numChars)
# print(make_space_line(3,5))
def make_space_line(numSpaces, numChars):
    return " " * numSpaces + "#" * numChars + " " * numSpaces

print(make_space_line(3,5))
    



# Part 2 C -- Make Isosceles Triangle
# make_isosceles_triangle(height)
# print(make_isosceles_triangle(5))
# Consider the top line of the triangle to be level 0, the next to be line 1, and so on. 
# Then line i is a space-line with height - i - 1 spaces and 2 * i + 1 hashes.

def make_isosceles_triangle(height):
    triangle = ""
    for i in range(height):
        triangle += (make_space_line(height -i -1, 2 * i + 1) + "\n")
    return triangle

print(make_isosceles_triangle(5)) 



# Part 3 -- Make a Diamond
# make-diamond(height)
# print(make_diamond(5))

def make_diamond(height):
    diamond = ""
    triangle = make_isosceles_triangle(height)
    diamond += triangle[:-1]
    for i in range(len(triangle)-1,-1,-1):
        diamond += triangle[i]
    return diamond

print(make_diamond(5))






