'''
while True :
    print("=============== PLANT PURCHASE & BILLING SYSTEM ===============")
    print("Welcome to The Green Leaf Nursery🌱 ")

    customer_name = input("Please Enter your Good Name : ")
    contact= int(input("Enter your Mobile Number : "))

    print("WE HAVE VARIOUS CATEGORIES OF PLANT LIKE --")

    print("1. Indoor Plants")
    print("2. Outdoor Plants")
    print("3. Flowering Plants") 
    print("4. Medicinal Plants")

    price =0
    bill= 0
    plastic_pot =100
    ceramic_pot =250
    fertilizer_price = 250
    premium_bill= 0

    category = int(input("SELECT THE PLANT CATEGORY : "))
    

    match category:
        case 1:
            indoor=input(" Which Indoor Plant Would You Prefer?🎍 ").lower()
            if indoor == "snake plant":
                plant_name ="Snake Plant"
                price =250
                print("Price is :" ,price)

            elif indoor== "money plant":
                plant_name ="Money Plant"
                price = 180
                print("Price is : ",price)

            elif indoor == "peace lily":
                plant_name ="Peace lily"
                price = 350
                print("Price is :",price)

            elif indoor == "spider plant":
                plant_name ="Spider Plant"
                price = 220
                print("Price is :",price)

            else:
                print("Oops!, Plant Not Found.")
                print("WE WILL TRY TO BRING IT SOON >>>")
                break

        case 2:
            outdoor=input(" Which outdoor Plant Would You Prefer?🌳 ").lower()
            if outdoor == "neem plant":
                plant_name ="Neem Plant"
                price =300
                print("Price is :" ,price)

            elif outdoor== "mango plant":
                plant_name ="Mango Plant"
                price = 450
                print("Price is : ",price)

            elif outdoor == "ashoka plant":
                plant_name ="Ashoka Plant"
                price = 380
                print("Price is :",price)

            elif outdoor == "guava plant":
                plant_name =" Guava Plant"
                price = 400
                print("Price is :",price)

            else:
                print("Oops!, Plant Not Found.")
                print("WE WILL TRY TO BRING IT SOON >>>")
                break

        case 3:
            flower =input(" Which Flowering Plant Would You Prefer?🌷 ").lower()
            if flower == "rose":
                plant_name ="Rose Plant"
                price =200
                print("Price is :" ,price)

            elif flower== "daisy":
                plant_name ="Daisy Plant"
                price = 250
                print("Price is : ",price)

            elif flower == "marigold ":
                plant_name ="Marigold Plant"
                price = 150
                print("Price is :",price)

            elif flower == "jasmine":
                plant_name ="Jasmine Plant"
                price = 300
                print("Price is :",price)

            else:
                print("Sorry!, Plant Not Found.")
                print("WE WILL TRY TO BRING IT SOON >>>")
                break

        case 4 :
            medicinal =input(" Which Medicinal Plant Would You Prefer?🌿 ").lower()
            if medicinal == "aloe vera":
                plant_name ="Aloe vera Plant"
                price =120
                print("Price is :" ,price)

            elif medicinal == "tulsi":
                plant_name ="Tulsi Plant"
                price = 80
                print("Price is : ",price)

            elif medicinal == "mint ":
                plant_name ="Mint Plant"
                price = 100
                print("Price is :",price)

            elif medicinal == "giloy":
                plant_name =" Giloy Plant"
                price = 190
                print("Price is :",price)
            else:
                print("Plant not found.. we will get it soon...")
                break
        case __ :
                print("CHOOSE CORRECT CATEGORY ")
                continue

    pot= input("Do you want a Pot (yes/no) ?").lower()
   
    match pot :
        case "yes":
            pot_type= input("which type of pot do you prefer (plastic pot/ ceramic pot) ? ").lower()
            if pot_type =="plastic pot" :
                pot_name = "Plastic Pot"
                pot_price =100
                print("Plastic Pot Price = ",pot_price)

            elif pot_type == "ceramic pot":
                pot_name ="Ceramic Pot"
                pot_price =250
                print("Ceramic Pot Price = ", ceramic_pot)

            else:
                pot_price=0
                print("No such Pot is Available.")

        case "no":
            pot_price=0
            pot_name="No Pot"
            print("Your Bill Amount is =",price)
            print("Thank you for Purchasing..")

        case __ :
            print("please choose between yes or no.")
            break
 
    fertilizer = input("Do you want Fertilizers (yes/no)? ").lower()
    match fertilizer :
        case "yes":
            fertilizer_price= 250
            print("Fertilizer Price is = ",fertilizer_price)

        case "no":
            fertilizer_price=0
            print("Thank you for Purchasing..")

        case __ :
            print("please choose between yes or no.")
            break

    bill = price + pot_price + fertilizer_price


    premium =  input("Are you a Premium member (yes/no)? ").lower()
    if premium == "yes" :
        while True :
            code=int(input("Enter the COUPON CODE : "))
            if code%2 ==0:
                print("<<< COUPON CODE IS VALID >>>")
                premium_bill =  (bill*5/100)
                print("Congrats! 5% Discount Applied")
                break
            else:
                print("INVALID COUPON CODE..")
                continue
        

    elif premium == "no":
        print("No Discount will be Applied ")
        print("Your Bill Amount is = ",bill)
        
    
    else:
        print("Incorrect statement")
        break

    gst = bill*4/100
    print("4% GST Added ")
    final_bill =(bill + gst ) - premium_bill

    print("=============== TOTAL BILL AMOUNT ===============")
    print("Customer Name : ",customer_name)
    print("Plant : ", plant_name)
    print("Plant price : ",price)
    print("Pot Name : ",pot_name)
    print("Pot Price : ",pot_price)
    print("Fertilizer Price : ",fertilizer_price)
    print("Premium User Discount : ",premium_bill)
    print("GST (4%) : ",gst)
    print("------------------------------------------------------------------------------------------------------------------")
    print("Final Bill : ",final_bill)
    print("------------------------------------------------------------------------------------------------------------------")

    another_buy =input("Do You want to Buy Another Plant (sure/no thanks)").lower()
    match another_buy:
        case "sure" :
            print("Please Continue Your Purchasing..😊")
            continue
        case "no thanks":
            print("Visit Again!")
            break
        case __ :
            print("Invalid statement")
            break

print("🌱 Thankyou For Visiting Green Leaf Nursery 🌱")

'''





            






            




