#program 1
num1 = 10.5
num2 = 2.5
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 
print("The sum of {} and {} is: {}".format(num1, num2, addition))
print("The difference when {} is subtracted from {} is: {}".format(num2, num1, subtraction))
print("The product of {} and {} is: {}".format(num1, num2, multiplication))
print("The division of {} by {} is: {}".format(num1, num2, division))

#Program 2

temp_celsius = 25.0
temp_fahrenheit = 77.0
converted_to_fahrenheit = (temp_celsius * 9/5) + 32
converted_to_celsius = (temp_fahrenheit - 32) * 5/9
print("The temperature {} degrees Celsius is equal to {} degrees Fahrenheit.".format(temp_celsius, converted_to_fahrenheit))
print("The temperature {} degrees Fahrenheit is equal to {:.2f} degrees Celsius.".format(temp_fahrenheit, converted_to_celsius))
