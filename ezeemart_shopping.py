customers = {}

# Custmer Registration and Mangement

class Customer:
# This is a counter to keep count of the client ID and avoid errors
  next_customer_id = 1

  def __init__(self, customer_id, name):
    self.customer_id = customer_id
    self.name = name
# This methof return the customer ID
  def get_customer_id(self):
    return self.customer_id
  # This method returns the name of the customer
  def get_customer_name(self):
    return self.name
  # This method returns the detail or the customer
  def display_customer_detail(self):
    print(f"Customer Detail\nCustomer ID: {self.customer_id}\nCustomer Name: {self.name}")

#  This uses a class method which allow to modify class level variable and create an instance with throwing an error
  @classmethod
  def register_customer(cls, name):
    customer_id = cls.next_customer_id
    customer = cls(customer_id, name)
    customers[customer_id] = name
    cls.next_customer_id += 1 
    return customer



