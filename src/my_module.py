
#Regular
#Rewards
def get_cheapest_hotel(number): 
    lakewood_prices = [110, 90, 80, 80]
    bridgewood_prices = [160, 60, 110, 50]
    ridgewood_prices = [220, 150, 100, 40]
    weekdays = ['mon', 'tues', 'wed', 'thu', 'fri']
    weekends = ['sat', 'sun']
    pay_weekdays = 0
    pay_weekend = 0

    client, date = number.split(": ") 
    days_scheduled = date.split(", ")
    if(client == 'Regular'):
        start_position = 0
    if(client == 'Rewards'):
        start_position = 2

    for day_scheduled in days_scheduled:
        for day in weekdays:
            if(day in day_scheduled):
                pay_weekdays += 1
        for day_end in weekends:
            if(day_end in day_scheduled):
                pay_weekend += 1 
    
    lakewood = lakewood_prices[start_position]*pay_weekdays + lakewood_prices[start_position+1] * pay_weekend
    bridgewood = bridgewood_prices[start_position]*pay_weekdays + bridgewood_prices[start_position+1] * pay_weekend
    ridgewood = ridgewood_prices[start_position]*pay_weekdays + ridgewood_prices[start_position+1]*pay_weekend

    if(lakewood < bridgewood):
        if(lakewood < ridgewood):
            cheapest_hotel = 'Lakewood'
        else:
            cheapest_hotel = 'Ridgewood'
    else:
        if(bridgewood < ridgewood):
            cheapest_hotel = 'Bridgewood'
        else:
            cheapest_hotel = 'Ridgewood'
    #DO NOT change the function's name
    return cheapest_hotel

#primeiramente - cortar a string
#verificar valores
#escolher 

# Lakewood - 3 
#           normal | fidelidade
#Semana ->  110    |     80
#Fim    ->  90     |     80


#Bridgewood - 4 
#           normal | fidelidade
#Semana ->    160  |    110
#Fim    ->    60   |    50

#Ridgewood - 5
#           normal | fidelidade
#Semana ->    220  |    100
#Fim    ->    150  |    40
