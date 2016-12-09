# This File that would contain Classes for bicycle, Customer and bicycleShop

class Bicycle(object):
    def __init__(self,p_model_name,p_weight,p_production_cost):
        self.model_name = p_model_name
        self.weight = p_weight
        self.production_cost = int(p_production_cost)

    def update_prod_cost(self,p_production_cost):
        self.production_cost = int(p_production_cost)

    def update_weight(self,p_weight):
        self.weight = p_weight

    def get_model_name(self):
        return self.model_name

    def get_prod_cost(self):
        return int(self.production_cost)


class BikeShops(object):
    def __init__(self,p_shop_name):
        self.shop_name = p_shop_name
        self.shop_inventory = {}
            # Public
            # key = Model Name
            # para 1 = List
            # para 1.0 = Inventory_Count
            # para 1.1 = Bicycle Production Cost per Unit from Bicycle Instance

        self.shop_books = {}
            # Private
            # key = Model Name
            # para 1 = List
            # para 1.0 = Total Inventory / Quantity Bought
            # para 1.1 = Total Sold Quantity
            # para 1.2 = Total Quantity Available
            # para 1.3 = Total Production cost for the given Model / Total Money Spent on Buying this Model
            # para 1.4 = Total Sales for the given Model

        #default margin set to 20%
        self.margin = 0.2
        self.total_cost = 0
        self.total_sales = 0

    def set_margin(self,p_margin):
        # expected value in % eg : 0.02 etc
        self.margin = float(int(p_margin)/100)

    def set_inventory(self,p_model_name, p_model_list):
        # initializing Inventory
        # Called when new bicycle Model is added to the shop first
        self.shop_inventory[p_model_name] = p_model_list
        self.model_total_production_cost = p_model_list[0] * p_model_list[1]
        self.shop_books[p_model_name] = [p_model_list[0],0,p_model_list[0],self.model_total_production_cost,0]

    def update_inventory(self,p_model_name,p_count,p_mode='SUB'):
        # add to both Inventory Dictionary and Book Dictionary

        shop_inv_invcount_0 = int(self.shop_inventory[p_model_name][0])
        shop_book_qty_sold_1 = int(self.shop_books[p_model_name][1])
        shop_book_qty_available_2 = int(self.shop_books[p_model_name][2])
        shop_book_prod_cost_3 = int(self.shop_books[p_model_name][3])
        shop_book_sales_4 = int(self.shop_books[p_model_name][4])
        production_cost = int(self.shop_inventory[p_model_name][1])

        if p_mode == "ADD":
            #Total Inventory Count ( increase)
            shop_inv_invcount_0 += int(p_count)
            self.shop_inventory[p_model_name][0] = shop_inv_invcount_0
            self.shop_books[p_model_name][0] = shop_inv_invcount_0

            #Total Quantity available
            shop_book_qty_available_2 = shop_inv_invcount_0 - shop_book_qty_sold_1
            self.shop_books[p_model_name][2] = shop_book_qty_available_2

            #Total Cost by Shop to own the inventory for given model
            shop_book_prod_cost_3 = shop_inv_invcount_0 * production_cost
            self.shop_books[p_model_name][3] = shop_book_prod_cost_3

            #total cost for the shop to Own the Bicycle Inventory all Model
            self.update_total_cost()

        else:
            if shop_inv_invcount_0 > 0:
                #Total Sold Quantity (increase)
                shop_book_qty_sold_1 += int(p_count)
                if (shop_inv_invcount_0 - shop_book_qty_sold_1) >= 0 :
                    self.shop_books[p_model_name][1] = shop_book_qty_sold_1

                    #Total Quantity Available
                    shop_book_qty_available_2 = shop_inv_invcount_0 - shop_book_qty_sold_1
                    self.shop_books[p_model_name][2] = shop_book_qty_available_2

                    #Total sales per Model
                    shop_book_sales_4 = shop_book_qty_sold_1 + (shop_book_qty_sold_1 * float(self.margin))
                    self.shop_books[p_model_name][4] = shop_book_sales_4

                    #Total Sales for all Models for the Shop
                    self.update_total_sales()

                else:
                    print("Quantity Ordered Exceeds the quantity Available in Inventory ")

            else:
                print("NULL Inventory")
                return "ERROR"

    def get_inventory(self,p_model_name):
        return self.shop_books[p_model_name][2]

    def get_unit_cost(self,p_model_name):
        return self.shop_inventory[p_model_name][1]

    def update_total_cost(self):
        for x in self.shop_books:
            self.total_cost += int(self.shop_books[x][3])

    def update_total_sales(self):
        for x in self.shop_books:
            self.total_sales += float(self.shop_books[x][4])
            #print ("****** total Sales {0} and {1} and {2} ******".format(self.total_sales,int(self.shop_books[x][4]),self.shop_books[x]))

    def get_shop_profit(self):
        return self.total_sales


