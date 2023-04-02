from food_details import Admin

class Main:
    def execute(self,choice):
        if choice == 1:
            print("************Add food************")
            admin_function.add_food_item()
        if choice == 2:
            print("************Edit Food************")
            admin_function.edit_food_item()
        if choice == 3:
            print("************View Food************")
            admin_function.view_food_items()
        if choice == 4:
            print("************Remove Food************")
            admin_function.remove_food_item()
main = Main()
admin_function = Admin()
while True:
    choice = int(input("enter \n1.add \n2.edit \n3.view \n4.remove \n:"))
    main.execute(choice)
    
        
    