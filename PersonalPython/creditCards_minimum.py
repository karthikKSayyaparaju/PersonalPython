# Define a list of dictionaries, each representing a credit card with its balance, interest rate, and minimum payment percentage
credit_cards = [
    {'name': 'Card 1', 'balance': 0, 'interest_rate': 20, 'min_payment_percentage': 2},
    {'name': 'Card 2', 'balance': 5000, 'interest_rate': 15, 'min_payment_percentage': 1.5},
    {'name': 'Card 3', 'balance': 3000, 'interest_rate': 18, 'min_payment_percentage': 2.5},
    # Add more cards here if needed
]

def calculate_min_payment(balance, interest_rate, min_payment_percentage):
    # Calculate monthly interest (annual interest divided by 12)
    monthly_interest = (interest_rate / 100) / 12 * balance
    # Calculate minimum payment based on the percentage of the balance
    min_payment = max(min_payment_percentage / 100 * balance, monthly_interest)
    return round(min_payment, 2)

def total_min_payments(credit_cards):
    total_payment = 0
    for card in credit_cards:
        min_payment = calculate_min_payment(card['balance'], card['interest_rate'], card['min_payment_percentage'])
        total_payment += min_payment
        print(f"Minimum payment for {card['name']}: ${min_payment}")
    return round(total_payment, 2)

# Calculate total minimum payments across all credit cards
total_min_payment = total_min_payments(credit_cards)
print(f"\nTotal minimum payment across all cards: ${total_min_payment}")