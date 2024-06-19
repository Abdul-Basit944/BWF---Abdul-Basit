#program 1 using advance dictnories
customers_list = [
    {"id": 0, "name": "John", "age": 30},
    {"id": 1, "name": "Jane", "age": 25}
]

customers_dict = {customer["id"]: customer for customer in customers_list}

print("Accessing information from dictionary of dictionaries:")
print(customers_dict[0]["name"])  
print(customers_dict[1]["age"])  
print()

customer = {
    "name": "John Doe",
    "orders": ["Order1", "Order2", "Order3"]
}

print("Orders for", customer["name"])
for order in customer["orders"]:
    print(order)
print()

customer_details = {
    "details": {"name": "David", "age": 35, "city": "New York"}
}

print("Customer Details:")
print("Name:", customer_details["details"]["name"])
print("Age:", customer_details["details"]["age"])
print("City:", customer_details["details"].get("city", "Unknown"))

#program 2 using Function complete

def greet(name):
    print(f"Hello, {name}!")

def calculate_total(price, quantity):
    total = price * quantity
    return total

def greet_with_default(name="Guest"):
    print(f"Hello, {name}!")

def describe_pet(animal_type, pet_name, **kwargs):
    description = f"My {animal_type.lower()} is named {pet_name}."
    if 'age' in kwargs:
        description += f" It is {kwargs['age']} years old."
    if 'color' in kwargs:
        description += f" It has {kwargs['color']} fur."
    print(description)

def print_arguments(*args):
    for arg in args:
        print(arg)

def add_and_multiply(num1, num2):
    sum_result = num1 + num2
    product_result = num1 * num2
    return sum_result, product_result

def outer_function(x):
    def inner_function(y):
        return y * 2
    return inner_function(x)

if __name__ == "__main__":
    greet("Alice")

    total_price = calculate_total(price=10, quantity=3)
    print(f"Total price: ${total_price}")

    greet_with_default()  
    greet_with_default("Bob")  

    describe_pet("Dog", "Buddy", age=3, color="brown")

    print_arguments("Hello", "world", 2023, [1, 2, 3])

    result_sum, result_product = add_and_multiply(5, 3)
    print(f"Sum: {result_sum}, Product: {result_product}")

    inner_result = outer_function(10)
    print(f"Inner result: {inner_result}")
