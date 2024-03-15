import requests
import sys
import json

if len(sys.argv) == 1:
    print("Missing command-line argument")
    sys.exit(1)

try:
    # Number of bitcoins to buy
    num = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate = float(o["bpi"]["USD"]["rate_float"])
    num_change = rate * num
    print(f"${num_change:,.4f}")

except ValueError:
    print("Command-line argument is not a number")
    sys.exit(1)

except requests.RequestException:
    sys.exit(1)

