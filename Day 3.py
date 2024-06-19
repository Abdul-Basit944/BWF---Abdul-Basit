
# Program 1 using for loop

sum_numbers = 0
for num in range(1, 6):  
    sum_numbers = sum_numbers+num
print("The sum of numbers from 1 to 5 is:", sum_numbers)

#program 2 

for num in range(1, 6):  
    square = num ** 2
    print(f"The square of {num} is:", square)

#pogram 3 using Dictionaries

phonebook = {
    "John": "123-4567",
    "Mary": "234-5678",
    "Bob": "345-6789"
}

print("Accessing values:")
print(phonebook["John"]) 
print(phonebook.get("John"))  
print(phonebook.get("Alice", "Not Found"))  
print()

print("Adding a new entry:")
phonebook["Alice"] = "456-7890"
print(phonebook)
print()

print("Updating entries:")
phonebook.update({"John": "111-2222", "Mary": "333-4444"})
print(phonebook)
print()

print("Deleting an entry:")
del phonebook["Bob"]
print(phonebook)
print()

print("Changing an entry:")
phonebook["John"] = "555-6666"
print(phonebook)
print()

print("Getting keys, values, and items:")
print("Keys:", phonebook.keys())      
print("Values:", phonebook.values())  
print("Items:", phonebook.items())    
print()

print("Iterating over values:")
for value in phonebook.values():
    print(value)
print()

print("Iterating over keys:")
for key in phonebook.keys():
    print(key)
print()

print("Iterating over key-value pairs:")
for key, value in phonebook.items():
    print(f"{key}: {value}")

