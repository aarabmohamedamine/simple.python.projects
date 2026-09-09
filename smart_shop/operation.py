from storage import save_product

def display_menu():
    print("------Menu------")
    print("1.add product ")
    print("2.View products")
    print("3. View total")
    print("4.exit")


def get_valid_price():
    while True:
     try:
        price = int(input("Enter a valid price : "))
        if price > 0:
           return price
        else:
           print("Price must be greather than 0 ")
     except ValueError:
      print("please enter a number !! ") 
def valid_choice():
    while True:
        try:
            display_menu()
            choice = int(input("Enter your choice : "))
            return choice
        except ValueError :
            print('Try again !!')


def add_product(product_list):
   while True:
      try : 
        product_name = input("enter the product name : ")
        price = get_valid_price()
        produit_prix = {"Product name" :  product_name , "Price" : price 
                        }
        product_list.append(produit_prix)
        print('Product added !')
        save_product(product_list)
        break
      except ValueError:
         print('Try again')
def view_products(product_list):
   for product in product_list:
      print(product)

    
def total(product_list):
    Total  =  0
    for expense in product_list:
        Total = Total + expense["Price"]

    return Total


