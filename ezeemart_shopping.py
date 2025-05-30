customers = {}

class Customer:
  def __init__(self, customer_id, name):
    self.customer_id = customer_id
    self.name = name

  def get_customer_id(self):
    return self.customer_id
  
  def get_customer_name(self):
    return self.name
  
  def display_customer_detail(self):
    print(f"Customer Detail\nCustomer ID: {self.customer_id}\nCustomer Name: {self.name}")

  def register_customer(self, name):
    next_customer_id = 0
    self.name = name
    self.customer_id = next_customer_id
    next_customer_id += 1 



client1 = Customer.register_customer(name='amaan')
client_id = client1.get_customer_id()
client_name = client1.get_customer_name()
client1.display_customer_detail()


