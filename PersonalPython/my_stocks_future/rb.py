#pip install robin_stocks
import robin_stocks.robinhood as r
from imessage import send_imessage
import time
import datetime

# Login to Robinhood
persons = ["Karthik"]
imessage_address = "karthikksayyaparaju@icloud.com"
message = ""

stocks = ["AAPL","NVDA","MU"]
cryptos = ["ETH","BTC"]

for person in persons:
    print("Person --> ", person)
    message = "Person --> " + person + "\n"
    if (person == "Karthik"):
        username = "skarthikkumar049@gmail.com"
        password = "654321@Usa"
    # elif(person == "Srivarsha"):
    # username = "srivarshapanguluri@gmail.com"
    # password = "654321@Usa"

    try:
        r.login(username, password)
        print("Login successfully.")
    except Exception as e:
        print(f"Login failed: {e}")

# Get the account profile
    profile = r.profiles.load_account_profile()


# Extract the account balance
    cash_balance = profile['cash_balances']['cash']
    positions = r.account.build_holdings()

    if(len(positions.items()) == 0):
        message += "\nYou own no position in Robinhood at this time.\n"

# Print the stocks you own
    for symbol, details in positions.items():
        message +=  f"Symbol: {symbol}" +"\n"
        message += f"Name: {details['name']}" +"\n"
        message += f"Quantity: {details['quantity']}" + "\n"
        message += f"Price: $ {details['price']}" + "\n"
        message += f"Equity: ${details['equity']}" + "\n"
        message += f"Percent Change: {details['percent_change']}%" + "\n"

message += f"\n List of stocks = [AAPL,NVDA,MU] \n\n"
now = datetime.datetime.now().ctime()

for stock in stocks:
    message += str(stock)+ " Stock price at  \n" + \
               str(now) + "\n" + \
               str(r.stocks.get_latest_price(stock)[0]) + "\n"

# for crypto in cryptos:
#         message += str(crypto) + " Crypto price at  \n" + \
#                    str(now) + "\n" + \
#                    str(r.crypto.get_crypto_info(crypto)) + "\n"
        # message += str(r.stocks.get_stock_historicals(inputSymbols=stock,interval="hour",
        #                                           span='4hour',bounds='regular',
        #                                           info=None)) + "\n"

print(message)
send_imessage(imessage_address, message)
try:
    r.authentication.logout
    print("Logged out successfully.")
except Exception as e:
    print(f"Logout failed: {e}")

