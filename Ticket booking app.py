#import library modules
import time
import random

#define variables
options="yes"
ticket_number=random.randint(0,200)#used in ticket receipt
category=[]
unit_cost=[]
total_qty=[]
total_cost=[]

logodate=time.strftime("%d/%m/%Y",time.localtime(time.time()))
present_month_year=time.strftime("%m/%y",time.localtime(time.time()))
logoclock=time.strftime("%r",time.localtime(time.time()))
datetime=time.strftime("%d/%m/%Y       %H:%M:%S",time.localtime(time.time()))

#print welcome message
print("*"*80)
print(logodate+"        "+"welcome to movie ticket booking app"+"         ",logoclock)
print("*"*80)
print("                                                   "+"developed by Mr.Karthik")
print(" ")

#price details against ticket category
def price_details():
    print(" ")
    print("price details: ")
    print(" ")
    print("ticket category          cost")
    print("*"*30)
    print("Adult                    100$")
    print("child                     20$")
    print("senior                    50$")
    print("prime user                70$")
    print(" ")

#price calculation against category selection
def calculation():
    ticket_type=int(input("how many categories ticket do you want to purcahse?(1-4) : "))

    if ticket_type > 4 or ticket_type == 0:
        print("invalid type count.retry!!!")
        print(" ")
        ticket_type=int(input("how many categories ticket do you want purchase? :"))

    print(" ")
    for i in range(ticket_type):
        choose_category=input("choose a category as 'a' for adult / c for child / s for senior / p for prime user : ")

        #adult selection
        if choose_category=="a":
            adult_qty=int(input("how many adult tickets do you want to purcahse? : "))
            print("")
            total_adult_price=adult_qty*100
            catType="Adult"
            category.append(catType)
            cost=100
            unit_cost.append(cost)
            total_qty.append(adult_qty)
            total_cost.append(total_adult_price)

        #child selection
        elif choose_category=="c":
            child_qty = int(input("how many adult tickets do you want to purcahse? : "))
            print("")
            total_child_price = child_qty * 20
            catType = "child"
            category.append(catType)
            cost = 20
            unit_cost.append(cost)
            total_qty.append(child_qty)
            total_cost.append(total_child_price)

        #senior selection
        elif choose_category == "s":
            senior_qty = int(input("how many adult tickets do you want to purcahse? : "))
            print("")
            total_senior_price = senior_qty * 50
            catType ="senior"
            category.append(catType)
            cost = 50
            unit_cost.append(cost)
            total_qty.append(senior_qty)
            total_cost.append(total_senior_price)

        #prime user selection
        elif choose_category == "p":
            prime_user_qty = int(input("how many adult tickets do you want to purcahse? : "))
            print("")
            total_prime_user_price =prime_user_qty * 50
            catType = "prime_user"
            category.append(catType)
            cost = 50
            unit_cost.append(cost)
            total_qty.append(prime_user_qty)
            total_cost.append(total_prime_user_price)

        else:
            print(" ")
            print("please choose a valid category")
            print(" ")


#cart details before payment
def cart_datail():
    print(" ")
    print("bill details: ")
    print(" ")
    print("ticket category"," ","unit cost"," ","Qty"," ","total cost")
    # use to design template for bill details
    subtotal = 0
    for i in range(len(category)):
        print(category[i], "               ", unit_cost[i], "     ", total_qty[i], "     ", total_cost[i])
        subtotal = int(total_cost[i] + subtotal)
    print("\t\t\t\t\t\t", "---------------------------------------------")
    print("\t\t\t\t\t\t", "subtotal: ", str(subtotal), "$")
    print("")
    tax_price = subtotal * 0.15
    print("\t\t\t\t\t\t", "tax_amount(15%): ", str(tax_price), "$")
    print("\t\t\t\t\t\t", "---------------------------------------------")
    total = tax_price + subtotal
    print("\t\t\t\t\t\t", "total cost of all ticket with tax: ", str(total), "$")
    print("-"*70)


