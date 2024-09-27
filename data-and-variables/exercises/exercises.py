# 1. Declare and assign the variables here:
shuttle_name ='Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 384400
MILES_PER_KM = 0.621


# 2. Use print() to print the 'type' each variable. Print one item per line.
print(type('Determination'))
print(type(17500))
print(type(225000000))
print(type(384400))
print(type(0.621))
      

# Code your solution to exercises 3 and 4 here:
# 3 create and assign miles to mars variable
miles_to_mars = distance_to_mars_km * MILES_PER_KM
hours_to_mars = miles_to_mars / shuttle_speed_mph
days_to_mars = hours_to_mars / 24

# 4 results of calculation
print(shuttle_name + " will take " + str(days_to_mars) + "to reach the Moon.")

# Code your solution to exercise 5 here
miles_to_moon = distance_to_moon_km * MILES_PER_KM
hours_to_moon = miles_to_moon / shuttle_speed_mph
days_to_moon = hours_to_moon / 24
print(shuttle_name + " will take " + str(days_to_moon) + " days to reach the Moon.")
