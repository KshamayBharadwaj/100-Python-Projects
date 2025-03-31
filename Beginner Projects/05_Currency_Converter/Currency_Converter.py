import requests

# Step 1: Set up API details
API_KEY = "YOUR_API_KEY"  # Replace with your ExchangeRate-API key
BASE_URL = f"https://v6.exchangerate-api.com/v6/{API_KEY}/latest/"

# Step 2: Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = BASE_URL + from_currency  # API URL for the base currency
    response = requests.get(url)  # Send API request
    data = response.json()  # Convert response to JSON

    # Step 3: Check for errors
    if "error" in data:
        print("Invalid currency code. Please check and try again.")
        return

    # Step 4: Get conversion rate
    rates = data["conversion_rates"]
    
    if to_currency not in rates:
        print("Invalid target currency. Please check and try again.")
        return

    conversion_rate = rates[to_currency]
    converted_amount = amount * conversion_rate  # Convert amount

    # Step 5: Display result
    print(f"\n{amount} {from_currency} = {converted_amount:.2f} {to_currency}")

# Step 6: Run the app
if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_currency = input("Enter base currency (e.g., USD, INR): ").upper()
    to_currency = input("Enter target currency (e.g., EUR, GBP): ").upper()
    convert_currency(amount, from_currency, to_currency)
