# ------------------------- PRODUCT CLASS -------------------------

# Define a base class 'Product' to represent generic products
class Product:
    # Constructor to initialize product attributes
    def __init__(self, name, price, deal_price, ratings): 
        #The use of __init__ is to initialize the attributes of the class when an object is created. it is a special method in Python that is automatically called when a new instance of the class is created.
        # Self is a reference to the current instance of the class, allowing us to access and modify the attributes of that instance.
        self.name = name              # Name of the product
        self.price = price            # Original price of the product   300
        self.deal_price = deal_price  # Discounted price of the product  250
        self.ratings = ratings        # Product ratings
        self.you_save = price - deal_price  # Calculate the discount amount #50
        
    # Instance method to display product details
    def display_Product_details(self):
        print("Product name:{}".format(self.name))
        print("Price:{}".format(self.price))
        print("Deal Price:{}".format(self.deal_price))
        print("Ratings:{}".format(self.ratings))
        print("You Save:{}".format(self.you_save))
        
    # Method to return the deal price of the product
    def get_deal_price(self):
        return self.deal_price

# ------------------------- ELECTRONIC ITEMS SUBCLASS -------------------------

# Subclass for electronic products, inherits from Product
class ElectronicItems(Product):
    # Constructor includes additional attribute: warranty_in_months
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)  # Call parent constructor
        self.warranty_in_months = warranty_in_months        # Add warranty info
    
    # Override method to display product details along with warranty
    def display_Product_details(self):
        super().display_Product_details()                   # Call parent display method
        print("Warranty in Months:{}".format(self.warranty_in_months))
        
# ------------------------- GROCERY ITEMS SUBCLASS -------------------------

# Subclass for grocery products, inherits from Product
class GroceryItems(Product):
    # Constructor includes additional attribute: expiry_date
    def __init__(self, name, price, deal_price, ratings, expiry_date):
        super().__init__(name, price, deal_price, ratings)  # Call parent constructor
        self.expiry_date = expiry_date                       # Add expiry date info
    
    # Override method to display product details along with expiry date
    def display_Product_details(self):
        super().display_Product_details()                   # Call parent display method
        print("Expiry Date:{}".format(self.expiry_date))
    
# ------------------------- ORDER CLASS -------------------------

# Define an Order class to manage cart and orders
class Order:
    # Class variable to store delivery charges for different delivery methods
    delivery_charges =  {"Normal": 0, "Prime delivery": 100 }
    
    # Constructor to initialize an order
    def __init__(self, delivery_method, delivery_address):
        self.items_in_cart = []  #[(AC,1),(Milk,2)]          # List to store products and quantities
        self.delivery_method = delivery_method  # Selected delivery method
        self.delivery_address = delivery_address  # Delivery address
    
    # Method to add items to the cart
    def add_items(self, product, quantity):
        item = (product, quantity)      # Store product and quantity as a tuple
        self.items_in_cart.append(item) # Add tuple to the cart list
        
    # Method to display order details
    def display_order_details(self):
        print("Delivery Method: {}".format(self.delivery_method))
        print("Delivery Address: {}".format(self.delivery_address))
        print("Products:")
        # Loop through items in the cart and display their details
        for product, quantity in self.items_in_cart:
            product.display_Product_details()  # Call product-specific display method
            print("Quantity: {}".format(quantity))
        print("----------------------------------------")
        
        # Calculate total bill including delivery charges
        total_bill = self.get_total_bill()
        print("Total Bill: {}".format(total_bill))
    
    # Method to calculate total bill
    def get_total_bill(self):
        total_bill = 0   #40080
        for product, quantity in self.items_in_cart:
            total_bill += product.get_deal_price() * quantity  # Multiply deal price by quantity
            #total_bill=total_bill + product.get_deal_price() * quantity
            #total_bill=0+40000*1=40000
            #total_bill=40000+40*2=40080
        # Add delivery charges based on delivery method
        order_delivery_charges = Order.delivery_charges[self.delivery_method]
        return total_bill + order_delivery_charges
    
    # Class method to update delivery charges
    # The @classmethod decorator indicates that this method belongs to the class and can be called on the class itself, rather than on an instance of the class. 
    # It allows us to modify class-level data (like delivery_charges) without needing to create an instance of the Order class.
    @classmethod  
    def update_delivery_charges(cls, delivery_method, new_charge): #the cls parameter is a reference to the class itself, allowing us to access and modify class variables like delivery_charges.
        cls.delivery_charges[delivery_method] = new_charge   # Update the delivery charge for the specified delivery method now we can call this method using the class name Order.update_delivery_charges("Normal", 50) without needing to create an instance of the Order class.
    
    

# ------------------------- CREATING PRODUCTS -------------------------

# Create an electronic item 'AC'
AC = ElectronicItems("AC", 45000, 40000, 4.5, 24)

# Create a grocery item 'Milk'
milk = GroceryItems("Milk", 50, 47.5, 4.8, "Jan 2024")

# ------------------------- CREATING ORDER -------------------------

# Create an order with normal delivery to Hyderabad
my_orders = Order("Normal", "Hyderabad")

# Add products to the order
my_orders.add_items(AC, 1)   # 1 AC
my_orders.add_items(milk, 2) # 1 Milk

# ------------------------- UPDATE DELIVERY CHARGES -------------------------

# Update normal delivery charge from 0 to 50
Order.update_delivery_charges("Normal", 50)

# ------------------------- DISPLAY ORDER DETAILS -------------------------

# Display all order information including products, quantities, and total bill
my_orders.display_order_details()
