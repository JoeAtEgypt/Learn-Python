# In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.

# There are two types of type conversion in Python.
## Implicit Conversion - automatic type conversion
## Explicit Conversion - manual type conversion

# Python promotes the conversion of the lower data type (integer) to the higher data type (float) to avoid data loss.
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:", new_number)  # => Value: 124.23
print("Data Type:", type(new_number))  # => Data Type: <class 'float'>


# We get TypeError, if we try to add str and int. For example, '12' + 23.
# Python is not able to use Implicit Conversion in such conditions.
# Python has a solution for these types of situations which is known as Explicit Conversion.
num_string = "12"
num_integer = 23

print(
    "Data type of num_string before Type Casting:", type(num_string)
)  # => <class 'str'>

# explicit type conversion
num_string = int(num_string)

print(
    "Data type of num_string after Type Casting:", type(num_string)
)  # => <class 'int'>

num_sum = num_integer + num_string

print("Sum:", num_sum)  # => Sum: 35
print("Data type of num_sum:", type(num_sum))  # => <class 'int'>
