class Product:
    def __init__(self, id, name, size, price, quantity):
        self.id = id
        self.name = name
        self.size = size
        self.price = price
        self.quantity = quantity

    def id(self):
        return self.id

    def name(self):
        return self.name

    def size(self):
        return self.size

    def price(self):
        return self.price

    def quantity(self):
        return self.quantity

    def describeProduct(self):
        print('Product ID: %s \n Product Name: %s \n Product Size: %s \n Product Price: %d \n Product Quantity: %d \n' % (
        self.id, self.name, self.size, self.price, self.quantity))


class Warehouse:
  def __init__(self, id, name, localization, shelfs, products):
    self.id = id
    self.name = name
    self.localization = localization
    self.shelfs = shelfs
    self.products = products

  def id(self):
    return self.id

  def name(self):
    return self.name

  def localization(self):
    return self.localization

  def shelfs(self):
    return self.shelfs

  def products(self):
    return self.products

  def describeProduct(self):
    print('Warehouse ID: %s \n Warehouse Name: %s \n Warehouse Localization: %s \n Warehouse Shelfs: %s \n Warehouse products: %s \n' % (
      self.id, self.name, self.localization, self.shelfs, self.products))



class Order:
  def __init__(self, id, user, date, products, origin):
    self.id = id
    self.user = user
    self.date = date
    self.products = products
    self.origin = origin

  def get_id(self):
    return self.id

  def get_user(self):
    return self.user

  def get_date(self):
    return self.date

  def get_products(self):
    return self.products

  def get_origin(self):
    return self.origin

  def set_id(self, value):
      self.id = value

  def set_user(self, value):
      self.user = value

  def set_date(self, value):
      self.date = value

  def set_products(self, value):
      self.products = value

  def set_origin(self, value):
      self.origin = value

  def describeProduct(self):
    print('Orders ID: %s \n Orders User: %s \n Orders Date: %s \n Orders Products: %s \n Orders Origin: %s \n' % (
      self.id, self.user, self.date, self.products, self.origin))

  def CalculateOrderValue(self):
      summaryValue = 0
      for product in self.products:
          summaryValue += (product.price * product.quantity)
      return summaryValue




class BusinessCustomer:
  def __init__(self, id, username, password, firstName, lastName):
    self.id = id
    self.username = username
    self.password = password
    self.firstName = firstName
    self.lastName = lastName

  def id(self):
    return self.id

  def username(self):
    return self.username

  def password(self):
    return self.password

  def firstName(self):
    return self.firstName

  def lastName(self):
    return self.lastName

  def describeProduct(self):
    print('BusinessCustomer ID: %s \n BusinessCustomer Username: %s \n BusinessCustomer Password: %s \n BusinessCustomer First Name: %s \n BusinessCustomer Last Name: %s \n' % (
      self.id, self.username, self.password, self.firstName, self.lastName))

