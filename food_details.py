from food_ordering_app import FoodItem 

class Admin:

    food_list = []
    def add_food_item(self):
        food_Id= int(input('enter: '))
        name= input('Enter name:')
        quantity= input('Enter quantity:')
        price= float(input('enter price:'))
        discount= input('Enter discount:')
        stock= input('Enter stock:')
        food_obj= FoodItem(food_Id,name,quantity,price,discount,stock)
        self.food_list. append(food_obj)
        print("Food Successfully Added!")

    

    def edit_food_item(self):
        foodid = int(input("enter id: "))
        for item in self.food_list:
            if foodid == item.get_foodId():
                foodname= input("Enter name:")
                foodquantity= input("Enter quantity:")
                foodprice= input("Enter price:")
                foodiscount= input("Enter discount:")
                foodstock= input("Enter stock:")
                

                item.set_name(foodname)
                item.set_quantity(foodquantity)
                item.set_price(foodprice)
                item.set_discount(foodiscount)
                item.set_stock(foodstock)

                print("Food item updated successfully!")
                break
        else:
            print("Invalid food item ID")

    def view_food_items(self):
        for i in self.food_list:
            print(i,"\n:")


    def remove_food_item(self):
        foodId = int(input("enter id:"))
        for food in self.food_list:
            if foodId == food.get_foodId():
                self.food_list.remove(food)
                print("Food item removed successfully!")
                break
        else:
            print("Invalid food item ID")





    