#ticket receipt after payment process
def ticket_receipt():
    print("")
    print("***********************************************************************")
    print("ticket no: ",ticket_number,"\t\t\t\t\t\t","date: ",datetime)
    print("***********************************************************************")
    print("ticket category"," ","unit cost"," ","Qty"," ","total cost")
    # use to design template for bill details
    subtotal = 0
    for i in range(len(category)):
        print(category[i], "               ", unit_cost[i], "     ", total_qty[i], "     ", total_cost[i])
        subtotal = int(total_cost[i] + subtotal)
    print("\t\t\t\t\t\t", "---------------------------------------------")
    print("\t\t\t\t\t\t", "subtotal: ", str(subtotal), "$")
    print("")
    tax_price = subtotal * 0.15
    print("\t\t\t\t\t\t", "tax_amount(15%): ", str(tax_price), "$")
    print("\t\t\t\t\t\t", "---------------------------------------------")
    total = tax_price + subtotal
    print("\t\t\t\t\t\t", "total cost of all ticket with tax: ", str(total), "$")
    print("-"*70)



#function used to write purchase data in to file
def data_write_file(category,total_qty,unit_cost,total_cost):
    with open("transaction.txt","w") as f:
        #design data representation template
        f.write("**************************************\n")
        f.write("ticket no: %d\n"%ticket_number)
        f.write("\n")
        f.write("******************************************")
        f.write("\n")

        for i in range(len(category)):
            f.write("category")
            f.write("%s\n"%category[i])
            f.write("qty")
            f.write("%d\n"%total_qty[i])
            f.write("unit cost :")
            f.write("%d\n"%unit_cost[i])
            f.write("total cost: ")
            f.write("%d\n"%total_cost[i])
            f.write("\n")

        f.write("-------------------------------------------------------\n")
        subtotal=0
        for i in range(len(total_cost)):
            subtotal=total_cost[i]+subtotal
        f.write("total cost %.f\n"%subtotal)
        tax_price=subtotal*0.15
        total=tax_price+subtotal
        f.write("total cost with tax(in $)%.f\n"%total)
        f.write("-----------------------------------------------------------\n")
        f.close()

#ticket purcahsing pricess
def purchase_ticket():
    print("the ticket categories are adult , child ,senior and prime user")
    print("")
    show_price=input("do you want to know the price against cataegories? Y/N or y/n: ")
    print("")
    if show_price in "Y" or show_price in "y":
        price_details()

    elif show_price in "N" or show_price in "n":
        print("lets purchase tickets ")
        print("")
    else:
        print("sorry your answer is not valid ")
        show_price=input("do you want to know the price against categories ? Y/N: ")
        print("")

    calculation()
    print(" ")
    cart_datail()
    print(" ")
    print("pleases enter your credit card details to process payment")
    print(" ")
    print("credit card details : ")
    print("-"*20)

    card_number=input("enter your credit card number (min 14 digit long):")
    if len(card_number)<14 or len(card_number)>14:
        print("")
        print("")
        print("invalid credit card number.retry!!!")
        card_number=input("enter your credit card number(min 14 digit long):")

    print(" ")
    Expairy_date=input("enter valid expairy date of card(month /year like 12/2020):")
    if Expairy_date<=present_month_year:
        print("invalid expairy.retry!!")
        print("")
        expairy_date=input("enter valid expairy date of card (month/year like 12/2020):")
        print(" ")

    print("thank you for information. we are processing your payment.........")
    print(" ")
    print("you have successfully purchased the tickets . ")
    print(" ")
    ticket_receipt()
    print(" ")
    print("thank you for purchasing !!!!! choose option to close the application or continue .")
    data_write_file(category,total_qty,unit_cost,total_cost)

#main menu option
while options in ("yes","y","YES","Y"):
    print("selection options")
    print("--"*10)
    print("1.show price details")
    print("2.purchase tickets")
    print("3.exit")
    print("")
    choice=input("choose a valid option as 1 or 2 or 3 :")
    print(" ")
    if choice=="1":
        price_details()
        buy_ticket=input("do you want to purcahse tickets ? Y/N  or y/n: ")
        print(" ")
        if buy_ticket in ("y","Y"):
            purchase_ticket()
    elif choice=="2":
        purchase_ticket()

    elif choice=="3":
        print("thank you for visiting us !!!!!")
        break

    else:
        print("choose a valid option.")
        options="yes"
