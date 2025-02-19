class Customer:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address
    def __str__(self):
        return self.name + " " + str(self.age) + " " + self.address

# Generate a Python function that takes in a list of Customer objects and returns a list of Customer objects whose age is greater than 18.
def filter_customers(customers):
    filtered = []
    for customer in customers:
        if customer.age > 18:
            filtered.append(customer)
    return filtered

customers = [Customer("John", 17, "123 Main St"), Customer("Jane", 21, "456 Main St"), Customer("Joe", 15, "789 Main St")]

for customer in filter_customers(customers):
    print(str(customer))

