# Create constructor and objects of Online_Shopping class

class OnlineShopping:
    def __init__(self, product_name, product_price):
        print(f"OnlineShopping constructor is running for {product_name}")
        self.product_name = product_name
        self.product_price = product_price

shopping1 = OnlineShopping("Headphones", 2500)
shopping2 = OnlineShopping("Backpack", 1800)

print(shopping2.product_name)
print(shopping1.product_price)