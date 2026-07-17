"""Check the value of a US Dollar in your Currency"""

import requests
import os
from dotenv import dotenv_values, load_dotenv

load_dotenv()

key = os.getenv("EXCHANGE_KEY")
def currency(amount,from_curr,to_curr):
    try:

        url = f"https://v6.exchangerate-api.com/v6/{key}/latest/{from_curr.upper()}"
        r = requests.get(url)
        r.raise_for_status()
        data = r.json()
        rate = data['conversion_rates']

        from_curr = from_curr.upper()
        to_curr = to_curr.upper()

        if from_curr not in rate:
            return f"{from_curr} is not a valid currency code"
        
        if to_curr not in rate:
            return f"{to_curr} is not a valid curruncy code"
        
        #convert amount to target curruncy
        converted = amount*rate[to_curr]
        return round(converted,2),None
     
    except requests.exceptions.RequestException as e:
        return {"Request not found",str(e)}
