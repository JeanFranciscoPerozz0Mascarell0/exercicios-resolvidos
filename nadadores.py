swimmers = []
best_time = 0
worst_time = 0
swimmer_best = ''
swimmer_worst = ''
arithmetic_average_sum = 0
arithmetic_average = 0
average_time = 0

for swimmer in range(3):
    swimmer_name = str(input(f"\nSwimmer name: "))
    swimmer_time = float(input(f"Swimmer time in seconds: "))

    swimmers.append({'name': swimmer_name, 'time': swimmer_time})
    
    arithmetic_average_sum += swimmer_time

    if(swimmer == 1):
        best_time = worst_time = swimmer_time
    else:
        if(swimmer_time < best_time):
            best_time = swimmer_time
            swimmer_best = swimmer_name
        if(swimmer_time > worst_time):
            worst_time = swimmer_time
            swimmer_worst = swimmer_name

    if swimmer_time >= 12 and swimmer_time <= 15:
        average_time += 1



arithmetic_average = arithmetic_average_sum / swimmer

print(f"The best time was {swimmer_best} with {best_time}.\n")
print(f"The worst time was {swimmer_worst} with {worst_time}.\n")
print(f"Number of swimmers time between 12 seconds and 15 seconds: {average_time}.\n")
print(f"The arithmetic average is {arithmetic_average}.")

for i in swimmers():
    for k, v in swimmers.items():
        print(f"{k} nadou por {v} segundos")
    print("--"*25)