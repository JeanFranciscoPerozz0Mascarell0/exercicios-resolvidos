medicines = []


def lines_separation(state = False):
    print('-'*30 ,'\n')

#name = input(f"name of the medicine: ")
#medicines["name1"] = name
#price = int(input("price of the medicine: "))
#medicines["price1"] = price
#name = input(f"name of the medicine: ")
#medicines["name2"] = name
#price = int(input("price of the medicine: "))
#medicines["price2"] = price
#name = input(f"name of the medicine: ")
#medicines["name3"] = name
#price = int(input("price of the medicine: "))
#medicines["price3"] = price
#name = input(f"name of the medicine: ")
#medicines["name4"] = name
#price = int(input("price of the medicine: "))
#medicines["price4"] = price
#name = input(f"name of the medicine: ")
#medicines["name5"] = name
#price = int(input("price of the medicine: "))
#medicines["price5"] = price

arithmetic_average_sum = 0
smallest_number = 0

for c in range(1,6):
    medicine_name = str(input(f"name of the medicine: "))
    medicine_price = float(input("price of the medicine: R$ "))

    medicines.append({'name': medicine_name, 'price': medicine_price})
    arithmetic_average_sum = arithmetic_average_sum + medicine_price
    
    if(c == 1):
        smallest_number = medicine_price
    else: 
        if(medicine_price < smallest_number):
            smallest_number = medicine_price

        

#case1 = medicines[0]['price'] < medicines[1]['price'] and medicines[0]['price'] < medicines[2]['price'] and medicines[0]['price'] < medicines[3]['price'] and medicines[0]['price'] < medicines[4]['price']
#case2 = medicines[1]['price'] < medicines[0]['price'] and medicines[1]['price'] < medicines[2]['price'] and medicines[1]['price'] < medicines[3]['price'] and medicines[1]['price'] < medicines[4]['price']
#case3 = medicines[2]['price'] < medicines[0]['price'] and medicines[2]['price'] < medicines[1]['price'] and medicines[2]['price'] < medicines[3]['price'] and medicines[2]['price'] < medicines[4]['price']
#case4 = medicines[3]['price'] < medicines[0]['price'] and medicines[3]['price'] < medicines[1]['price'] and medicines[3]['price'] < medicines[2]['price'] and medicines[3]['price'] < medicines[4]['price']
#case5 = medicines[4]['price'] < medicines[0]['price'] and medicines[4]['price'] < medicines[1]['price'] and medicines[4]['price'] < medicines[2]['price'] and medicines[4]['price'] < medicines[2]['price']

#if(case1):
 #   smallest_number = medicines[0]['price']
#elif(case2):
#    smallest_number = medicines[1]['price']
#elif(case3):
 #   smallest_number = medicines[2]['price']
#elif(case4):
#    smallest_number = medicines[3]['price']
#elif(case5):
#    smallest_number = medicines[4]['price']

lines_separation(state=True)

print(f'The smallest price in the list is: {smallest_number}.')
arithmetic_average = arithmetic_average_sum / c
print(f'The arithmetic average of prizes is: R$ {arithmetic_average:.2f}')

lines_separation(state=True)
print(medicines)