class Customer(object):
    Customer = Customer_Directory = {}
       #key = Customer Name
       #para1 = list
       #para1.0 = Fund Available
       #para1.1 = Purchase eligability
       #para1.2 = list
       #para1.2.0= bicycle ModelName Purchased

    def __init__ (self,p_cust_name,p_fund,p_purchase_eligability):
        self.cust_name = p_cust_name
        self.fund = int(p_fund)
        self.purchase_eligability = p_purchase_eligability
        Customer.Customer_Directory[p_cust_name] = [p_fund,p_purchase_eligability,[]]

    def update_fund(p_cust_name,p_fund,p_mode='SUB'):
        cal = int(Customer.Customer_Directory[p_cust_name][0])
        if p_mode =="ADD":
            cal += int(p_fund)
            Customer.Customer_Directory[p_cust_name][0] = cal
        else:
            if cal > 0:
                cal_temp = cal
                cal -= int(p_fund)
                if cal > 0:
                    Customer.Customer_Directory[p_cust_name][0] = cal
                else:
                    print("**** Not sufficient Fund Available for Purchase ****")
                    print("**** For {0} , available Credit/Fund is : {1}".format(p_cust_name,cal_temp))
                    return 1

            else:
                print("No Fund Available for Deduction")
                Customer.update_customer_eligability(p_cust_name,'N')
                return 1
        return 0

    def get_customer_name(self):
        return self.cust_name

    def get_fund(self):
        return self.fund

    def check_customer_elibability(self):
        return self.purchase_eligability

    def update_customer_eligability(p_cust_name,p_purchase_eligability):
        #self.purchase_eligability = p_purchase_eligability
        Customer.Customer_Directory[p_cust_name][1] = p_purchase_eligability


if __name__ == "__main__":

    # 3 New Customer
    customer1 = Customer("VIBHU1","500","Y")
    customer2 = Customer("VIVHU2","200","Y")
    customer3 = Customer("VIBHU3","1000","Y")


    # 6 new bicycle Model
    bicycleModel1 = Bicycle("BBMX",300,250)
    bicycleModel2 = Bicycle("RRMX",450,345)
    bicycleModel3 = Bicycle("LLMX",234,120)
    bicycleModel4 = Bicycle("TTMX",456,100)
    bicycleModel5 = Bicycle("GGMX",200,150)
    bicycleModel6 = Bicycle("CCMX",300,160)

    # 1 new Shop
    bikeShop1 = BikeShops("Bike Shop Inc")

    #set sales margin
    bikeShop1.set_margin(25)

    # adding bicycle Model to Shop inventory List
    bikeShop1.set_inventory(bicycleModel1.get_model_name(),[10,bicycleModel1.get_prod_cost()])
    bikeShop1.set_inventory(bicycleModel2.get_model_name(),[20,bicycleModel2.get_prod_cost()])
    bikeShop1.set_inventory(bicycleModel3.get_model_name(),[5,bicycleModel3.get_prod_cost()])
    bikeShop1.set_inventory(bicycleModel4.get_model_name(),[2,bicycleModel4.get_prod_cost()])
    bikeShop1.set_inventory(bicycleModel5.get_model_name(),[25,bicycleModel5.get_prod_cost()])
    bikeShop1.set_inventory(bicycleModel6.get_model_name(),[15,bicycleModel6.get_prod_cost()])

    #Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget
    # mentioned amount check is 200

    print ("**** Print the name of each customer, and a list of the bikes offered by the bike shop that they can afford given their budget ****")
    for x,y in Customer.Customer_Directory.items():
        if int(y[0]) >= 200:
            print("Eligable Customer Names : {0} and there Budget : {1}".format(x,y[0]))
            for i,l in bikeShop1.shop_inventory.items():
                if int(y[0]) >= l[1]:
                    print ("Bicycle Available for {0} are {1}".format(x,i))
        else:
            print ("For given Budget for bicycle, No Customer are eligable")


    #Print the initial inventory of the bike shop for each bike it carries
    print()
    print("**** Print the initial inventory of the bike shop for each bike it carries ****")
    for x,y in bikeShop1.shop_inventory.items():
        print("Model name : {} , respective inventory available : {}".format(x,y[0]))

    # Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund
    print()
    print("**** Have each of the three customers purchase a bike then print the name of the bike the customer purchased, the cost, and how much money they have left over in their bicycle fund ****")


    i_margin = input("Enter the profit margin, you want to sell the bicycle :")
    bikeShop1.set_margin(i_margin)

    count = 0
    while (count < len(Customer.Customer_Directory.items())):
        try:
            print("--- iteration : {} ---".format(count))
            customer_name = (input("Enter the name of the Customer :")).upper()
            bicycle_name = input("Enter the name of the Bicycle Model :").upper()
            bicycle_count = input("Enter the Number of Cylce to Purchase :")

            cost = bikeShop1.get_unit_cost(bicycle_name)
            if Customer.update_fund(customer_name,cost)== 0:
                check = bikeShop1.update_inventory(bicycle_name,bicycle_count)
                if check == "ERROR":
                    break
                Customer.Customer_Directory[customer_name][2].append(bicycle_name)


            print(" Bicycle Name/Model Purchased by {0} : {1} ".format(customer_name,Customer.Customer_Directory[customer_name][2]))
            print(" Available fund left for purchase for Customer name {0} : {1}".format(customer_name,Customer.Customer_Directory[customer_name][0]))
            count+=1

        except KeyError:
            print("Invalid Entry Please try Again .....")


    # After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes
    print()
    print("**** After each customer has purchased their bike, the script should print out the bicycle shop's remaining inventory for each bike, and how much profit they have made selling the three bikes ****")
    for x,y in bikeShop1.shop_books.items():
        print("Available Inventory for {0} : {1}".format(x,y[2]))

    print()
    print("Total Profit Made by Shop : {0}".format(bikeShop1.get_shop_profit()))
    print()
    print("****END****")





