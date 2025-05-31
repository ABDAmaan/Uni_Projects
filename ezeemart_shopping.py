
# Custmer Registration and Mangement

class Customer:
# This is a counter to keep count of the client ID and avoid errors
  _next_customer_id = 1

  def __init__(self, customer_id, name):
    self._customer_id = customer_id
    self._name = name
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

  def display_all_customers(self):
    for customer in self.customers.values():
      print(f"ID:{customer._customer_id} Name: {customer._name}")
    
    

    