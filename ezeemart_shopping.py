
# Custmer Registration and Mangement

class Customer:
  _customers = {}
# This is a counter to keep count of the client ID and avoid errors
  _next_customer_id = 1

  def __init__(self, customer_id, name):
    self._customer_id = customer_id
    self._name = name
# This methof return the customer ID
  def get_customer_id(self):
    return self._customer_id
  # This method returns the name of the customer
  def get_customer_name(self):
    return self._name
  # This method returns the detail or the customer
  def display_customer_detail(self):
    print(f"Customer Detail\nCustomer ID: {self._customer_id}\nCustomer Name: {self._name}")

#  This uses a class method which allow to modify class level variable and create an instance with throwing an error
  @classmethod
  def register_customer(cls, name):
    customer_id = cls._next_customer_id
    customer = cls(customer_id, name)
    cls._customers[customer_id] = name
    cls._next_customer_id += 1 
    return customer



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