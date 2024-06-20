#program 1 using classes complete

class BankAccount:
    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance:.2f}")

    def update_account_holder(self, new_name):
        self.account_holder = new_name
        print(f"Account holder's name updated to {self.account_holder}")

account1 = BankAccount("Alice")
account1.display_account_info()

account1.deposit(100.50)
account1.withdraw(25.25)
account1.withdraw(200)  

account1.display_account_info()
account1.update_account_holder("Alice Smith")
account1.display_account_info()

#program 2 using  Data Files Complete

file_name = "data.txt"

def store_data(data):
    with open(file_name, "w") as file:
        file.write(data)
    print("Data stored successfully.")

def retrieve_data():
    try:
        with open(file_name, "r") as file:
            data = file.read()
        print("Data retrieved from file:")
        print(data)
    except FileNotFoundError:
        print("File not found. Please store data first.")

def append_data(new_data):
    with open(file_name, "a") as file:
        file.write(new_data)
    print("Data appended successfully.")

initial_data = "This is the initial data.\n"

store_data(initial_data)

retrieve_data()

new_data_to_append = "This is additional data.\n"

append_data(new_data_to_append)

retrieve_data()

#program using CSV files both CSV and JSON Operations


import csv
import json

csv_file_name = "simple_data.csv"

data = [
    ["name", "age", "city"],
    ["Alice", 30, "New York"],
    ["Bob", 25, "San Francisco"],
    ["Charlie", 35, "Los Angeles"]
]

def write_csv(data):
    with open(csv_file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("Data written to CSV file successfully.")

def read_csv():
    try:
        with open(csv_file_name, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("CSV file not found. Please write data first.")

def append_csv(new_data):
    with open(csv_file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(new_data)
    print("Data appended to CSV file successfully.")

write_csv(data)

read_csv()

new_data = [
    ["David", 40, "Chicago"],
    ["Eve", 22, "Boston"]
]

append_csv(new_data)

read_csv()

#JSON Operation

json_file_name = "simple_data.json"

sample_list = ["apple", "banana", "cherry"]

def save_to_json(data):
    with open(json_file_name, mode='w') as file:
        json.dump(data, file)
    print("List saved to JSON file successfully.")

def load_from_json():
    try:
        with open(json_file_name, mode='r') as file:
            data = json.load(file)
        print("List loaded from JSON file successfully.")
        return data
    except FileNotFoundError:
        print("JSON file not found. Please save data first.")

save_to_json(sample_list)

loaded_list = load_from_json()
print(loaded_list)
