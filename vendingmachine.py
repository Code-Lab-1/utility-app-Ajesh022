# Catagorizing items in different catagory
items = {
    "Drinks": {
        "1": {"item": "Pepsi", "price":3, "stock":15},
        "2": {"item": "Coca Cola", "price":3, "stock":20},
        "3": {"item": "Water", "price":2, "stock":20},
        "4": {"item": "Mango Juice", "price":4, "stock":15},
    },
    "Chocolates": {
        "5": {"item": "Twix", "price":3, "stock":20},
        "6": {"item": "Bounty", "price":3,"stock":15},
        "7": {"item": "Galaxy", "price":2, "stock":20},
        "8": {"item": "Dairy Milk", "price":4, "stock":20},
        "9":{"item": "Toblerone", "price":4, "stock":15},
        "10":{"item": "KitKat", "price":2, "stock":15},
    },
    "Snacks": {
        "11": {"item": "Lays", "price":3, "stock":20},
        "12": {"item": "Cheetos", "price":3, "stock":15},
        "13": {"item": "Takis", "price":4, "stock":15},
        "14": {"item": "Oreo", "price":3, "stock":20},
        "15": {"item": "Popcorn", "price":2, "stock":15},
        "16": {"item": "Pringles", "price":4, "stock":15}    
     },
     "Coffee": {
        "17": {"item": "Cappucino", "price":4, "stock":15},
        "18": {"item": "Cold Coffee", "price":3, "stock":20},
        "19": {"item": "Latte", "price":4, "stock":20},
        "20": {"item": "Espesso", "price":4, "stock":15},
        "21": {"item": "Milk Coffee", "price":3, "stock":20},
        "22": {"item": "Black Coffee", "price":3, "stock":20},
     },
}
# Function to print menu of items
def print_menu(item):
    print("Menu:\n")
    for category, category_items in item.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f} dhs)')
        print()

# Function to get valid code from user
def get_code(item):
    while True:
        code= input("Enter code: ")
        # check if code is valid
        for category, category_items in item.items():
            if code in category_items:
                return code
        print("invalid code. Please try again.")

# Function to get valid amount of money from user 
def get_money(item, code):
    # search for item in Drinks , Chocolate,Snacks and Coffee Dictionaries
    for category, category_items in item.items():
        if code in category_items:
            item= category_items[code]
            break
    else:
        print(f'Invalid code "{code}".')
        return
    
    while True:
        money= float(input("Enter money: "))
        # check if the amount was enough
        if money > item["price"] or money==item["price"]:
            return money 
            dispense_item(item, code,money)
        print(
            f'Not enough money. please insert {item["price"] - money:.2f} dhs more.'
         )


# Function to dispense item and calcuate change
def dispense_item(item,code, money):
    # search for item in Drinks, Chocolate,Snacks and Coffee Dictionaries
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f'Invalid code "{code}".')
        return
    
    # check if item is in stock
    if item["stock"] > 0:
        #dispense item and calculate change
        print(f'\ndispensing {item["item"]}...')
        change = money - item["price"]
        item["stock"]-= 1
        print(f"Returning {change: .2f} DHS...\n")
    else:
        print(f'\nError: {item["name"]} is out of stock')


# Function to suggest additional purchase based on previous purchase
def suggest_purchase(item, code):
    if code in items["Drinks"]:
        print("You might also like:")
        for code, item in items["Chocolates"].items():
            print(f'{code}: {item["item"]}({item["price"]:.2f}dhs)')
    elif code in items["Snacks"]:
        print("You might also like:")
        for code, item in items["Coffee"].items():
            print(f'{code}: {item["item"]} ({item["price"]:.2f}dhs)')



#main program
while True:
    # print menu of items
    print_menu(items)
    # get valid code from user
    code = get_code(items)
    # get valid amount of money from user
    money = get_money(items, code)
    # dispense item and calculate change
    dispense_item(items, code, money)
    # suggest additional purchase based on previous purchase
    suggest_purchase(items, code)
    # prompt user to continue or exit 
    while True:
        response = input("\nWould you like to make another purchase? (y/n) ")
        if response.lower() == "y":
            break
        elif response.lower() == "n":
            print("Thank you for using the vending machine!")
            exit()
        else:
            print("Invalid response. Please try again.")

