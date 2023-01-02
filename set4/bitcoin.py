import requests
import sys

# Check if the user input correctly
if len(sys.argv) == 1:
    sys.exit("Missing command-line argument!")
elif len(sys.argv) != 2:
    sys.exit("Invalid Command-line argument! Please enter a floating point!")

try:
    bitcoin = float(sys.argv[1])
    
except ValueError:
    sys.exit("Invalid Command-line argument!")
else:
# Connect to the server to retrieve info
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    except requests.RequestException:
        sys.exit("Can't pull a request! Please retry!")
    # Pull the data and do the calculations
    data = response.json()
    bitcoin_USD_exchanger = data["bpi"]["USD"]["rate_float"]
    price = bitcoin * bitcoin_USD_exchanger
    print(f"${price:,.4f}")
