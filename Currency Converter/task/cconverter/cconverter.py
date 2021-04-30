import requests
import json

# ask user to enter their currency
user_currency = input().lower()

# define url
URL = "http://www.floatrates.com/daily/" + user_currency + ".json"


# function to get data from url
def request(url):
    response = requests.get(url)
    currency_data = json.loads(response.text)
    return currency_data


request(URL)


def currency_converter(user_currency_):

    data = request(URL)

    # cache
    currency_list = {}

    if user_currency_ == 'usd':
        currency_list['eur'] = data['eur']['rate']
    elif user_currency_ == 'eur':
        currency_list['usd'] = data['usd']['rate']
    else:
        currency_list['usd'] = data['usd']['rate']
        currency_list['eur'] = data['eur']['rate']

    while True:
        # ask user which currency they want to exchange to
        exchange_currency = input().lower()
        # if no input provided exit
        if exchange_currency == '':
            break
        else:
            # ask user to enter the amount of money they want to exchange
            amount_of_money = float(input())
            print('Checking the cache...')
            if exchange_currency in currency_list:
                print('Oh! It is in the cache!')
                print(f'You received {round(amount_of_money * currency_list[exchange_currency], 2)} {exchange_currency.upper()}')
            else:
                print('Sorry, but it is not in the cache!')
                # add that currency to the currency list we have (cache)
                currency_list[exchange_currency] = data[exchange_currency]['rate']
                print(
                    f'You received {round(amount_of_money * currency_list[exchange_currency], 2)} {exchange_currency.upper()}')


currency_converter(user_currency)
