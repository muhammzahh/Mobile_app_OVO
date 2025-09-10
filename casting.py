# Koding Casting data types

# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0

num_bool = bool(num_int)
print(num_bool, type(num_bool))



# Koding comparison operators
# Equal to
8 == 8
# Not equal to
8 != 9
# Greater than
8 > 9
# Less than
8 < 9
# Less than
8 <= 9
# Less than
9 >= 9


# Koding logical operators
a = True
b = True
print(a and b)
print(a or b)
print(not b)
#logic
5 > 6 and 6 < 7


#Koding arithmetic operators
e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}\n")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}\n")

# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}\n")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}\n")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}\n")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}\n")

#Koding input output
#input
name = str(input("Muhammad Burhannudin Hamzah: "))
age = int(input("18:"))
print("Name :", name)
print("Age :",18)

#output
#normal print
print('Hi all! I am', name, 'age', age, 'years old')
# format print
print(f'Hi all! I am {name} age {age} years old')
# normal print
print('Hi all! I am', name, 'age', age, 'years old')
# format print
print(f'Hi all! I am {name} age {age} years old')
# format print
print(f'Hi all! I am %s age %d years old'%(name, age))
# fortmat output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")