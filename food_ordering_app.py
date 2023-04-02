class FoodItem:
    def __init__(self,food_Id,name, quantity, price, discount, stock):
        self.food_Id = food_Id
        self.name = name
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.stock = stock

    def set_food_Id(self,food_Id):
        self.food_Id = food_Id

    def get_foodId(self):
        return self.food_Id
    
    def set_name(self,name):
        self.name = name

    def get_name(self):
        return self.name
    
    def set_quantity(self,quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity
    
    def set_price(self,price):
        self.price = price

    def get_price(self):
        return self.price
    
    def set_discount(self,discount):
        self.discount = discount

    def get_discount(self):
        return self.discount
    
    def set_stock(self,stock):
        self.stock = stock

    def get_stock(self):
        return self.stock
    def __str__(self):
        return f"Food ID : {self.food_Id} \nFood Name : {self.name} \nFood Quantity : {self.quantity} \nFood Price : {self.price} \nFood Discount : {self.discount} \nFood Stock : {self.stock} \n:"
    



    
