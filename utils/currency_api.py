import requests

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    """
    Convert an amount from one currency to another using a public exchange rate API.
    :param amount: The amount of money to convert.
    :param from_currency: The currency code of the source currency (e.g., "USD").
    :param to_currency: The currency code of the target currency (e.g., "EUR").
    :return: The converted amount.
    """
    # Use a public exchange rate API to fetch the conversion rate
    api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        # Extract the converted amount from API response
        return data.get("result", 0.0)
    except requests.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")