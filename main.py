import json
import os
class Gun:
    def __init__(self):
        self.name = None
        self.type = None
        self.modelyear = 0
        self.weight = None
        self.price = 0

guns_data = "guns_detail.json"
guns_list = []


if os.path.exists(guns_data):
    with open(guns_data, "r") as file:
        guns_list = json.load(file)

print("Wellcome to **FIREARM INVENTORY**")
print("\nEnter the details of the guns you want to store in the inventory\n")
while True:
    GUN = Gun() 
    GUN.name = input("> Gun name: ") 
    GUN.type = input("> Handgun, Shotgun, Sniper Rifle, AR Rifle or SMG: ") 
    GUN.modelyear = int(input("> Manufacture year: "))
    GUN.weight = float(input("> Weight of gun in grams(in kg for Snipers): "))
    GUN.price = int(input("> Price of the gun: "))
    
    gun_data = {
        "NAME": GUN.name,
        "TYPE": GUN.type,
        "MANUFACTURE YEAR": GUN.modelyear,
        "WEIGHT": GUN.weight,
        "GUN PRICE": GUN.price   
    }

    guns_list.append(gun_data)

    add_another = input("Do you want to add another gun? (yes/no): ")
    if add_another== 'no':
        with open(guns_data, "w") as file:
            json.dump(guns_list,file,indent=2 )
        break

