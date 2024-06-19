#program 1
a = 5
b = 3.5
name = "Abdul Basit"
print("Value of 'a':", a)
print("Value of 'b':", b)
print("Name:", name)
sum_ab = a + b
difference_ab = a - b
product_ab = a * b
division_ab = a / b

print("Sum of 'a' and 'b':", sum_ab)
print("Difference of 'a' and 'b':", difference_ab)
print("Product of 'a' and 'b':", product_ab)
print("Division of 'a' by 'b':", division_ab)

#Program 2

temp_celsius = 25.0
temp_fahrenheit = 77.0
converted_to_fahrenheit = (temp_celsius * 9/5) + 32
converted_to_celsius = (temp_fahrenheit - 32) * 5/9
print("The temperature {} degrees Celsius is equal to {} degrees Fahrenheit.".format(temp_celsius, converted_to_fahrenheit))
print("The temperature {} degrees Fahrenheit is equal to {:.2f} degrees Celsius.".format(temp_fahrenheit, converted_to_celsius))
