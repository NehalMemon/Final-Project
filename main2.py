import json

# Load the JSON data
with open("guns_detail.json", "r") as file:
    guns_data = json.load(file)

print("\n** WELCOME TO FIREARM EXPLORER **\n")

print(" AVAILABLE GUNS DETAILS ")

print(
"""
  ** HANDGUN **          ** SHOTGUN **           ** AR RIFLE **         ** SNIPER RIFLE **            ** SMG **
YEAR(1983 TO 2021)     YEAR(1950 TO 2013)      YEAR(1950 TO 2016)       YEAR(1958 TO 1999)        YEAR(1938 TO 2020)
""")
    
gun_type = input("Enter the type of Gun you want \n( Handgun || Shotgun || AR Rifle || Sniper Rifle || SMG ) : ")
min_manufacture_year = int(input("Enter the Minimum Manufacture Year : "))
max_manufacture_year = int(input("Enter the Maximum Manufacture Year : "))
max_price = int(input("Your maximun budget: "))


matching_guns = []

for gun in guns_data:
     if gun["TYPE"] == gun_type \
     and min_manufacture_year <= gun["MANUFACTURE YEAR"] <= max_manufacture_year \
     and gun["GUN PRICE"] <= max_price:   
            matching_guns.append(gun)

if matching_guns:
    print("\nGuns of your interest:\n")
    for gun in matching_guns:
         print(json.dumps(gun, indent=2))

else:
     print("No guns found matching the given requirements.")
