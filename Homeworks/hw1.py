"""
Smit Naik, Intro to Python Programming
Homework 1.1 , Due : June 21st, 2018
"""
#Problem:Exponientation with tidy border: start with the following code, which takes input from the user twice:

#Asking user to input integers

usr_in1 = input("Please enter an integer: ")
usr_in1 = int(usr_in1)
usr_in2 = input("Please enter another integer: ")
usr_in2 = int(usr_in2)

# Calculating exponientation of integers and converting to string, getting lenght.
usr_exp = usr_in1 ** usr_in2
len_exp = (len(str(usr_exp)) * "=" )
print (len_exp)
print (usr_exp)
print (len_exp)

#Homework1.2
"""
Tip calculator: write a restaurant bill calculator that takes three inputs: a restaurant bill total charge, the number of people who will be splitting the bill, and the desired tip in percent of the total bill.

"""
bill = float(input ("Please enter the total bill amount: "))
guests = int(input("Please enter the number of guests: "))
tip = float(input("Please enter desired tip percentage ( for example, \"20\" for 20% ): "))

#Calculating tip amount, and adding it to total
total_tip = (bill * tip * 0.01)
subtotal = (bill + total_tip)
subtotal_invd = subtotal / guests
#printing receipt by converting numbers in strings
print ( "A " + str(tip) + "% tip" + "($" + str(total_tip) + ") was added to the bill, for a total of $" + str(subtotal))
print ( "With " + str(guests) + " in your party, each person must pay $" + str(subtotal_invd))

#Homework1.3

product1_size = int(input("Please enter the unit size of Product 1: "))
product1_price = float(input("Please enter the price of Product 1: "))
product2_size = int(input("Please enter the unit size of Product 2: "))
product2_price = float(input("Please enter the price of Product 2: "))

product1_cost_unit = product1_price / product1_size
product2_cost_unit = product2_price / product2_size

diff1 = ((product1_cost_unit / product2_cost_unit) * 100)
diff2 = round(diff1, 2)
print(("Product 1 costs $" + str(product1_cost_unit) + " per unit"))
print(("Product 2 costs $" + str(product2_cost_unit) + " per unit"))
print(("Product 1 is " + str(diff2) + "% " + "the per-unit cost of Product 2"))

#Homework1.4


def get_price(symbol):
    import urllib.request, urllib.parse, urllib.error, urllib.request, pprint, ssl

    apikey = 'demo'

    url = ('https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
           '&symbol={symbol}&interval=1min&apikey={apikey}'
           '&datatype=csv'.format(symbol=symbol, apikey=apikey))

    # if you get a 'certificate' error, uncomment the next 3
    # commented lines and try again
    ctx = None
    # ctx = ssl.create_default_context()
    # ctx.check_hostname = False
    # ctx.verify_mode = ssl.CERT_NONE
    text = urllib.request.urlopen(url, context=ctx).read().decode('utf-8')

    try:
        quote = text.splitlines()[1].split(',')[4]
    except IndexError:
        if 'demo purposes' in text:
            exit('\n*** NOTE ***  This demo URL can only be used with MSFT.  '
                 'To obtain live data on other symbols, you must edit your '
                 'program to change "apikey = " variable in this function to '
                 'a user key you can obtain from the "alphavantage" service '
                 'by signing up for a free account.  See error message below: '
                 ' \n\n' + text)

        exit('error parsing response.  Response:  ' + text)

    return quote

aa = input('please input the stock symbol you would like to buy:  ')
bb = input('please input the cash you have to invest:  ')

cc = 100.6     # returns a string price
share = int(float(bb) / float(cc))
print(("with $" + str(bb) + " you can buy " + str(share) + " shares of " + str(aa) + " at $" + str(cc) + " per share"))
