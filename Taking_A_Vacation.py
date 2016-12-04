def hotel_cost(nights):
    return 140 * nights

def plane_ride_cost(city):
    if city.lower() == 'charlotte':
        return 183
    elif city.lower() == 'tampa':
        return 220
    elif city.lower() == 'pittsburgh':
        return 222
    elif city.lower() == 'los angeles':
        return 475
    else:
        print('I don\'t know')

def rental_car_cost(days):
    if days >= 7:
        return (days * 40) - 50
    elif days >= 3:
        return (days * 40) - 20
    else:
        return days * 40

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money

print(trip_cost('Los Angeles', 5, 600))
