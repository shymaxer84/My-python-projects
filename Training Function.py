import datetime as dt


def say_hello(name):
    time = dt.datetime.today()
    if 6 < time.hour <= 12:
        time_of_day = 'Morning'
    elif 12 < time.hour <= 16:
        time_of_day = 'Noon'
    elif 16 < time.hour <= 20:
        time_of_day = 'Evening'
    else:
        time_of_day = 'Night'
    print(f' Good {time_of_day} {name} The time is: {time.hour}:{time.minute}\n')


text_name = 'Dmitry'
say_hello(text_name)

euro_prices = [100, 200, 300]


def convert(price, coin_type):
    rates = {'USD': 3.52, 'EUR': 3.78}
    rate = rates[coin_type]
    result = round(price * rate, 2)
    # print(result)
    return result


# convert(100, 'USD')

nis_prices = [convert(price, 'EUR') for price in euro_prices]
for price in nis_prices:
    print(price)
