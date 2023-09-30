
name ="lama"
age = 20
street = "159"
city = "Gaza"
country = "palestine"
print(f""""Name: {name}"
"Age: {age}"  
"Address: {street} {city}  {country}"
""")
#  another way of writing
print("*"*30)
print(f'"Name: {name}"')
print(f'"Age: {age}"')
print(f'"Address : {street} , {city} , {country} "')
print("*"*30)

age -= 5
print(f'"Hello {name} Your age is {age} years old, Your Address is {street} {city} {country}."')
print("*"*50)
# types_of_variables
print(type(name))
print(type(age))
print(type(street))
print(type(city))
print(type(country))
print("*"*50)

print(f' "Hello {name}, How are you? \ """ Your Age Is "{age}"" + And Your Country Is : {country}')
print("*"*50)

print(f""" "Hello '{name}', How Are You? \ """ )
print(f'"""Your Age Is "{age}"" + And')
print(f"Your city is: {city} ")
print("*"*50)

name = 'ITF Gsg Python'
print(f'First Letter Is "{name[0]}" ')
print(f'Third Letter Is "{name[2]}" ')
print(f'Last Letter Is "{name[-1]}" ')
print("*"*50)

print(name[11:])
print(name[:3])
print(name[0:8:2])
print(name[14:7:-1])
print("*"*50)

name ="$&$&Mohammed$&$&"
print(name.strip("$&$&"))
print("*"*50)

msg = " I %7 python And Although I %7 GSG with Zakaria "
print(msg.replace("%7","Love"))
print("*"*50)

num1 = "4"
num2 = "56"
num3 = "963"
num4 = "385"
num5 = "8719"
num6 = "87190"
print(num1.zfill(5))
print(num2.zfill(5))
print(num3.zfill(5))
print(num4.zfill(5))
print(num5.zfill(5))
print(num6.zfill(5))
print("*"*50)

# the difference between (capitalize) and (title) methods :
# the (capitalise) method will only modify ( make capital) the initial character and let
# other characters in the string without any changes .
# While the (title) method capitalises the first letter of each word in the string .
name1 = "farah bassam alzain"
print(name1.capitalize())
print(name1.title())
name2 = "i love gsg and python"
print(name2.capitalize())
print(name2.title())

print("*"*50)
first_name = "farah"
print("*"*11 +first_name)
print("*"*11 +first_name+ "*"*11)
print(first_name+ "*"*11)
print("*"*50)

name_one = "SaMER"
name_two = "Abed"
print(name_one.swapcase())
print(name_two.swapcase())
print(name_one.lower())
print(name_two.upper())
print("*"*50)

print(name_one.isupper())
print(name_two.islower())
#this related to above varabiles
#if variables are as below
# name_one = "SAMER"
# name_two = "abed"
# print(name_one.isupper())
# print(name_two.islower())
# print("*"*50)

#Bonus ****
print(name_one.find("S"))
print(name_two.find("HD"))
print("*"*50)

msg = " I Love Python And Although I Love GSG with Zakaria "
print("Number of <love>: " +str(msg.count("Love")))
print("Number of <t>: " + str(msg.count("t")))
print("*"*50)

msg = " I %7 python And Although I %7 GSG with Zakaria "
print(msg.replace("%7","Love",1))
print("*"*50)

