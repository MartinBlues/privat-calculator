#Calculator
import requests

def get_interest_rate(api_key):
  api_url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
  response = requests.get(api_url, headers={"Authorization": f"Bearer {api_key}"})

  if response.status_code == 200:
    data = response.json()
    for item in data:
      if item["ccy"] == "USD":
        return float(item["buy"])
  else:
    print("Failed to retrieve exchange rate from the API")

def compound_interest(principal, rate, years):
  return principal * (1 + rate/100) ** years

api_key = "abc123"

invest_sum = float(input("Enter sum in USD: "))
invest_rate = float(input("Enter percent: "))
invest_years = float(input("Enter years: "))

usd_exchange_rate = get_interest_rate(api_key)
if usd_exchange_rate:
  principal_uah = invest_sum * usd_exchange_rate
  rate_uah = invest_rate
  years = invest_years
  compound_interest_uah = compound_interest(principal_uah, rate_uah, years)
  print(f"Compound interest in UAH: {compound_interest_uah:.2f}")

