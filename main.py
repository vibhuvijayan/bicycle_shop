import cycle

# 3 New Customer
customer1 = cycle.Customer("VIBHU1","500","Y")
customer2 = cycle.Customer("VIVHU2","200","Y")
customer3 = cycle.Customer("VIBHU3","1000","Y")


# 6 new bicycle Model
bicycleModel1 = cycle.Bicycle("BBMX",300,250)
bicycleModel2 = cycle.Bicycle("RRMX",450,345)
bicycleModel3 = cycle.Bicycle("LLMX",234,120)
bicycleModel4 = cycle.Bicycle("TTMX",456,100)
bicycleModel5 = cycle.Bicycle("GGMX",200,150)
bicycleModel6 = cycle.Bicycle("CCMX",300,160)

# 1 new Shop
bikeShop1 = cycle.BikeShops("Bike Shop Inc")

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
budget_baseline = input("Enter the baseline budget for the customer : ")
for x,y in cycle.Customer.Customer_Directory.items():
    if int(y[0]) >= int(budget_baseline):
        print("Eligable Customer Names : {0} and there Budget : {1}".format(x,y[0]))
        for i,l in bikeShop1.shop_inventory.items():
            if int(y[0]) >= l[1]:
                print ("Bicycle Available for {0} are {1}".format(x,i))
    else:
        print ("For given Budget for bicycle, {0} is not eligable".format(x))


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
while (count < len(cycle.Customer.Customer_Directory.items())):
    try:
        print("--- iteration : {} ---".format(count))
        customer_name = (input("Enter the name of the Customer :")).upper()
        bicycle_name = input("Enter the name of the Bicycle Model :").upper()
        bicycle_count = input("Enter the Number of Cylce to Purchase :")

        cost = bikeShop1.get_unit_cost(bicycle_name)
        if cycle.Customer.update_fund(customer_name,cost)== 0:
            check = bikeShop1.update_inventory(bicycle_name,bicycle_count)
            if check == "ERROR":
                break
            cycle.Customer.Customer_Directory[customer_name][2].append(bicycle_name)


        print(" Bicycle Name/Model Purchased by {0} : {1} ".format(customer_name,cycle.Customer.Customer_Directory[customer_name][2]))
        print(" Available fund left for purchase for Customer name {0} : {1}".format(customer_name,cycle.Customer.Customer_Directory[customer_name][0]))
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

