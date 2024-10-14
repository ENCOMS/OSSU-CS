"""
In a file called bitcoin.py, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins,
, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
- Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

import requests

try:
    ...
except requests.RequestException:
    ...

- Outputs the current cost of "n" Bitcoins in USD to four decimal places, using , as a thousands separator.
 """

import requests
import json
import sys


def main():
    # if there are or are not arguments to the program.
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    if len(sys.argv) == 2:
        try:
            user_input = float(sys.argv[1])
        except ValueError:
            sys.exit("Command-line argument is not a number")

    # Catch all the raised request exception
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # from JSON to dic object
        r_dic = r.json()
    except requests.RequestException:
        sys.exit("Error in the request")

    
    print(json.dumps(r.json(), indent=4))
    
    #status
    print(r.status_code)    


    # Operation
    btc_current = float(r_dic["bpi"]["USD"]["rate_float"])
    amount = user_input * btc_current


    # Result
    print(f"${amount:,.4f}")


if __name__ == "__main__":
    main()
