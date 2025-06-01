
# Custmer Registration and Mangement

class Customer:
# This is a counter to keep count of the client ID and avoid errors
  _next_customer_id = 1

  def __init__(self, customer_id, name):
    self._customer_id = customer_id
    self._name = name
    self.cart = []

  # This method returns the detail or the customer
  def display_customer_detail(self):
    print(f"Customer Detail\nCustomer ID: {self._customer_id}\nCustomer Name: {self._name}")
    

#  This uses a class method which allow to modify class level variable and create an instance with throwing an error
  @classmethod
  def register_customer(cls, name):
    customer_id = cls._next_customer_id
    customer = cls(customer_id, name)
    cls._next_customer_id += 1 
    return customer

# amaan = Customer.register_customer('amaan')
# print(amaan._customer_id, amaan._name)
# output 1 amaan

# Product Management
# encapsulate
# method for displaying products
class Product:

  def __init__(self, name, price, availability: bool = True):
    self._name = name
    self._price = price
    if availability == True:
      self._availability = 'In Stock'
    else:
      self._availability = 'Out of Stock'

  def display_product(self):
    print(f"Product Detail\nName: {self._name}\nPrice: ${self._price} \nAvailability: {self._availability}")
  
# sauce = Product('Sauce', '100', True)
# sauce.display_product()

# Mayo = Product('Sauce', '100', False)
# Mayo.display_product()


# EzeeMart System
# EzeeMart Class, maintain list of product and customers
# Methods = Add new product, Display product availabilyt = True

class EzeeMartSystem:
  
  def __init__(self): 
    self.customers ={}
    self.products = {}

  def add_new_product(self, name, price, availability):
    product = Product(name, price, availability)
    self.products[product._name] = product

  def display_available_products(self):
    for product in self.products.values():
      if product._availability == 'In Stock':
        print(f"{product._name} ${product._price}")
      else:
        pass
  
  def register_customer(self, name):
    customer = Customer.register_customer(name)
    self.customers[customer._customer_id] = customer
    print(f"New Customer Added\nCustomer ID: {customer._customer_id} \nName: {customer._name}")

  def display_all_customers(self):
    for customer in self.customers.values():
      print(f"ID:{customer._customer_id} Name: {customer._name}")
    
  
  def add_to_cart(self, customer_id, product_name):
    customer = self.customers[customer_id]
    product = self.products[product_name]
    customer.cart.append(product)

  def remove_from_cart(self, customer_id, product_name):
    customer = self.customers[customer_id]
    for product in customer.cart:
      if product._name == product_name:
        customer.cart.remove(product)
        return
    print("Item not found in cart")


  def view_cart(self, customer_id):
    customer = self.customers[customer_id]
    print(f"{customer._name}'s cart")
    for product in customer.cart:
      print(product._name)
    


# store = EzeeMartSystem()
# store.register_customer('Amaan')
# store.register_customer('umar')
# store.register_customer('shafi')

# store.display_all_customers()

# store.add_new_product('sauce', 15, True)
# store.add_new_product('Mayo', 15, True)
# store.add_new_product('Ranch', 15, False)
# store.add_new_product('Indome', 15, True)
# store.add_new_product('Chicke', 15, True)

# store.display_available_products()

# store.add_to_cart(1,'sauce')
# store.add_to_cart(2,'sauce')
# store.add_to_cart(3,'sauce')
# store.add_to_cart(1,'Mayo')
# store.add_to_cart(1,'Indome')

# store.view_cart(1)
# store.remove_from_cart(1, 'ketchup')
# store.view_cart(1)

print("Welcome tO EzeeMart System")
print("________________________")
program = True
print("How to use the System:\n1: To Register New Customer \n2: Display Customer Detail \n3: Add New Product \n4: Display product detail \n5: Add product to Customer's Cart \n6: Remove product from Customer's cart \n7: View Customer's Cart \n8: Exit Program")
store = EzeeMartSystem()

while program:
    try:
        user_input = int(input("Select a number to proceed: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 8.")
        continue

    if user_input == 1:
        name = input("Enter Customer Name: ").strip()
        if name:
            print("!------------------------!")
            store.register_customer(name)
            print("!------------------------!")
        else:
            print("Name cannot be empty!")

    elif user_input == 2:
        print("!------------------------!\nCustomer Details")
        store.display_all_customers()
        print("!------------------------!")

    elif user_input == 3:
        print("!------------------------!\nAdd new product")
        name = input("Enter Product Name: ").strip()
        try:
            price = float(input("Enter Product Price: "))
            availability = input("Enter availability ('y' if product available, 'n' if unavailable): ").lower()
            if availability == 'y':
                valid_availability = True
            elif availability == 'n':
                valid_availability = False
            else:
                raise ValueError("Invalid availability input.")
            store.add_new_product(name, price, valid_availability)
            print("!------------------------!")
        except ValueError as e:
            print(f"Invalid input: {e}")
        print("!------------------------!")

    elif user_input == 4:
        print("!------------------------!\nAll Available Products")
        store.display_available_products()
        print("!------------------------!")

    elif user_input == 5:
        print("!------------------------!\nAdd Product to Customer's cart")
        try:
            customer_id = int(input("Enter Customer ID: "))
            product = input("Enter Product Name: ").strip()
            store.add_to_cart(customer_id=customer_id, product_name=product)
        except (ValueError, KeyError):
            print("Invalid Customer ID or Product Name.")
        print("!------------------------!")

    elif user_input == 6:
        print("!------------------------!\nRemove product from Customer's cart")
        try:
            customer_id = int(input("Enter Customer ID: "))
            product = input("Enter Product Name: ").strip()
            store.remove_from_cart(customer_id=customer_id, product_name=product)
        except (ValueError, KeyError):
            print("Invalid Customer ID or Product Name.")
        print("!------------------------!")

    elif user_input == 7:
        print("!------------------------!\nView Customer's Cart")
        try:
            customer_id = int(input("Enter Customer ID: "))
            store.view_cart(customer_id=customer_id)
        except (ValueError, KeyError):
            print("Invalid Customer ID.")
        print("!------------------------!")

    elif user_input == 8:
        print("Exiting EzeeMart System. Goodbye!")
        program = False

    else:
        print("Please select a valid option from 1 to 8.")
