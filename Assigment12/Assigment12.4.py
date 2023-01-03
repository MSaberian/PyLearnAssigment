class Product:
    def __init__(self, i, n, p, c):
        self.id = i
        self.name = n
        self.price = p
        self.sount = c

    @staticmethod
    def add():
        code = input("enter code: ")
        name = input("enter name: ")
        price = input("enter price: ")
        count = input("enter count: ")
        # new_product = {'code': code, 'name': name, 'price': price, 'count': count}
        new_product = Product(code, name, price, count)
        PRODUCTS.append(new_product)

    def edit(self):
        ...
    @staticmethod
    def search():
        ...

    def show(self):
        ...

    @staticmethod
    def show_list():
        ...

    def remove(self):
        ...

    def buy(self):
        ...

class Database:
    def __init__(self):
        ...


    def read():
        f = open("database.txt","r")

        for line in f:
            line = line.replace('\n', '')
            result = line.split(",")
            # my_dict = {"code": result[0], "name": result[1], "price": result[2], "count": result[3]}
            my_obj = Product(result[0], result[1], result[2], result[3])
            PRODUCTS.append(my_dict)

    

    def write():
        ...
        # open('database.txt', 'w').close()
        # file_object = open('database.txt', 'a')
        # for product in PRODUCTS:
        #     file_object.write(str(product["code"])+","+str(product['name'])+','+str(product['price'])+','+str(product['count'])+'\n')
        # file_object.close()

        f.close()

db = Database()
PRODUCTS = []

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
db.read()
print("Data loaded.")


while True:
    show_menu()
    choice_user = input("enter your choice: ")
    if choice_user.isdigit():
        choice = int(choice_user)
        if 0 < choice < 9:
            if choice == 1:
                Product.add()
            elif choice == 2:
                code = int(input('enter product id: '))
                for product in PRODUCTS:
                    if product.id == id:
                        product.edit()

            elif choice == 3:
                code = int(input('enter product id: '))
                for product in PRODUCTS:
                    if product.id == id:
                        product.remove()

            elif choice == 4:
                Product.search()

            elif choice == 5:
                Product.show_list()

            elif choice == 6:
                buy()

            elif choice == 7:
                qrcode0()
            elif choice == 8:
                db.write()
                exit(0)
        else:
            print('⚠ you have to enter number between 1-8')
    else:
        print('⚠ you have to enter number between 1-8')

