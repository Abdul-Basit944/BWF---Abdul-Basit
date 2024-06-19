#if else statment program


num = float(input("Enter a number: "))

if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

#program 2

score = float(input("Enter your score: "))

if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your Grade is {grade}")

#program 3 using Nested If


num = float(input("Enter a number: "))

if num >= 0:
    if num > 100:
        print("The number is positive and greater than 100.")
    elif num == 0:
        print("The number is zero.")
    else:
        print("The number is positive and less than or equal to 100.")
else:
    print("The number is negative.")

#program 4 using List
numbers = [1, 2, 3, 4, 5]
print("First element:", numbers[0])
print("Last element:", numbers[4])
numbers[2] = 30
print("Modified list:", numbers)
numbers.append(6)
print("List after appending:", numbers)
removed_element = numbers.pop(1)
print("List after removing element at index 1:", numbers)
print("Removed element:", removed_element)

#program 5 using chaning cases

text = "Hello, World!"
uppercase_text = text.upper()
print("Uppercase:", uppercase_text)
lowercase_text = text.lower()
print("Lowercase:", lowercase_text)
capitalized_text = text.capitalize()
print("Capitalized:", capitalized_text)



