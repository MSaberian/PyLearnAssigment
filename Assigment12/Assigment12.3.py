import qrcode

PRODUCTS = []

def read_from_database():
    f = open("database.txt","r")

    for line in f:
        line = line.replace('\n', '')
        result = line.split(",")
        my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
        PRODUCTS.append(my_dict)

    f.close()

def write_to_database():
    open('database.txt', 'w').close()
    file_object = open('database.txt', 'a')
    for product in PRODUCTS:
        file_object.write(str(product["code"])+","+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n')
    file_object.close()

#     1001,piaz,3600,500
# 1002,sos,15000,122
# 1003,nushabe,10000,321


def add():
    code = input("enter code: ")
    name = input("enter name: ")
    price = input("enter price: ")
    count = input("enter count: ")
    new_product = {'code': code, 'name': name, 'price': price, 'count': count}
    PRODUCTS.append(new_product)

def edit():
    user_input = input("enter your code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            print("code\t\tname\t\tprice\t\tcount")
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"])
            print("Which item do you want to change?")
            print("1- Name      2- Price        3- count")
            user_choice = int(input("your choice: "))
            if user_choice == 1:
                new_name = input('New name: ')
                product['name'] = new_name
            elif user_choice == 2:
                new_price = input('New price: ')
                product['price'] = new_price
            elif user_choice == 3:
                new_count = input('New count: ')
                product['count'] = new_count
            print('Data changed successfully')

            break
    else:
        print("not found")

def remove():
    user_input = input("enter your code: ")
    index = 0
    for product in PRODUCTS:
        index += 1
        if product["code"] == user_input:
            print("code\t\tname\t\tprice\t\tcount")
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"], "\t\t", product["count"])
            print("Are you soure you want to remove this product?")
            print("1- yes      2- no  ")
            user_choice = int(input('your choice: '))
            if user_choice == 1:
                PRODUCTS.pop(index-1)
            elif user_choice == 2:
                break
            print('Data removed successfully')

            break
    else:
        print("not found")

def search():
    user_input = input("type your keyword: ")
    for product in PRODUCTS:
        if product["code"] == user_input or product["name"] == user_input:
            print(product["code"], "\t\t", product["name"], "\t\t", product["price"])
            break
    else:
        print("not found")



def show_list():
    print("code\t\tname\t\tprice")
    for product in PRODUCTS:
        print(product["code"], "\t\t", product["name"], "\t\t", product["price"])

def qrcode0():
    user_input = input("enter your code: ")
    for product in PRODUCTS:
        if product["code"] == user_input:
            print("code\t\tname\t\tprice\t\tcount")
            temp_string = str(product["code"]) + "\t\t" + str(product["name"]) + "\t\t" + str(product["price"]) + "\t\t"+ str(product["count"])
            print(temp_string)
            QRcode = qrcode.make(temp_string)
            QRcode.save(product["code"] + "QrCode.png")
            print('QrCode saved successfully')

            break
    else:
        print("not found")

def buy_new_product(shopper_products,user_input):
    for product in PRODUCTS:
        if product["code"] == user_input:
            user_count = int(input('enter your count: '))
            if user_count <= int(product['count']):
                product['count'] = int(product['count']) - user_count
                new_product = {'code': product["code"], 'name': product["name"], 'price': product["price"], 'count': user_count}
                shopper_products.append(new_product)
                print(str(user_count) + ' ' + product["name"] + ' add to your list')
            else:
                print('Insufficient inventory')

            break
    else:
        print("not found")
    return shopper_products

def print_purchase_invoice(shopper_products):
    total_price = 0
    print('\n------------------------\n')
    print('\n    *   *   *   *   *   *   *     ')
    print('     Purchase Invoice     \n')
    print("code\t\tname\t\tprice\t\tcount")
    for product in shopper_products:
        print(str(product["code"]) + "\t\t" + str(product["name"]) + "\t\t" + str(product["price"]) + "\t\t"+ str(product["count"]))
        total_price += int(product["price"])*int(product['count'])
    print('\nTotal price is: ' , str(total_price))
    print('Thanks for your shopping')
    print('\n------------------------\n')


def buy():    
    shopper_products = []
    print('Exit by \'exit\'')
    while True:
        user_input = input("enter your code: ")
        if user_input == 'exit':
            print_purchase_invoice(shopper_products)

            break
        else:
            buy_new_product(shopper_products, user_input)

def show_menu():
    print("1- Add")
    print("2- Edit")
    print("3- Remove")
    print("4- Search")
    print("5- Show List")
    print("6- Buy")
    print("7- Creat Qr Code")
    print("8- Exit")


print("welcome to Mahammad Store")
print("Loading...")
read_from_database()
print("Data loaded.")


while True:
    show_menu()
    choice_user = input("enter your choice: ")
    if choice_user.isdigit():
        choice = int(choice_user)
        if 0 < choice < 9:
            if choice == 1:
                add()
            elif choice == 2:
                edit()
            elif choice == 3:
                remove()
            elif choice == 4:
                search()
            elif choice == 5:
                show_list()
            elif choice == 6:
                buy()
            elif choice == 7:
                qrcode0()
            elif choice == 8:
                write_to_database()
                exit(0)
        else:
            print('⚠ you have to enter number between 1-8')
    else:
        print('⚠ you have to enter number between 1-8')

