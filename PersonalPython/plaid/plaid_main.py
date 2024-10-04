import plaid
from plaid.api import plaid_api
from plaid.model.accounts_get_request import AccountsGetRequest
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.transactions_get_request_options import TransactionsGetRequestOptions
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest
import datetime

# Set up Plaid client
client = plaid_api.PlaidApi(plaid.ApiClient(configuration=plaid.Configuration(
    host=plaid.Environment.Sandbox,  # Use Development or Production environment for real data
    api_key={
        'clientId': 'your-client-id',
        'secret': 'your-secret',
        'plaidVersion': '2020-09-14'
    }
)))

# Exchange a public token for an access token
request = ItemPublicTokenExchangeRequest(public_token='your-public-token')
response = client.item_public_token_exchange(request)
access_token = response['access_token']

# Get account details
accounts_request = AccountsGetRequest(access_token=access_token)
accounts_response = client.accounts_get(accounts_request)
accounts = accounts_response['accounts']
print(accounts)

# Get transactions for the last 30 days
start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
end_date = datetime.datetime.now().strftime('%Y-%m-%d')

options = TransactionsGetRequestOptions(count=10)  # You can change the count as per your needs

transactions_request = TransactionsGetRequest(
    access_token=access_token,
    start_date=start_date,
    end_date=end_date,
    options=options
)

transactions_response = client.transactions_get(transactions_request)
transactions = transactions_response['transactions']

# Print transaction details
for transaction in transactions:
    print(f"Transaction: {transaction['name']}, Amount: {transaction['amount']}, Date: {transaction['date']}")