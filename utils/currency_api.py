import requests

def convert_currency(amount: float, from_currency: str, to_currency: str) -> float:
    api_url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount={amount}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        return data.get("result", 0.0)
    except requests.RequestException as e:
        raise RuntimeError(f"API request failed: {e}")