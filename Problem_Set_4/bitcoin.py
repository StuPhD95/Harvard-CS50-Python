import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=e6cbdb0999e010bc64abe884499a9df86b6ecc63b7e76d812ba9904b86e26793")
    bitcoin_price = float(response.json()["data"]["priceUsd"])
    result = bitcoin_price * n
    print(f"${result:,.4f}") # :,.4f = 4 d.p. using , as a thousands separator
except requests.RequestException:
    pass